import numpy as np

L = 474.56e-6*np.pi
D1 = 95e9 
wl = 1.55e-6
c = 3e8
D_wl = 40e-6 
neff = 2

D2 = (L/2/np.pi)*(wl**2/(2*np.pi*c))*D1**3*D_wl

ng = 3e8 / L /D1
D2_ref = (c/ng)*(wl**2/(2*np.pi*c))*D1**2*D_wl

print(D2)
print(D2_ref)

