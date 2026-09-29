"""
PW2 Lab A -- Motion from tracking data.

Read noisy free-fall position measurements, then:
  - differentiate once  -> velocity
  - differentiate twice -> acceleration (should be ~ constant -g, but noisy!)
  - integrate the acceleration back up -> recover velocity and position

Complete the TODOs. Run:  python analysis.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# TODO 1: read freefall.csv into arrays t and y
#         (hint: np.loadtxt with a comma delimiter, skipping the header)
data = np.loadtxt("freefall.csv", delimiter=",", skiprows=1)
t = data[:, 0]   
y = data[:, 1]   
# TODO 2: compute velocity v = derivative of y w.r.t. t   (np.gradient)
#         and acceleration a = derivative of v w.r.t. t    (np.gradient again)
#         Print the mean acceleration. Is it close to -9.81? Is it noisy?
v = np.gradient(y, t)  
a = np.gradient(v, t)  
print("Mean acceleration:", a.mean())

# TODO 3: integrate a back up to recover velocity and position
#         (hint: cumulative_trapezoid(a, t, initial=0) + v[0], then again)
v_rec = cumulative_trapezoid(a, t, initial=0) + v[0]
y_rec = cumulative_trapezoid(v_rec, t, initial=0) + y[0]

print("Max difference in position:", np.max(np.abs(y_rec - y)))
# TODO 4: make a figure with 3 stacked panels: position, velocity, acceleration
#         vs time. Mark the true -9.81 line on the acceleration panel.
#         Save it as motion.png
fig, axs = plt.subplots(3, 1, sharex=True, figsize=(8, 9))

axs[0].plot(t, y)
axs[0].set_ylabel("Position y (m)")

axs[1].plot(t, v)
axs[1].set_ylabel("Velocity v (m/s)")

axs[2].plot(t, a)
axs[2].axhline(-9.81, color="red", linestyle="--", label="-9.81 m/s²")
axs[2].set_ylabel("Acceleration a (m/s²)")
axs[2].set_xlabel("Time t (s)")
axs[2].legend()

fig.tight_layout()
fig.savefig("motion.png", dpi=150)
print("std of a:", a.std())
print("mean without edges:", a[1:-1].mean())
print("time step:", t[1] - t[0])
print("g from quadratic fit:", -2 * np.polyfit(t, y, 2)[0])