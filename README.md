
# CSPC Lab A

## PW1 — Lab A

## 1. Environment
First, I created a Conda environment called `cspc` using the provided `environment.yml` file. I used Python 3.11 and installed NumPy and pytest.I also created a `.gitignore` file in the root of the `CSPC` repository and added:
__pycache__/
*.pyc
This prevents Python cache files and compiled files from being added to Git.
## 2. Radioactive decay simulation
I worked with two versions of the simulation in `decay.py`:
`simulate_loop()` — a pure Python version that checks every atom one by one.
`simulate()` — a NumPy version that uses vectorised operations.
### 3. Tests
I added two more tests to `test_decay_STUDENT.py`.The first test checks that the program raises a `ValueError` when a negative decay rate is given.The second test runs the simulation many times with different seeds, calculates the average result, and compares it with the analytical radioactive decay law.
After adding the tests, I ran it
All three tests passed:
3 passed in 0.09s
## 4. Git
I created the Git repository and made commits for my work. I also created a separate branch for the README, merged it into `main`, and deleted the branch afterwards.
## 5. Performance comparison
I created `speed.py` to compare the performance of `simulate_loop()` and `simulate()`.
My result was:
simulate_loop: 2.2008 seconds
simulate:      0.0002 seconds
Speed-up:       12872.26x
The NumPy version was much faster because it does not loop through every atom in Python.
## Conclusion
In this lab, I learned how to create and use a Conda environment, work with NumPy, write tests with pytest, use Git and GitHub, and compare the performance of two different implementations and also saw in practice how vectorised NumPy operations can make a big difference in performance compared with a pure Python loop.




---

## PW1 — Lab B: Data, Plotting, and Automation

**What I built:**

- I worked with the observed radioactive decay data from `decay_observed.csv` and used NumPy to read the data and build the analytical decay curve.
- I created `plot.py` to show the observed data and the analytical law in two side-by-side plots, and created a `Snakefile` to automate the generation of `figure.png`.

**Result:**

- The observed count decreased over time and showed an approximately exponential decay pattern.
- The observed data matched the analytical decay law reasonably well, although the points did not match the curve exactly.

**Snakemake:**

- The Snakemake pipeline uses `decay_observed.csv` as input and runs `plot.py` to create `figure.png`.
- It rebuilds the figure when the input or code changes and does nothing when everything is already up to date.

**Conclusion:**

- I learned how to work with real observation data and compare it with an analytical model using NumPy and Matplotlib.
- I also learned how Snakemake can automate a simple data analysis workflow and avoid running steps that do not need to be repeated.




---

## PW2 --- Lab A: Motion from Tracking Data

**Data.** `freefall.csv` contains the measured height (m) of an object dropped from about 500 m, sampled every 0.1 s. Velocity and acceleration were computed with `np.gradient` (once and twice), and then integrated back with `cumulative_trapezoid`.

**Measured mean acceleration.** The mean acceleration was −8.58 m/s², somewhat different from the expected −9.81 m/s². The mean of a double derivative depends mostly on the noisy values at the ends of the record. A quadratic fit to the whole position curve gives g ≈ 9.80 m/s², so the data are consistent with free fall.

**Why the acceleration is noisy.** The acceleration is much noisier than the position because each derivative divides the difference of neighbouring noisy values by the small time step (0.1 s), so differentiating twice amplifies the noise by a large factor, while the true signal (a constant −9.81 m/s²) stays the same. The standard deviation of the acceleration was 28.7 m/s².

**What integrating back showed.** Integrating the noisy acceleration twice recovered the position to within 0.78 m of the original (over a ~500 m drop), because integration is a sum in which random noise largely cancels, the opposite of differentiation, which amplifies it.

**Figure.** `PW2/Lab A/motion.png` shows three stacked panels sharing the time axis: a smooth position, a slightly rough velocity, and a very noisy acceleration around the dashed −9.81 m/s² line.





## PW2 --- Lab B

### Part 2: comparing the three methods

**2A: f(x) = (x-3)^2 + 1.** This one was easy. Gradient descent, Newton and
SLSQP all ended up at x ≈ 3 (f ≈ 1), so I couldn't see any real difference
between them.

**2B: g(x) = x^4 - 3x^2 + x + 5.** Here the methods did not agree.
- Starting from x0 = 0, gradient descent and SLSQP went to the global minimum
  at x ≈ -1.30 (g ≈ 1.486). Newton, however, stopped at x ≈ 0.17. I checked
  g'' there and it is negative, so that point is a maximum, not a minimum.
- Starting from x0 = 2, Newton found the local minimum at x ≈ 1.13
  (g'' > 0, g ≈ 3.93). Gradient descent and SLSQP still went to the global
  minimum at x ≈ -1.30.

What I learned: Newton's method only solves g'(x) = 0, so it can stop at any
stationary point, and I have to look at the sign of g'' to know whether it is
a minimum or a maximum. The starting point also decides which stationary
point we reach. So on a complicated function both the algorithm and the
starting point matter.

### Part 3: fitting the reaction rate

I fitted the first-order model C(t) = C0 * exp(-k t) to the data, with C0 =
104.08 (the first measurement). The fitted rate constant is k ≈ 0.262, with a
minimum squared error of about 266. This is close to the expected value of
0.25; the small difference is probably due to the noise in the measurements
(including the noise in C0). The fitted curve goes through the data points
(kinetics.png).

### Part 4: chemical equilibrium

For H2 + I2 <=> 2 HI with K = 15.6, starting from 1 mol of each reactant, I
solved for the extent x in two ways. Newton's root-finding gave x = 0.66385
and SLSQP (minimising k_imbalance^2) gave x = 0.66385 as well; they differ
only by about 2e-7, so the two methods agree.

At equilibrium: H2 = 0.336 mol, I2 = 0.336 mol, HI = 1.328 mol. To check, I
put these amounts back into the formula and got K = 15.6 again
(equilibrium.png).

### Part 5 (bonus): titration equivalence point

I computed the slope of the pH curve with np.gradient and looked for its
maximum. The slope peaks at 4.0 pH/mL at V = 50.0 mL, where pH = 7.0, so the
equivalence point is at 50.0 mL (titration.png).
