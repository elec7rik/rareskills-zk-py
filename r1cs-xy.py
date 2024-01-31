# R1CS: Handling simple multiplication: out=x*y

import numpy as np

# define the matrices
C = np.array([[0,1,0,0]])
A = np.array([[0,0,1,0]])
B = np.array([[0,0,0,1]])

witness = [1, 4223, 41, 103]

# Cw = Aw*Bw
result = C.dot(witness) == A.dot(witness) * B.dot(witness)

# check all element-wise equality is True
assert result.all(), "result contains an inequality"
