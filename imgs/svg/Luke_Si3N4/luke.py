import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.constants import c, pi
from scipy.misc import derivative
from math import sqrt
# from matplotlib import rcParams

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.constants import c, pi
from scipy.misc import derivative
from math import sqrt
# from matplotlib import rcParams

from cycler import cycler
plt.rcParams.update({    
    'font.size': 16,
#     'ytick.labelsize':14,
    'lines.linewidth': 0.8,
    'figure.max_open_warning': 0,
    'legend.frameon': False,
    'figure.subplot.hspace': 0,
    'savefig.dpi':300,
    'axes.labelsize': 16,
    'savefig.transparent': True,
    'axes.grid': True,
    'grid.linestyle': ':',
    'axes.prop_cycle': cycler('color', 'bgrcmyk')
#     'xtick.alignment': 'right'
})

# wl,nRaw = np.loadtxt('ellipso.txt').T
# nSq = nRaw**2

def sell(x, a, b, c):
    return 1+a*x**2/(x**2+b)+c*x # a unitless, b nm^2

# def sell(x, a, b):
#     return 1+a*x**2/(x**2+b) # a unitless, b nm^2
# popt, pcov = curve_fit(sell, wl, nSq)
# n = lambda x: sqrt(sell(x,*popt))

precision = 1e-1
wlRange = np.arange(1300,1700,precision)

def  Luke(x):
    return sqrt(1+(3.0249*x**2)/(x**2-135.3406**2)+(40314*x**2)/(x**2-1239842**2))
n_Luke = [Luke(i) for i in wlRange]
d2n_Luke = [derivative(Luke, i, dx=5e-3, n=2) for i in wlRange]
D_Luke = d2n_Luke*wlRange/c*(-1)*1e9

fig, (axn,axD) = plt.subplots(2,1,figsize=(7,5),sharex=True)
# axD = axn.twinx()

axn.plot(wlRange,n_Luke, 'r-', label='Luke 2015')
axD.plot(wlRange, D_Luke*1e6, 'b--',label=r'$D_{\lambda}$')


axD.set_xlabel(r'wavelength (nm)')
axD.set_ylabel(r'$D_M$ (ps/km·nm)')
axn.set_ylabel('refractive index')


pin = np.argmin(np.abs(wlRange-1550))
axD.scatter(wlRange[pin], D_Luke[pin]*1e6,color='blue')
axn.scatter(wlRange[pin], n_Luke[pin],color='red')

# axn.annotate(f'({wlRange[pin]:.0f}, {n_Luke[pin]:.4f})', xy = (wlRange[pin]-200,n_Luke[pin]))
# axD.annotate(f'({wlRange[pin]:.0f}, {D_Luke[pin]*1e6:.2f})', xy = (wlRange[pin]-200,D_Luke[pin]))

# axD.tick_params(axis='y', labelcolor='blue')
# axn.tick_params(axis='y', labelcolor='red')

plt.savefig('Luke_raw.svg', dpi = 300, transparent=True, bbox_inches='tight')