'''
R1CS: out = 3*x*x*y + 5*x*y - x - 2*y + 3
Transformed -> 
v1 = x*y
v2 = 3v1 * x
out - 3 + x + 2*y - 5*v1 = 3 * v2
'''

import numpy as np 
import random

A = np.array([[0,0,1,0,0,0],
              [0,0,0,0,3,0],
              [3,0,0,0,0,0]])

B = np.array([[0,0,0,1,0,0],
              [0,0,1,0,0,0],
              [0,0,0,0,0,1]])

C = np.array([[0,0,0,0,1,0],
              [0,0,0,0,0,1],
              [-3,1,1,2,-5,0]])


# Generate x,y to test
x = np.random.randint(1,1000)
y = np.random.randint(1,1000)

v1 = x * y
v2 = 3 * v1 * x
out = 3 - x - 2*y +  5*v1 + 3*v2

# witness
witness = np.array([1, out, x, y, v1, v2])

# verify: Cw = Aw * Bw
result = C.dot(witness) == np.multiply(A.dot(witness), B.dot(witness))
assert result.all(), "system contains inequalities"
