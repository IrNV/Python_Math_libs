from scipy import optimize
import numpy as np


# Rosenbrock function
def f(x):
    return .5*(1 - x[0]) ** 2 + (x[1] - x[0] ** 2) ** 2


# function gradient
def grad_f(x):
    return np.array((-2 * .5 * (1 - x[0]) - 4 * x[0] * (x[1] - x[0] ** 2),
                     2 * (x[1] - x[0] ** 2)))

# finding minimum
result = optimize.brute(f, ((-5, 5), (-5, 5)))
print(result)

result = optimize.minimize(f, [2, 2])
print(result)

check = optimize.check_grad(f, grad_f, [2, 2])
print("Deviation gradient:", check)

result = optimize.fmin_bfgs(f, [2, 2], fprime=grad_f)
print(result)
