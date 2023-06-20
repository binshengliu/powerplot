import matplotlib.ticker as plticker
import numpy as np
import seaborn as sns
from statsmodels.stats.power import TTestPower

sns.set_theme("paper", "darkgrid", font="Linux Biolinum O")
power = TTestPower()
fig = power.plot_power(
    dep_var="nobs",
    effect_size=[0.05, 0.1, 0.15, 0.2],
    nobs=np.arange(100, 1101, 50),
    alpha=0.05,
)
fig.axes[0].xaxis.set_major_locator(plticker.MultipleLocator(base=50))
fig.axes[0].yaxis.set_major_locator(plticker.MultipleLocator(base=0.1))
fig.axes[0].axhline(y=0.8)
fig.savefig("power.png", dpi=600)
