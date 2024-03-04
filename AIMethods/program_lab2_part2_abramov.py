import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon, norm


def generate_and_plot(n):
    sample_means = []
    for _ in range(1000):
        sample = expon.rvs(size=n)
        sample_means.append(np.mean(sample))

    plt.hist(sample_means, bins=30, density=True, alpha=0.5, label='Гистограмма средних значений выборки')

    mu = expon.mean()
    sigma = np.sqrt(expon.var() / n)

    x = np.linspace(0, 3, 100)
    pdf = norm(loc=mu, scale=sigma).pdf(x)
    plt.plot(x, pdf, label='Теоретическая плотность распределения')
    plt.legend()
    plt.grid()
    plt.title(f'n = {n}')
    plt.show()


for n in [5, 10, 50]:
    generate_and_plot(n)