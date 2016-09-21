# Choosing Between Fitting Methods and Scatter Estimators in the Frequentist Paradigm



Construct two 100-element “data sets” x and y such that x ranges from 1-10 and y ranges from 20-40.  Note that x and y should vary smoothly, with no randomness. If you plot y vs. x, you see the “true” relation with no measurement errors or biases.

Now add random Gaussian scatter to y with a sigma of 1. Also choose ~10 elements of y to give extra “systematic” errors of 2-3 by hand (hint – systematic errors all go in one direction, unlike random errors).  Plot y vs. x. Fit the data using forward, inverse, and bisector fits and overplot the fits. The bisector slope and intercept are given in Table 1 and equation 8 of [Isobe et al. 1990](http://adsabs.harvard.edu/abs/1990ApJ...364..104I). Label the fits and comment on which one appears most correct. In fact the lowest rms scatter corresponds to the most correct fit -- why? 

For each fit, compute the rms scatter as well as the biweight scatter in the y-direction (use the formula for the biweight scatter S<sub>BI</sub> from [Beers, Flynn, & Gebhardt 1990](http://adsabs.harvard.edu/abs/1990AJ....100...32B). Which measures the scatter more accurately?

Now, add Gaussian scatter to x with a sigma of 3 and repeat your fits and scatter measurements. Which type of fit appears most correct now? Consider your “gut feeling” as well as the original true relation. Why might these not agree? Why does the lowest rms scatter in y not correspond to the best fit anymore? Can you see another way of computing the rms scatter by which the best fit would in fact correspond to the lowest scatter? Why do the biweight and rms scatter look similar now?

Finally, add a selection bias on x, such that x cannot be detected below 3. Repeat your fits and again discuss which fit appears most correct vs. is actually most correct.

All of the above assumed that the goal was to measure the true, underlying relationship between x and y.  What if your goal were to find the best predictive relation between the two, in order to predict y with greatest accuracy for a given x. How would the optimal choice of fit type change in this case?
