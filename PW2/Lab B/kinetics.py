"""
PW2 Lab B Part 3 -- fit a reaction's rate constant to measured data.

A first-order reaction decays as  C(t) = C0 * exp(-k*t).  You have noisy
concentration-vs-time measurements; find the k that best matches them.
Run:  python kinetics.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# TODO 1: read kinetics.csv (time, concentration) into arrays t, C; C0 = first value
data = np.loadtxt("kinetics.csv", delimiter=",", skiprows=1)
t = data[:, 0]         
C = data[:, 1]         
C0 = C[0]

# TODO 2: total_error(k) = sum of (measured - C0*exp(-k*t))^2
def total_error(k):
    model = C0 * np.exp(-k * t)
    return np.sum((C - model) ** 2)

# TODO 3: minimise with SLSQP, bounds [(0, 5)], start x0 = 0.5
result = minimize(total_error, x0=0.5, method="SLSQP", bounds=[(0, 5)])
k_fit = result.x[0]

print("C0 =", C0)
print("Fitted k =", k_fit)
print("Minimum error =", result.fun)

# TODO 4: plot data (points) and fitted curve (line), save as kinetics.png
t_smooth = np.linspace(t.min(), t.max(), 300)
plt.figure(figsize=(7, 5))
plt.scatter(t, C, label="measured data")
plt.plot(t_smooth, C0 * np.exp(-k_fit * t_smooth), color="red",
         label=f"fit: k = {k_fit:.3f}")
plt.xlabel("time")
plt.ylabel("concentration")
plt.title("First-order decay: fit of the rate constant")
plt.legend()
plt.grid(True)
plt.savefig("kinetics.png", dpi=150)
print("Saved kinetics.png")