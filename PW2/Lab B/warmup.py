"""
PW2 Lab B Part 2 -- three routes to a minimum.

Compare gradient descent, Newton, and SLSQP on two functions:
  2A: f(x) = (x-3)**2 + 1          (easy, one minimum at x=3)
  2B: g(x) = x**4 - 3*x**2 + x + 5 (harder, several stationary points)
Run:  python warmup.py
"""
import numpy as np
from scipy.optimize import newton, minimize


# ---------- 2A: easy convex function ----------
def f(x):   return (x-3)**2 + 1
def df(x):  return 2*(x-3)
def d2f(x): return 2.0

x0 = 0


x = x0
lr = 0.1
for i in range(10000):
    x_new = x - lr * df(x)
    if abs(x_new - x) < 1e-8:
        x = x_new
        break
    x = x_new

print("2A Gradient Descent:")
print("x =", x)
print("f(x) =", f(x))

x_newton = newton(df, x0, fprime=d2f)

print("2A Newton:")
print("x =", x_newton)
print("f(x) =", f(x_newton))


result = minimize(f, x0, method="SLSQP")

print("2A SLSQP:")
print("x =", result.x[0])
print("f(x) =", result.fun)


# ---------- 2B: harder landscape ----------
def g(x):   return x**4 - 3*x**2 + x + 5
def dg(x):  return 4*x**3 - 6*x + 1
def d2g(x): return 12*x**2 - 6


def run_all(x0):
    print(f"\n===== 2B, start x0 = {x0} =====")

    # (1) Gradient descent
    x = x0
    lr = 0.1
    for i in range(10000):
        x_new = x - lr * dg(x)
        if abs(x_new - x) < 1e-8:
            x = x_new
            break
        x = x_new
    print("Gradient descent: x =", x, " g(x) =", g(x))

    # (2) Newton (solves dg(x) = 0) + sign check of d2g
    xn = newton(dg, x0, fprime=d2g)
    kind = "MINIMUM" if d2g(xn) > 0 else "MAXIMUM"
    print("Newton:           x =", xn, " g(x) =", g(xn))
    print("   d2g =", d2g(xn), "->", kind)

    # (3) SLSQP
    r = minimize(g, x0, method="SLSQP")
    print("SLSQP:            x =", r.x[0], " g(x) =", r.fun)


run_all(0)
run_all(2)