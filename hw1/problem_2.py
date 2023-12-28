import numpy as np
import matplotlib.pyplot as plt

# values found by the Residual Least Squares Method with different values of lambda
lambda_vals = [1, 100, 1000]

# approximate values found by finding loss function-minimizing values of a1 and a2 for different values of lambda
a1_vals = [-0.2095, -0.2128, -0.2146]
a2_vals = [-0.0818, -0.0809, -0.0804]

# part 1
def u_tilde(x, a1, a2):
    return (a1 + a2 * x) * (x**2 - x)

# part 3
def residual(x, a1, a2):
    return 2 * a1 * x + a1 + 3 * a2 * x**2 + 4 * a2 * x - 2 * a2 + x

def analytical_solution(x):
    return - (x**2 / 2) + x + 1 / (2 * (1 - np.exp(-1))) * (np.exp(-x) - 1)

x_data = np.linspace(0, 1, 100)

# plotting
plt.figure()

# plot the data points we are given as "measured"
plt.plot(0.5, 0.06377, marker="o", markersize=2, color="black", label="Given measurement: (0.5, 0.06377)")

# plot solution u_tilde as a function fo x for all values of lambda
for i, _ in enumerate(lambda_vals):
    plt.plot(x_data, u_tilde(x_data, a1_vals[i], a2_vals[i]), alpha=0.5, linewidth=0.7, linestyle="dashed", label=rf"$\lambda = {lambda_vals[i]}, a_1 \approx {a1_vals[i]}, a_2 \approx {a2_vals[i]}$")
    plt.xlabel(r"x")
    # plt.ylabel(r"$\tilde{u}(x; a)$")

# plot analytical solution
plt.plot(x_data, analytical_solution(x_data), label="Analytical Solution", alpha=0.5, linewidth=0.7)


plt.legend(fontsize=7)
plt.savefig("problem_2_u_tilde_different_lambdas.png", dpi=300)

"""
Discussion of results (part 3)
We find that a higher value of lambda is associated with a function approximation that better-fits the given data point. This makes intutive sense, as it increases the amount of loss associated with a difference between the function approximation and the given measurement. The highest value of lambda also closely matches the analytical solution, which demonstrates the importance of checking multiple values of lambda and comparing against a known analytical solution (if available).
"""


# part 4
def residual(x, a1, a2):
    return 2 * a1 * x + a1 + 3 * a2 * x**2 + 4 * a2 * x - 2 * a2 + x

# add values to lists that weren't used in part 3
lambda_vals.insert(0, 0)
a1_vals.insert(0, -307/1466)
a2_vals.insert(0, -60/733)

plt.figure()
plt.axvline(x=0.5, label="Given measurement: x=0.5", color="black")

for i, _ in enumerate(lambda_vals):
    plt.plot(x_data, residual(x_data, a1_vals[i], a2_vals[i]), alpha=0.5, linewidth=0.7, linestyle="dashed", label=rf"$\lambda = {lambda_vals[i]}, a_1 \approx {round(a1_vals[i], 4)}, a_2 \approx {round(a2_vals[i], 4)}$")
    plt.xlabel(r"x")
    plt.ylabel(r"$R(x; a_1, a_2)$")

plt.legend(fontsize=7)
plt.savefig("problem_2_residual_different_lambdas.png", dpi=300)



"""
Discussion of results (part 4)

The higher values of lambda demonstrate lower values in the magnitude of the residual as the approximate function is nearer the given data point. However, they have larger residuals further away from the given measurement compared to the lower values of lambda, and given enough data points, a higher value of lambda may overfit, so a careful study of bias, variance, and generalization to unseen data points should be conducted to properly trade off between these factors given requirements of a particular project.

"""
