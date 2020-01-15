import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from scipy.optimize import fsolve
from scipy.constants import c

plt.rcParams.update({    
    'font.size': 12,
    'lines.linewidth': 0.8,
    'figure.max_open_warning': 0,
    'savefig.dpi':300,
    'savefig.transparent': True,
})

w = np.arange(0.5,2.4,0.1)
t = np.arange(0.5,1.0,0.1)

data = np.loadtxt('20013-test_disp.txt')#[:int(len(w)*len(t)*3)]
d_array = data.reshape((len(w),len(t),4))[:,:,1]*1e6

X, Y = np.meshgrid(w,t)
fig, ax = plt.subplots(dpi=200,figsize=(6,3))
im = ax.imshow(d_array, interpolation='bilinear', origin='lower',
                cmap=cm.rainbow,extent=(w[0],w[-1],t[0],t[-1]),aspect='auto')

cs = ax.contour(d_array, (-300,-100,0,50,100,150),
                origin='lower',#cmap='flag',
                colors='k',extent=(w[0],w[-1],t[0],t[-1]))

sizex, sizey = 1.5, 0.8
mark = True
if mark:
#     ax.hlines(xmin=w[0],xmax=sizex,y=sizey, ls='--', alpha=0.5)
#     ax.vlines(ymax=sizey,ymin=t[0],x=sizex, ls='--', alpha=0.5)
    ax.plot(sizex,sizey,'.',color='black',)

# cs.levels = [nf(val) for val in cs.levels]

# plt.setp(cs.collections[1], linewidth=2)

if plt.rcParams["text.usetex"]:
    fmt = r'%.0f'
else:
    fmt = ' %.0f '
ax.clabel(cs, cs.levels, fmt=fmt,inline=1, fontsize=10)
cbar = fig.colorbar(im, ax=ax)
cbar.ax.set_ylabel(r'$D_{W}$ (ps/nm·km)')

ax.set_xlabel('width ($\mathrm{\mu}$m)')
ax.set_ylabel(r'thickness ($\mathrm{\mu}$m)')

# plt.show()
fig.savefig(f'fdtd_fine.svg',dpi=200,transparent=True,bbox_inches='tight')
