# Model Fitting: Frequentist and Bayesian Approaches

A python tutorial by Kathleen Eckert adapted from tutorials by Sheila Kannappan & Amy Oldenberg June 2015. Edited by Rohan Isaac and Sheila Kannappan Sept. 2016.

In this repository there are python codes, [paramfit1.py](paramfit1.py) and [paramfit2.py](paramfit2.py), that contain partial answers for you to finish.

**Why do we fit models to data?**

-   To understand the underlying distribution of the data
-   To test hypotheses or competing theoretical models
-   To predict values for future observations

These are just a few examples of why we might want to fit models to data. In this tutorial we will go through the basics of determining model parameters using two different techniques: Frequentist Maximum Likelihood Parameter Estimation and Bayesian Posterior Distribution Parameter Estimation.

## Part I: Frequentist Estimation of Model Parameters

*Least Squares Fitting* is based on the assumption that all the measurement uncertainties &sigma; in a data set are the same, i.e., follow the same Gaussian distribution. In the case of a linear model, the least squares fit gives the slope & y-intercept parameters that minimize the mean square residuals between the data and the model, where the residuals are measured in the y-direction in the case of "forward" fitting. Here the mean square residuals are given by: <img src="https://latex.codecogs.com/png.latex?\mathrm{rms}^2=\frac{1}{N}\sum{\left(y_i-\left(\alpha&space;x_i&plus;\beta\right)\right&space;)^2}"/> where x<sub>i</sub> is the independent variable, y<sub>i</sub> is the dependent variable, and α and β are the slope and y-intercept parameter values. Minimizing the mean square residuals is equivalent to minimizing the rms (root mean square) residuals, and also equivalent to minimizing the &chi;<sup>2</sup>, because of the fact that all &sigma;'s have been assumed to be identical.

Least Squares Fitting falls within the broader category of parameter estimation known as *Maximum Likelihood Estimation (*MLE). In this method, we measure the likelihood for a given model using the χ<sup>2</sup> statistic:

The likelihood is given by: <img src="https://latex.codecogs.com/png.latex?L=\exp{\frac{-\chi^2}{2}}"/> where <img src="https://latex.codecogs.com/png.latex?\chi^2=\sum\frac{\left(y_{value,i}-y_{model,i}\right)^2}{\sigma_i^2}"/>

To find the MLE solution to our model, we maximize the likelihood function by taking the derivative with respect to each parameter (the slope and y-intercept in the case of a linear fit) and by solving for where each derivative is equal to 0. To simplify the math, we first take the natural log of the likelihood function. For least squares fitting (wherein all &sigma; values are taken to be equal), it is possible to obtain an analytical solution for the slope and y-intercept of a linear model. The derivation is shown below:

Take the natural log of the likelihood function <img src="https://latex.codecogs.com/png.latex?\ln(L)=-\frac{1}{2}\chi^2=-\frac{1}{2}\sum\frac{\left(y_i-\left(\alpha&space;x_i&plus;\beta\right)\right&space;)^2}{\sigma_i^2}"/>

Take the derivatives of ln(L) with respect to α and β and set those equations to 0:
<img src="https://latex.codecogs.com/png.latex?\frac{d\ln(L)}{d\alpha}=-\sum\frac{\left(y_i-\left(\alpha&space;x_i&plus;\beta\right)\right)(-x_i)}{\sigma_i^2}=0"/> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; and &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img src="https://latex.codecogs.com/png.latex?\frac{d\ln(L)}{d\beta}=-\sum\frac{\left(y_i-\left(\alpha&space;x_i&plus;\beta\right)\right)(-1)}{\sigma_i^2}=0"/> .

If we assume the σ<sub>i</sub>'s are all the same, then we have two equations for two unknowns to solve:

**eqn 1:** <img src="https://latex.codecogs.com/png.latex?\sum&space;y_i&space;x_i-\alpha\sum&space;x_i^2-\beta\sum&space;x_i=0"/> 

**eqn 2:** <img src="https://latex.codecogs.com/png.latex?\sum&space;y_i-\alpha\sum&space;x_i-N\beta=0"/> 

Multiply eqn 1 by N and multiply eqn 2 by <img src="https://latex.codecogs.com/png.latex?\sum&space;x_i"/> to get:

**eqn 1** <img src="https://latex.codecogs.com/png.latex?N\sum&space;y_i&space;x_i-N\alpha\sum&space;x_i^2-N\beta\sum&space;x_i=0"/> 

**eqn 2** <img src="https://latex.codecogs.com/png.latex?\sum&space;x_i\sum&space;y_i-\alpha\sum&space;x_i\sum&space;x_i-N\beta\sum&space;x_i=0"/> 

Now we can set these two equations equal to each other:

