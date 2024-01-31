# R1CS: Multiplication with a constant -> out = 2x*x + y -> out-y = 2x*x
import numpy as np
import random

A = np.array([[0,0,2,0]])
B = np.array([[0,0,1,0]])
C = np.array([[0,1,0,-1]])

# Generate random numbers
x = np.random.randint(1,1000)
y = np.random.randint(1,1000)

out = 2*pow(x,2) + y
print(f"out = {out}")

# Witness
witness = np.array([1,out,x,y])
print(f"witness is : {witness}")
print(f"A.dot(witness): {A.dot(witness)}")
print(f"B.dot(witness): {B.dot(witness)}")
print(f"C.dot(witness): {C.dot(witness)}")
result = C.dot(witness) == np.multiply(A.dot(witness), B.dot(witness))
assert result.all(), "System contains inequality"
