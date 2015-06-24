"""
Part I, First activity in Parameter Fitting Tutorial
Modified by Katie Eckert from ASTR502 activity written by Sheila Kannappan
June 24, 2015
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.random as npr
import pylab
pylab.ion()


# Generating fake data set to start with:
alphatrue=2. # slope
betatrue=5.  # intercept
errs=2.5 # sigma (amplitude of errors)

narr=50. # number of data points
xvals = np.arange(narr) + 1. # xvals range from 1-51
yvals = alphatrue*xvals + betatrue+ npr.normal(0,errs,narr) # yvals 
# What does npr.normal do?

# Plot fake data
plt.figure(1) 
plt.clf()
plt.plot(xvals,yvals,'b*',markersize=10)
plt.xlabel("x-values")
plt.ylabel("y-values")

# Determine slope & y-intercept using analytic solution from derivation sheet

#alphaest=(np.mean(xvals)*np.mean(yvals)-np.mean(xvals*yvals)) / \
#   (np.mean(xvals)**2 -np.mean(xvals**2)) #  from derivation
#betaest= ? # calculate estimate of y-intercept from derivation


# What are MLE values of slope and y-intercept?

#print("analytical MLE slope = %f" %alphaest)
#print("analytical MLE y-intercept = %f" %?)

# Overplot the best fit solution
#yfitvals=xvals*alphaest+betaest
#plt.plot(xvals,yfitvals,'r')

# What have we assumed about the uncertainties on our data?

# Compute analytic uncertainties on slope and y-intercept 

#alphaunc=?
#betaunc=?

#print("analytical MLE uncertainty on alpha is %0.7f" % (alphaunc))
#print("analytical MLE uncertainty on beta is %0.7f" % (betaunc))

#print("fractional uncertainty on alpha is %0.7f" % (alphaunc/alphaest))
#print("fractional uncertainty on beta is %0.7f" % (?))


# Solution using python solver np.polyfit
# third parameter is order of fit, 1 for linear
#pfit=np.polyfit(xvals,yvals,1) # returns highest power first 

#print("               ") # put in some whitespace to make easier to read
#print("np.polyfit MLE slope = %f" %pfit[0])
#print("np.polyfit MLE y-intercept = %f" %?)

# Do you get the same result as in analytical case?

# Note that not all problems have analytical solutions like linear regression

# Can also obtain errors from the diagonal terms of the covariance
# matrix, which is the inverse of the Hessian matrix (from your pre-reading) and
# can be computed in np.polyfit by setting cov='True'

#pfit,covp=np.polyfit(xvals,yvals,1,cov='True') # returns highest power first
# setting cov='True' returns the covariance matrix
# how do we get the errors from it?
#print("slope is %0.7f +- %0.7f" % (pfit[0], np.sqrt(covp[0,0])))
#print("intercept is %0.7f +- %0.7f" % (?, ?)

# Are those errors the same as in analytical solution?
# What happens to the uncertainties if you increase/decrease the number of points used in the fit (try N=100, N=10) ?
# What happens to the percentage difference between the analytical and numerical methods for computing the uncertanties if you increase/decrease the number of points (try N=100, N=10)?




