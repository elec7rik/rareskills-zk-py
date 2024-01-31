field_size = 29
def compute_inv(a):
    return pow(a, -1, field_size)

a = 22
b = compute_inv(a)

assert((a*b)%field_size == 1)

