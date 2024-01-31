import numpy as np
import random

'''
Transforming {out=x*y*w*u}
v1 = x * y
v2 = w * u
out = v1 * v2

3 equations -> 3 rows , 8 columns

witness -> 1 row , 8 columns = [1, out, x, y, x, u, v1, v2]

Construct matrix A from left hand terms(x, w, v1).
Construct matrix B from right hand terms(y, u, v2).
Construct matrix C from output terms(v1, v2, out).

'''

A = np.array([[0,0,1,0,0,0,0,0],
              [0,0,0,0,1,0,0,0],
              [0,0,0,0,0,0,1,0]])

B = np.array([[0,0,0,1,0,0,0,0],
              [0,0,0,0,0,1,0,0],
              [0,0,0,0,0,0,0,1]])

C = np.array([[0,0,0,0,0,0,1,0],
              [0,0,0,0,0,0,0,1],
              [0,1,0,0,0,0,0,0]])


# random x, y, z, w values
x = random.randint(1,1000)
y = random.randint(1,1000)
z = random.randint(1,1000)
w = random.randint(1,1000)

# computing the algebraic circuit
out = x * y * z * w
v1 = x * y
v2 = z * w

witness = np.array([1, out, x, y, z, w, v1, v2])

# element-wise multiplication
result = C.dot(witness) == np.multiply(A.dot(witness), B.dot(witness))

assert result.all(), "system contains an inequality"