# Solution to a CTF problem
import libnum
import matplotlib.pyplot as plt

def generate_points(mod):
    xs = []
    ys = []
    def y_squared(x):
        return (x**3 + 18*x + 9) % mod

    for x in range(0, mod):
        if libnum.has_sqrtmod_prime_power(y_squared(x), mod, 1):
            square_roots = libnum.sqrtmod_prime_power(y_squared(x), mod, 1)

        # we might have two solutions
            for sr in square_roots:
                ys.append(sr)
                xs.append(x)
    return xs, ys

# printing x-coordinates
xs, ys = generate_points(8011)
print(len(xs))
print(xs[7900], ys[7900])
print(xs[7899], ys[7899])
print(xs[7898], ys[7898])
print(xs[7897], ys[7897])
print(xs[7896], ys[7896])
# fig, (ax1) = plt.subplots(1, 1);
# fig.suptitle('y^2 = x^3 + 3 (mod p)');
# fig.set_size_inches(6, 6);
# ax1.set_xticks(range(0,11));
# ax1.set_yticks(range(0,11));
# plt.grid()
# plt.scatter(xs, ys, s=0.01)
# plt.show()