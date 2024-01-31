# Multiplying a vector by a scalar is homomorphic to multiplying the corresponding polynomial by the same scalar
import numpy as np 
from scipy.interpolate import lagrange

x = np.array([1,2,3,4])
y_v1 = np.array([0,8,6,12])         # vector y
y_scaled = 5 * y_v1                 # vector y scaled by 5

poly = lagrange(x,y_v1)
poly_scaled = 5 * poly

# verification
print(y_scaled)
print(int(poly_scaled(1)), int(poly_scaled(2)), int(poly_scaled(3)), int(poly_scaled(4)))