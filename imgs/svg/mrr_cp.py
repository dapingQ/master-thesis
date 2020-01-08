import numpy as np
import matplotlib.pyplot as plt
plt.style.use('classic')
a = .9
r = .9

def trans(x, a, r):
    return (a**2-2*a*r*np.cos(x)+r**2)/(1-2*a*r*np.cos(x)+a**2*r**2)

x = np.linspace(-3*np.pi, 3*np.pi, 500)
aList = [0.9, 0.5]
rList = [0.9, 0.8]

linestyles = ['-', '--', '-.', ':']
fig, ax = plt.subplots(figsize=(6,3))
for a in aList:
    for r in rList:
        ax.plot(x, trans(x, a, r), label=f'$a$={a}'+ r' $\tau$'+f'={r}')
ax.legend(fancybox = True, bbox_to_anchor=(1.1, 0.5, 0.3, 0.5), fontsize=10)  
# ax.legend( fontsize=8,loc=0)  


# ax.set_xticks((-np.pi,0,np.pi))
# ax.set_xticklabels(('$\pi$', r'$0$', '$\pi$'), color='k', size=20)
# ax.axis('off')
ax.set_ylim(ymin=0,ymax=1)
ax.set_xlim(xmin=x.min(),xmax=x.max())

ax.set_yticks((0,1))
# fig.tight_layout()

ax.set_xticks(np.linspace(-3*np.pi, 3*np.pi, 7) )

ax.set_xticklabels(( f'{i:.0f}'+r'$\pi$' for i in np.linspace(-3, 3, 7)   ))

ax.set_xlabel(r'$\phi$')
ax.set_ylabel(r'$T$')
fig.savefig('svg\mrr_cp.svg', transparent = True,
    # bbox_inches="tight"
    )
