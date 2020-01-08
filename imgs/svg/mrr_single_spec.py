import numpy as np
import matplotlib.pyplot as plt
# plt.style.use('fast')
a = .9
r = .9

def trans(x, a, r):
    return (a**2-2*a*r*np.cos(x)+r**2)/(1-2*a*r*np.cos(x)+a**2*r**2)

x = np.linspace(-np.pi, 3*np.pi, 500)
aList = [0.9, 0.5]
rList = [0.9, 0.8]

linestyles = ['-', '--', '-.', ':']
fig, ax = plt.subplots(figsize=(6,3))

ax.plot(x, trans(x, .8, .9), color='black', lw=1)
ax.vlines(ymax=1,ymin=0,x=0,lw=1,ls=':')
ax.vlines(ymax=1,ymin=0,x=2*np.pi,lw=1,ls=':')
ax.set_ylim(ymin=0,ymax=1)
ax.set_yticks((0,1))
ax.set_xticks((0,2*np.pi))

ax.set_xticklabels((r'$\lambda_{\mu}$',r'$\lambda_{\mu+1}$'))


# fig.tight_layout()
fig.savefig('mrr_fsr.svg', transparent = True, bbox_inches="tight")
