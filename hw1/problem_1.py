import numpy as np
import matplotlib.pyplot as plt

# values found by the Galerkin projection method
a1 = -307/1466
a2 = -60/733

# part 1
def u_tilde(x):
    return (a1 + a2 * x) * (x**2 - x)

x_data = np.linspace(0, 1, 100)
y_data_1 = u_tilde(x_data)
plt.figure()
plt.plot(x_data, y_data_1)
plt.xlabel(r"x")
plt.ylabel(r"$\tilde{u}(x; a)$")
plt.savefig("problem_1_u_tilde.png")

# part 3
def residual(x):
    return 2 * a1 * x + a1 + 3 * a2 * x**2 + 4 * a2 * x - 2 * a2 + x

y_data_3 = residual(x_data)
plt.figure()
plt.plot(x_data, y_data_3)
plt.xlabel(r"x")
plt.ylabel(r"$R(x)$")
plt.savefig("problem_1_residual.png")

# part 4
