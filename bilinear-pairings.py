from py_ecc.bn128 import neg, G1, G2, pairing, add, multiply, eq

# ab + cd = 0
a = 4
b = 3
c = 6
d = 2

# structuring output
(aG1_x, ag1_y) = neg(multiply(G1,a))
(bG2_x1, bG2_y1) = multiply(G2,b)[0]
(bG2_x2, bG2_y2) = multiply(G2,b)[1]
(cG1_x, cG2_y) = multiply(G1,c)
(dG2_x1, dG2_y1) = multiply(G2,d)[0]
(dG2_x2, dG2_y2) = multiply(G2,d)[1]

# Asserting: 
