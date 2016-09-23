"""
paramfit2.py rewritten to perform multiple runs and compare priors 
(S. Kannappan Sept. 2016; loosely based on code by Eckert/Kannappan June 2015)
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.random as npr

timetest = False
if timetest: import time

usemethod = "vectorized" # "vectorized" or "doubleloop"

# True parameters for generating fake data
alphatrue=2. # slope
betatrue=5.  # intercept
errs=2.5 # sigma (amplitude of errors)

# Generate fake data
ndata=10 # number of data points
xvals = np.arange(ndata) + 1.
# yvals will be generated inside nruns loop -- different errors every time

# Grids of parameters to test
nalpha = 1000
nbeta = 100
alphaposs = np.linspace(0,10,nalpha,endpoint=False)
betaposs = np.linspace(0,10,nbeta,endpoint=False)

# Priors to test (all implicitly zero outside alpha, beta ranges)
prioronintercept = 1.
comparepriors = False
if comparepriors: # plot three possible slope priors
    plt.figure(2,figsize=(5, 3.75))
    plt.plot(alphaposs,np.zeros(nalpha)+1.,color="red",label="flat in slope")
    plt.plot(alphaposs,np.cos(np.arctan(alphaposs))**2,color="green",label="flat in angle")
    plt.plot(alphaposs,(1.+alphaposs**2)**(-3./2),color="purple",label="symmetric")
    plt.ylim(0,1.1)
    plt.legend(loc="best")

# Uncomment one of three below
prioronslope, priorname, pcolor = np.zeros(nalpha)+1., "flat in slope", "red"
#prioronslope, priorname, pcolor = np.cos(np.arctan(alphaposs))**2, "flat in angle", "green"
#prioronslope, priorname, pcolor = (1.+alphaposs**2)**(-3./2), "symmetric", "purple"
# http://jakevdp.github.io/blog/2014/06/14/frequentism-and-bayesianism-4-bayesian-in-python/
prior = prioronintercept * prioronslope
if usemethod != "doubleloop": 
    prior = prior.reshape(nalpha,1)

nruns=1000
slopeposteriors = np.zeros((nruns,nalpha))

irun = 0
while irun < nruns:

    # generate yvals with random errors   
    yvals = alphatrue*xvals + betatrue + npr.normal(0,errs,ndata)
    
    # start clock
    if timetest: init_time = time.clock()   
 
    # compute Bayesian numerical solution finding the posterior probability 
    # distribution for the full model grid using P(M|D) = P(D|M)*P(M)/P(D)
    # (except we'll ignore P(D) as it's just a normalization)
    # note postprob = exp(-1*chisq/2)*prior can exceed computational capabilities
    # so we'll use the log-space equivalent ln(postprob) =-1*chisq/2 + ln(prior) 

    if usemethod == "doubleloop":
        lnpostprob=np.zeros((nalpha,nbeta))
        for i in xrange(nalpha):  # loop over all possible values of alpha
            for j in xrange(nbeta): # loop over all possible values of beta
                modelvals = alphaposs[i]*xvals+betaposs[j] # compute yfit for given model
                resids = (yvals - modelvals) # compute residuals for given grid model
                chisq = np.sum(resids**2 / errs**2) # compute chisq 
                lnpostprob[i,j] = (-1./2.)*chisq + np.log(prior[i])      
    else:
        if usemethod != "vectorized":
            print "warning, using vectorized method not "+usemethod+" method"
        modelgridterm1 = alphaposs.reshape(1,nalpha) * xvals.reshape(ndata,1) 
        modelgrid = modelgridterm1.reshape(ndata,nalpha,1) + betaposs.reshape(nbeta,1,1).T
        residgrid = yvals.reshape(ndata,1,1) - modelgrid
        chisqgrid = np.sum(residgrid**2/errs**2,axis=0)        
        lnpostprob = (-1./2.)*chisqgrid + np.log(prior)     

    # end clock and print time
    if timetest:
        elapsed_time = time.clock() - init_time  # finds difference
        print "Time elapsed is %0.3f ms" % (elapsed_time*1000)  # converts to ms

    postprob=np.exp(lnpostprob)
    marginalizedpostprob_slope = np.sum(postprob,axis=1) / np.sum(postprob)
    slopeposteriors[irun,:] = marginalizedpostprob_slope
    
    irun += 1    

plt.figure(1,figsize=(5, 3.75))
cumprobgrid = np.cumsum(np.sum(slopeposteriors,axis=0))
halfprob = np.argmin(np.abs(cumprobgrid - 0.5*max(cumprobgrid)))
print "median slope %f for %s" % (alphaposs[halfprob], priorname)
plt.plot(alphaposs,np.sum(slopeposteriors,axis=0),color=pcolor,label=priorname)
plt.legend(loc="best")