<img src="https://latex.codecogs.com/png.latex?N\sum&space;y_i&space;x_i-N\alpha\sum&space;x_i^2=\sum&space;x_i\sum&space;y_i-\alpha(\sum&space;x_i)^2"/>

Solving for α and dividing the top and bottom by N<sup>2</sup>:

<img src="https://latex.codecogs.com/png.latex?\alpha=\frac{\bar{x}\bar{y}-\bar{xy}}{\bar{x}^2-\bar{(x^2)}}"/>

where the bar over the variable signifies the mean value of that quantity.

Now we can go back and solve for β:

from **eqn 2** <img src="https://latex.codecogs.com/png.latex?\beta=\bar{y}-\alpha\bar{x}"/> 

For more complicated functions or if the uncertainties are not uniform, setting the derivatives of the likelihood equal to zero may not lead to equations that are easily solved analytically, so we typically use programs such as `np.polyfit` to determine the parameters numerically.

### Activity 1: [paramfit1.py](paramfit1.py)

In `paramfit1.py` we create fake data with known slope and y-intercept. We then compute the maximum likelihood estimated slope and y-intercept for the fake data. Fill in lines ending with "?" and answer questions by putting your own comments in the code.

* a) Run the program `paramfit1.py` and plot the data. What aspect of a real data set is `npr.normal` used to emulate? What assumption is made in the code that is key to the least squares approach?

* b) Read over the derivation for the linear least squares analytical solution (above) and add code to compute the estimated slope and y-intercept based on the fake data set. Plot the maximum likelihood ("best fit") solution on top of the data.

* c) For linear least squares fitting, we can obtain analytical formulae for the uncertainties on the slope
and y-intercept estimates, which have been provided below. (See http://mathworld.wolfram.com/LeastSquaresFitting.html for the full derivation.)<br><br>
<img src="https://latex.codecogs.com/png.latex?\sigma_\alpha=\sqrt{\frac{\sum\left(y_i-\left(\alpha&space;x_i&plus;\beta\right)\right&space;)^2}{(N-2)\sum(x_i-\bar{x})^2}}"/><br>
<img src="https://latex.codecogs.com/png.latex?\sigma_\beta=\sqrt{\left(\frac{\sum\left(y_i-\left(\alpha&space;x_i&plus;\beta\right)\right)^2}{N-2}\right)&space;\left(\frac{1}{N}+\frac{(\bar{x})^2}{\sum(x_i-\bar{x})^2}\right)}"/><br><br>
Uncomment the code to compute the uncertainties for the slope and y-intercept analytically. Which parameter has larger fractional
uncertainty?

* d) Read up on `np.polyfit`: http://docs.scipy.org/doc/numpy/reference/generated/numpy.polyfit.html <br><br>
Use `np.polyfit` to compute the MLE slope and y-offset for the data set numerically rather than analytically. Do you get the same result as in the analytical case from part b? Note that `np.polyfit` does not automatically take an array of uncertainties on the y value. If the uncertainty on each data point is different, we can input an optional weight vector: `fit=np.polyfit(xvals, yvals, 1, w=1/sig)` where `sig` is an array containing the uncertainty on each data point. Note that the input is `1/sig` rather than `1/sig**2` as you might expect from the equations above. The `np.polyfit` function squares the weight value within the source code.<br><br>
In this example we have assumed that the &sigma; on all data points is the same. This simplified assumption is often not the case. If the uncertainties are different, then we must include each data point's uncertainty within the MLE calculation.

* e) One numerical method to determine uncertainties is to have `np.polyfit` compute the covariance matrix:
<img src="https://latex.codecogs.com/png.latex?C=\begin{pmatrix}\sigma_a^2&cov(\alpha,\beta)\\cov(\alpha,\beta)&\sigma_\beta^2\end{pmatrix}"/> which is the inverse of the Hessian Matrix, consisting of second derivatives of the log likelihood with respect to different model parameters. (When these matrices get tricky to compute, we can resort to a more approximate numerical technique such as the bootstrap.)<br><br>
`np.polyfit` will compute the covariance matrix numerically if you add `cov="True"` to the `np.polyfit` function call. Print out the uncertainties computed using the covariance matrix. Are they the same as the analytical solution? What happens to the uncertainties if you increase/decrease the number of data points? What happens to the percentage difference between the analytical and numerical methods if you increase/decrease the number of data points?

## Part II: Bayesian Estimation of Model Parameters

*Bayesian analysis* presents an entirely different philosophy compared to frequentist analysis. In part I we determined the likelihood of the data given the model, which presumes one model and many possible data sets. The data set in activity 1 was imagined to be an example data set drawn from many possible experiments, which we could mathematically model assuming the other experiments would provide data points distributed in Gaussian fashion around the measured data points (i.e., the standard sleight of hand of statistics, substituting the observed data distribution for "true" parent distribution). In the Bayesian framework, however, we do not imagine many possible experiments that have not actually been conducted. Instead, we determine the likelihood of the model given the data, meaning we consider many models and only one data set.

