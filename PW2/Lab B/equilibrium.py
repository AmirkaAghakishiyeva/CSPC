"""
PW2 Lab B Part 4 -- chemical equilibrium via the equilibrium constant K.

Reaction  H2 + I2 <=> 2 HI, starting from 1 mol H2 and 1 mol I2.
As the reaction proceeds by an extent x:  H2 = 1-x,  I2 = 1-x,  HI = 2x.
At equilibrium the composition satisfies the equilibrium constant
        K = [HI]^2 / ([H2][I2]) = (2x)^2 / ((1-x)(1-x)).
Given K, find the extent x. Solve it TWO ways and compare.
Run:  python equilibrium.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 15.6
a = b = 1.0

# TODO 1: k_imbalance(x) = (2x)^2/((a-x)(b-x)) - K  (zero at equilibrium)
def k_imbalance(x):
    return (2 * x) ** 2 / ((a - x) * (b - x)) - K

# TODO 2 (method 1): Newton root-finding, start x0 = 0.5
x_newton = newton(k_imbalance, x0=0.5)

# TODO 3 (method 2): minimise k_imbalance(x)^2 with SLSQP
def squared_imbalance(x):
    return k_imbalance(x[0]) ** 2      # minimize passes x as an array

res = minimize(squared_imbalance, x0=[0.5], method="SLSQP",
               bounds=[(0, 0.999)])
x_slsqp = res.x[0]

print("Newton x =", x_newton)
print("SLSQP  x =", x_slsqp)
print("Difference =", abs(x_newton - x_slsqp))

# TODO 4: equilibrium amounts and plot
x_eq = x_newton
n_H2 = a - x_eq
n_I2 = b - x_eq
n_HI = 2 * x_eq
print(f"\nEquilibrium amounts (mol): H2 = {n_H2:.4f}, "
      f"I2 = {n_I2:.4f}, HI = {n_HI:.4f}")
print("Check K =", n_HI**2 / (n_H2 * n_I2))

x_grid = np.linspace(0, 1, 300)
plt.figure(figsize=(7, 5))
plt.plot(x_grid, a - x_grid, label="H2", linewidth=3)
plt.plot(x_grid, b - x_grid, "--", label="I2", color="orange")
plt.plot(x_grid, 2 * x_grid, label="HI", color="green")
plt.axvline(x_eq, color="red", linestyle=":",
            label=f"equilibrium x = {x_eq:.3f}")
plt.scatter([x_eq, x_eq, x_eq], [n_H2, n_I2, n_HI], color="red", zorder=5)
plt.xlabel("extent of reaction x")
plt.ylabel("amount (mol)")
plt.title("H2 + I2 <=> 2 HI: amounts vs extent")
plt.legend()
plt.grid(True)
plt.savefig("equilibrium.png", dpi=150)
print("Saved equilibrium.png")