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

ni = 2.029 # inner index
no = 1.48 # outer index
wl = 1.55
step = 1e-2 # pm
wl_list = [wl-step,wl,wl+step]

w = np.arange(0.6,2.4,0.01)
t = np.arange(0.6,1.0,0.01)

filename = f'ni_{ni}_no_{no}_cwl_{wl}_w_{w[0]:.2F}_{w[-1]:.2F}_step{w[1]-w[0]:.2F}_t_{t[0]:.2F}_{t[-1]:.2F}_step{t[1]-t[0]:.2F}.txt'

d_array = np.loadtxt(filename)
X, Y = np.meshgrid(w,t)
fig, ax = plt.subplots(dpi=200,figsize=(6,3))
im = ax.imshow(d_array, interpolation='bilinear', origin='lower',
                cmap=cm.rainbow,extent=(w[0],w[-1],t[0],t[-1]),aspect='auto')

cs = ax.contour(d_array, np.arange(-400,400,100),
                origin='lower',#cmap='flag',
                colors='k',extent=(w[0],w[-1],t[0],t[-1]))

sizex, sizey = 1.5, 0.8
mark = True
if mark:
#     ax.hlines(xmin=w[0],xmax=sizex,y=sizey, ls='--', alpha=0.5)
#     ax.vlines(ymax=sizey,ymin=t[0],x=sizex, ls='--', alpha=0.5)
    ax.plot(sizex,sizey,'o',color='black')

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
fig.savefig(f'..\{wl*1e3:.0F}_{mark}.svg',dpi=200,transparent=True,bbox_inches='tight')
# ax.set_title(r'$D_{W}$ at ' + f'{wl*1e3:.0F} nm (ps/nm·km)')
# fig.savefig(f'{wl*1e3:.0F}_{mark}_title.svg',dpi=200,transparent=True,bbox_inches='tight')
