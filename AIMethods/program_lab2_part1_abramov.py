import numpy as np
from scipy.optimize import minimize, differential_evolution


def f(x):
    return np.sin(x / 5) * np.exp(x / 10) + 5 * np.exp(-x / 2)


result_2 = minimize(f, 2, method='BFGS')
answer_1 = round(result_2.fun, 2)

result_30 = minimize(f, 30, method='BFGS')
answer_2 = round(result_30.fun, 2)

with open('submission-1.txt', 'w') as file:
    file.write(f"{answer_1} {answer_2}")
# ----------------------------------------------------------------------------------------------------------------------
bounds = [(1, 30)]
result = differential_evolution(f, bounds)
answer = round(result.fun, 2)

with open('submission-2.txt', 'w') as file:
    file.write(str(answer))


# ----------------------------------------------------------------------------------------------------------------------
def h(x):
    return f(x).astype(int)


result_bfgs = minimize(h, 30, method='BFGS')
answer_1 = round(result_bfgs.fun, 2)

bounds = [(1, 30)]

result_de = differential_evolution(h, bounds)
answer_2 = round(result_de.fun, 2)

with open('submission-3.txt', 'w') as file:
    file.write(f"{answer_1} {answer_2}")