#### Bayes's Theorem

<img src="https://latex.codecogs.com/png.latex?P(M|D)=\frac{P(D|M)*P(M)}{P(D)}"/>

1. P(D|M) - the likelihood (as in part I), this is read as “probability of the data given the model”
2. P(M) - the prior probability (known information about the model set, an example is a flat prior, which weights all parameter possibilities hence all models equally)
3. P(D) - probability of the data, essentially a normalization factor
4. P(M|D) - the posterior probability distribution of the model given the data

Whereas in MLE, we maximized the likelihood function to find the single "best" set of parameters, in Bayesian analysis we construct the posterior probability distribution, which is the distribution of probabilities that each model is correct in a set of models defined by different parameter values. A common approach is to generate a grid of models spanning parameter value ranges where we think our parameters are likely to be, meaning we set the "prior" to 0 outside these ranges. To do this in practice, we compute the likelihood of the data given each model multiplied by the prior for each model over the entire model grid. In many problems scientists will assume a flat prior (all grid points weighted equally), and then the posterior probability distribution is proportional to the likelihood distribution.

### Activity 2: [paramfit2.py](paramfit2.py)

In `paramfit2.py` we will use the same fake data set created in `paramfit1.py`. This time, however, we will determine the slope and y-intercept through Bayesian analysis by constructing a grid of possible values of the slope and y-intercept and evaluating the posterior probability at each grid point. Fill in any lines of code ending in "?".

* a) Run `paramfit2.py` and plot the fake data. The code has preset grids for the y-intercept and slope values. What values are being considered? What are the implicit priors on the slope and y-intercept?

* b) Check that the model space from the choice of grid values for both the y-intercept and slope is also uniformly distributed. To do this plot a series of lines using all possible y-intercepts (`y=x+beta_i`) and then all possible slopes (`y=x*alpha_i`). Is the model space from the y-intercept parameter evenly spaced? Is the model space from the slope parameter evenly spaced? Note that uniform priors can be uniform in the parameter or in a function of the parameter, e.g. slope, log(slope), tan(slope), depending on what physically makes sense. What is a physically motivated definition of "evenly spaced" for the slope, based on studying the plots?

* c) Read through the first part of http://jakevdp.github.io/blog/2014/06/14/frequentism-and-bayesianism-4-bayesian-in-python/ from "Test Problem: Line of Best Fit" through "Prior on Slope and Intercept", stopping at "Prior on &sigma;". How can we write a prior that compensates for the non-uniform weighting of the angles?
**Note that in the article the definition of alpha and beta are reversed to be y = α + βx. ** 

* d) Using the fake data, compute the posterior probability distributions (posterior distributions for short) for the entire grid assuming 1) flat priors on the values of the slopes and y-intercepts (non-uniform in the angle) and 2) the prior that compensates and creates a uniform angular distribution. Pay attention to where the prior appears in the equation for computing the posterior probabilities. (Note: we do not need to normalize the prior distribution to sum to 1 because we will consider only relative, not absolute probabilities.)

* e) Now that we have our posterior distribution over the entire parameter space, we can find the posterior distributions of our individual parameters by summing over the posterior distributions of the other parameters (i.e., if we want to look at the posterior distribution of the slope, we sum over the posterior distribution of the y-intercept). We call this procedure "marginalizing."
(See diagram.)

![](jointmarginalsmall.jpg)

Plot the marginalized posterior distributions of the slope using the two different priors (green for flat and red for compensating). Are there any differences (you may need to zoom in)? How do the marginalized posterior distributions of the slope compare with the MLE values from paramfit1.py? Estimate the uncertainty on the slope value from the plot by eye (you may need to zoom in on the region of significant probability). How does the uncertainty on the slope compare with the MLE value? Do the same for the y-intercept. What happens to the marginalized posterior distributions for the slope and y-intercept if you change the number of data points (try N=100, N=10)? What happens if you change the grid spacing (try slope ranges from 1-10 in steps of 0.1, y-int ranges from 1-10 in steps of 1)?

In Bayesian analysis, it is important to think about the questions you are trying to answer when setting up the problem. Starting with a well understood model grid and set of priors is key. In this case do you want a flat prior on the slope and y-intercept, or do you want a prior that compensates for the unequal distribution in angles? What range do you want to compute your data over? How finely should you bin the grids?

For more information on the Bayesian approach, additional tutorials are available at [this website](http://jakevdp.github.io/blog/2014/06/14/frequentism-and-bayesianism-4-bayesian-in-python/).

## Part III: Zombies!

To cement your understanding, complete this [coding activity](https://github.com/galastrostats/ModelFittingTutorial/blob/master/zombieactivity.md) in which the codes are not written for you.

