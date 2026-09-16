
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
