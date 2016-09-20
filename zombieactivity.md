# Zombie Activity
A python activity written by Kathleen Eckert in June 2015 with input from Sheila Kannappan.

### Activity 1: Frequentist Zombies

For this activity you will write your own code, but remember that you can use the [python quick reference card](http://user.physics.unc.edu/~sheila/PythonQuickReference.pdf) and codes from previous tutorials to help you write the code faster. You should work together with a partner or small group on this part. My solutions are provided in `zombies1.py.sln` in this repository.

A virus has gotten out that is turning humans into zombies. You as a scientist have been recording the % of zombies ever since the outbreak (~14 days ago). However the power has gone out for the past four days and your generator just kicked in allowing you to analyze the data and determine when there will be no humans left (`% humans = [1- % zombies] = 0`). Your data are in `percentzombie.txt` where `time=0` is the present day (`time = -14` is 14 days ago when you started taking data).

* a) Read in your data and plot it as % human vs. time as blue stars. The uncertainties on both time and % zombie are unknown.

* b) Evaluate the MLE slope & y-intercept and overplot the best fit line in green. What does the y-intercept value mean in the context of this situation? Are you a zombie?

* c) In the above step you have fit the data minimizing residuals in the y-direction (% human). How could you use `np.polyfit` to fit the data minimizing residuals in the x-direction (time)? Keep in mind that you can rewrite a line `y=a*x + b` as `x =(1/a)*y – (b/a)`. Over plot this fit in red – how does the y-intercept value change? Does this change your conclusion as to whether you are a zombie? In which variable should you minimize residuals to get the most accurate prediction of total zombification?

* d) Now assume your uncertainty on each % zombie measurements is ~3%. In a new plotting window, plot the residuals in % human from the linear fit from part b as green stars (residuals can be computed for either % human or time, but use % human since we have an estimated error for each data point of about 3%). Evaluate the reduced χ<sup>2</sup> for your data using residuals in % human as that is the measurement for which we have an uncertainty estimate. Is your model a good fit to the data? To get a sense for how much the reduced χ<sup>2</sup> should typically exceed 1, you can re-run your "Interpreting χ<sup>2</sup>" tutorial with the number of data points used here and a one-sided "detection" confidence of 1&sigma; (84% confidence interval integrated from -infinity). If 3% is an over- or under-estimate of the errors, how will this affect the reduced χ<sup>2</sup>?

* e) What happens when you increase the order of the fit (% humans vs. time)? Overplot the higher order fits on figure 1. What happens to the residuals if you increase the order of the fit (see **np.polyfit**, and optionally **np.polyval**)? Overplot the new residuals in time compared to the residuals from the linear fit from part b on figure 2.

* f) Calculate the reduced χ<sup>2</sup>for these higher order fits – do they yield as good a fit to the data as the linear fit?

### Activity 2: Bayesian Zombies

For this activity you will again write your own code, but remember that you can use the [python quick reference card](http://user.physics.unc.edu/~sheila/PythonQuickReference.pdf) and codes from previous tutorials to help you write the code faster. You should work together with a partner or small group on this part. My solutions are provided in `zombies2.py.sln` in this repository.

The scenario is the same: a virus has gotten out that is turning humans into zombies. You have been recording the % of zombies ever since the outbreak (~14 days ago). However the power has gone out for the past four days and your generator just kicked in allowing you to analyze the data and determine when there will be no humans left (`% humans = [1-% zombies] = 0`). where `time=0` is the present day (`time = -14` is 14 days ago when you started taking data). Use your Bayesian skills now to perform this analysis.

* a) Read in the data and plot it as % human vs. time in blue stars (Figure 1).

* b) Set up grids for your parameter space assuming a set of linear models for the data. Based on your output from `zombies1.py`, what ranges should you try? Compute the posterior distribution. Which prior should you want to use?

* c) Determine the marginalized posterior distribution for the percentage of humans today (`time=0`). Which parameter must you marginalize over? In Figure 2, plot the marginalized posterior distribution for the percentage of humans today (`time=0`) as red stars. What is the most likely % of humans alive today?

* d) Using the prior that you yourself are not a zombie yet, recompute the posterior distribution and determine the marginalized posterior distribution for % of humans alive today (`time=0`). In Figure 2, over plot the new marginalized posterior distribution as green dots.

* e) How does the Bayesian analysis for determining the % of humans today compare with the value from the MLE fit from the Frequentist Zombies activity?

