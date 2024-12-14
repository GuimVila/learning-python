import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

# Configurar subplots (4 files x 4 columnes, per a 16 distribucions)
fig, axes = plt.subplots(4, 4, figsize=(20, 16))  # 4x4 graella de subgràfiques

# Llista de distribucions amb configuració i títols
distributions = [
    ("Normal", random.normal(loc=50, scale=5, size=1000)),
    ("Binomial", random.binomial(n=100, p=0.5, size=1000)),
    ("Poisson", random.poisson(lam=3, size=1000)),
    ("Uniform", random.uniform(low=0, high=100, size=1000)),
    ("Exponential", random.exponential(scale=2, size=1000)),
    ("Gamma", random.gamma(shape=2, scale=2, size=1000)),
    ("Chi-Square", random.chisquare(df=2, size=1000)),
    ("Rayleigh", random.rayleigh(scale=2, size=1000)),
    ("Pareto", random.pareto(a=3, size=1000)),
    ("Logistic", random.logistic(loc=50, scale=5, size=1000)),
    ("Multinomial", random.multinomial(n=10, pvals=[0.2, 0.3, 0.5], size=1000)[:, 0]),
    ("Zeta", random.zipf(a=2, size=1000)),
    ("Beta", random.beta(a=2, b=5, size=1000)),
    ("Triangular", random.triangular(left=10, mode=20, right=30, size=1000)),
    ("Weibull", random.weibull(a=1.5, size=1000)),
    ("Lognormal", random.lognormal(mean=0, sigma=1, size=1000)),
]

# Iterar sobre cada distribució i subgràfica
for ax, (title, data) in zip(axes.flatten(), distributions):
    sns.histplot(data, kde=True, ax=ax)
    ax.set_title(title)

# Ajustar espais entre subgràfiques
plt.tight_layout()
plt.show()
