from numpy import *
from pylab import *

import numpy

#goes from y=0, y=1.1
v_o_max = 1.1

#
v_sat = 3.0
A = v_o_max/pi

k_0=0.3
k_1=0.65

x = arange(-15.0, 15.0, 0.01)
y = 0.5*v_o_max + A*numpy.arctan(x/v_sat - k_1)

plot(x, y, linewidth=1.0)
grid(True)
show()

#for x in range(0,100):
#	print (math.atan(x))
