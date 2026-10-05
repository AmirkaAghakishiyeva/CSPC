"""
PW2 Lab B Part 5 (bonus) -- find a titration's equivalence point.

titration.csv holds a titration curve: pH versus the volume of base added.
The equivalence point is the volume where the pH changes fastest (the steep
jump). Numerically, that is where the SLOPE of the pH curve is largest.
Run:  python titration.py
"""
import numpy as np
import matplotlib.pyplot as plt

# TODO 1: read titration.csv (volume_base, pH) into arrays V, pH
data = np.loadtxt("titration.csv", delimiter=",", skiprows=1)
V = data[:, 0]          # volume of base added (mL)
pH = data[:, 1]         # measured pH

# TODO 2: slope of the pH curve and the volume where it is largest
slope = np.gradient(pH, V)       # d(pH)/dV at every point
i_max = np.argmax(slope)         # index of the largest slope
V_eq = V[i_max]

print("Equivalence point volume =", V_eq, "mL")
print("pH at equivalence point  =", pH[i_max])
print("Maximum slope            =", slope[i_max], "pH/mL")

# TODO 3: two plots side by side, save as titration.png
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5))

ax1.plot(V, pH, color="blue")
ax1.axvline(V_eq, color="red", linestyle="--",
            label=f"equivalence point = {V_eq:.1f} mL")
ax1.set_xlabel("volume of base (mL)")
ax1.set_ylabel("pH")
ax1.set_title("Titration curve")
ax1.legend()
ax1.grid(True)

ax2.plot(V, slope, color="green")
ax2.axvline(V_eq, color="red", linestyle="--",
            label=f"peak at {V_eq:.1f} mL")
ax2.set_xlabel("volume of base (mL)")
ax2.set_ylabel("slope d(pH)/dV (pH per mL)")
ax2.set_title("Slope of the pH curve")
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.savefig("titration.png", dpi=150)
print("Saved titration.png")