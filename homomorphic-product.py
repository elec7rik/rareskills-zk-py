# Polyomial multiplication is homomorphic to vector Hadamard product

import numpy as np 
from scipy.interpolate import lagrange

x = np.array([1,2,3,4])
y_v1 = np.array([0,8,6,12])         # first vector
y_v2 = np.array([4,12,16,22])       # second vector
y_prod = np.multiply(y_v1,y_v2)     # product vector

poly_v1 = lagrange(x,y_v1)
poly_v2 = lagrange(x,y_v2)
poly_prod = poly_v1*poly_v2

print(poly_v1)                      # represents polynomial corresponding to the first vector
print(poly_v2)                      # represents polynomial corresponding to the second vector


# values corresponding to x = [1, 2, 3] from the result of polynomial multiplication
print([int(poly_prod(1)), int(poly_prod(2)), int(poly_prod(3)), int(poly_prod(4))])

# hadamard product of 2 vectors
print(y_prod)                     

