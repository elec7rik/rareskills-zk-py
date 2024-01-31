# Using lagrange interpolation to find a curve that fits (x,y) points

import numpy as np
from scipy.interpolate import lagrange

x = np.array([1,2,3])
y = np.array([4,18,12])

poly = lagrange(x,y)

print(poly)
