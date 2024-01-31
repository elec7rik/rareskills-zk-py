# Polyomial addition is homomorphic to vector addition

import numpy as np 
from scipy.interpolate import lagrange

x = np.array([1,2,3,4])
y_v1 = np.array([0,8,6,12])         # first vector
y_v2 = np.array([4,12,16,22])       # second vector

poly_v1 = lagrange(x,y_v1)
poly_v2 = lagrange(x,y_v2)

print(poly_v1)                      # represents polynomial corresponding to the first vector
print(poly_v2)                      # represents polynomial corresponding to the second vector

poly_v3 = lagrange(x,y_v1+y_v2)     # represents polynomial corresponding to the sum of 2 vectors

'''
using np.allclose() since the polynomial objects created by lagrange have floating point values
so direct comparison using == doesnt work
'''
coeff_equal = np.allclose(poly_v3.c, (poly_v1 + poly_v2).c)
assert coeff_equal, "system contains an inequality"
