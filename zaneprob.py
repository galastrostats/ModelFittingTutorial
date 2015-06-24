# run scatter.py assert tests if something is true, if change problem get an error

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import scipy as sp
import scipy.stats as stats
import numpy.random as npr
import pylab
pylab.ion()
import scatter as sc
import neldermead as nm


# evaluate himmel function at several grid points:
testoutparam1=np.arange(-5,5,0.1)
testoutparam2=np.arange(-1,1,0.1)


gridout=np.zeros((np.size(testoutparam1),np.size(testoutparam2)))
gridoutx=np.zeros((np.size(testoutparam1),np.size(testoutparam2)))
gridouty=np.zeros((np.size(testoutparam1),np.size(testoutparam2)))

for i in np.arange(np.size(testoutparam1)):
    for j in np.arange(np.size(testoutparam2)):
      print i, j
      gridout[(i,j)]=sc.simulate(np.array([testoutparam1[i],testoutparam2[j]]))
      gridoutx[(i,j)]=testoutparam1[i]
      gridouty[(i,j)]=testoutparam2[j]

# plot himmel function as surface plot
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.plot_surface(gridoutx,gridouty,gridout)

# run neldermead on himmel function
# neldermead.py as default evaluates the known minima of a parabola


# setup 3 points
#i_simp = [np.array([-2.0, -2.0]),
#          np.array([0.0, 2.0]),
#          np.array([2.0, -2.0])
#          ]
i_simp = [np.array([-5.0, -5.0]),
          np.array([0.0, 5.0]),
          np.array([-5.0, 5.0])
          ]
max_iters = 200
tol = 1e-7
min_pos = nm.minimize(sc.simulate, i_simp, max_iters, tol)

print min_pos
