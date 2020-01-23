import numpy as np

L = 474.56e-6*np.pi
D1 = 2*np.pi*95e9 
wl = 1.55e-6
c = 3e8
D_wl = 100e-6 
neff = 2

b2 = 57.4e-27

D2 = (L/2/np.pi)*(wl**2/(2*np.pi*c))*D1**3*D_wl

D2 = c/neff*D1**2*b2

ng = c / L /D1
# D2_ref = (c/ng)*(wl**2/(2*np.pi*c))*D1**2*D_wl

print(D2)
# print(D2_ref)

R = 200e-6
FSR_w = c/(2*np.pi*R*neff)

# print(FSR_w)