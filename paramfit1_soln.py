"""
Part I, First activity in Parameter Fitting Tutorial
Modified by Katie Eckert from ASTR502 activity written by Sheila Kannappan
June 24, 2015
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.random as npr

# Generating fake data set to start with:
alphatrue=2. # slope
betatrue=5.  # intercept
errs=2.5 # sigma (amplitude of errors)

narr=50 # number of data points
xvals = np.arange(narr) + 1. # xvals range from 1-51
yvals = alphatrue*xvals + betatrue + npr.normal(0,errs,narr) # yvals 
# What aspect of a real data set does npr.normal emulate here?
# What assumption is made here that is key to the least squares approach?
'''
It's emulating random measurement errors with amplitude sigma=errs.
The code is assuming that these errors have the same amplitude for all 
data points, which is key to the unweighted least squares approach.
'''

# Plot fake data
plt.figure(1) 
plt.clf()
plt.plot(xvals,yvals,'b*',markersize=10)
plt.xlabel("x-values")
plt.ylabel("y-values")

# Determine slope & y-intercept using least squares analytic solution 

alphaest=(np.mean(xvals)*np.mean(yvals)-np.mean(xvals*yvals)) / \
   (np.mean(xvals)**2 -np.mean(xvals**2)) #  from derivation
betaest= np.mean(yvals) - alphaest * np.mean(xvals) # calculate estimate of y-intercept from derivation
# Why must we use alphaest rather than alphatrue in the above formula?
'''
These formulae represent our best *estimates* of the slope and intercept from 
the *data*. We do not a priori know the true slope when working with real 
data, so we cannot use our knowledge of it in this analysis.
'''

# The MLE values of the slope and y-intercept are equivalent to the least
# squares fit results.
print("analytical MLE slope = %0.7f" %alphaest)
print("analytical MLE y-intercept = %0.7f" %betaest)

# Overplot the MLE ("best fit") solution
yfitvals=xvals*alphaest+betaest
plt.plot(xvals,yfitvals,'r')

# Compute analytic uncertainties on slope and y-intercept 

alphaunc = np.sqrt(np.sum((yvals - (alphaest*xvals+betaest))**2) / ((narr-2.)*(np.sum((xvals-np.mean(xvals))**2))))
betaunc = np.sqrt((np.sum((yvals - (alphaest*xvals+betaest))**2) / (narr-2.)) * ((1./narr) + (np.mean(xvals)**2)/np.sum((xvals-np.mean(xvals))**2)) )

print("analytical MLE uncertainty on alpha is %0.7f" % (alphaunc))
print("analytical MLE uncertainty on beta is %0.7f" % (betaunc))

print("fractional uncertainty on alpha is %0.7f" % (alphaunc/alphaest))
print("fractional uncertainty on beta is %0.7f" % (betaunc/betaest))
# Which parameter has larger fractional uncertainty?
'''
The intercept beta has much larger fractional uncertainty.
'''

# Solution using python solver np.polyfit
# third parameter is order of fit, 1 for linear
pfit = np.polyfit(xvals, yvals, 1) # returns coeff. of highest order term first

print("               ") # put in some whitespace to make easier to read
print("np.polyfit MLE slope = %0.7f" %pfit[0])
print("np.polyfit MLE y-intercept = %0.7f" %pfit[1])

# Do you get the same result as in analytical case?
'''
Yes, the result is the same.
'''

# Note that most problems do not have analytical solutions

# Can also obtain errors from the diagonal terms of the covariance
# matrix, which is the inverse of the Hessian matrix and
# can be computed in np.polyfit by setting cov='True'

pfit,covp = np.polyfit(xvals, yvals, 1, cov='True') # returns highest power first
# setting cov='True' returns the covariance matrix
# how do we get the errors from it?
print("slope is %0.7f +- %0.7f" % (pfit[0], np.sqrt(covp[0,0])))
print("intercept is %0.7f +- %0.7f" % (pfit[1], np.sqrt(covp[1,1])))
'''
The error estimate comes from the square root of the corresponding diagonal term.
'''

# Are those errors the same as in the analytical solution?
'''
They agree closely but are not identical.
'''
# What happens to the uncertainties if you increase/decrease the number of points used in the fit (try N=100, N=10) ?
'''
The uncertainties get larger for N=10, smaller for N=100.
'''
# What happens to the percentage difference between the analytical and numerical methods for computing the uncertanties if you increase/decrease the number of points (try N=100, N=10)?
'''
The percentage difference between methods gets larger for N=10, smaller for N=100.
'''
