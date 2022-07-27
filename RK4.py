import numpy as np
import matplotlib.pylab as plt
	
def odeRK(f, r0, t0, n, h):

	N_eq = len(r0)

	r = np.zeros([n, N_eq], dtype = np.float32)

	t = np.zeros(n, dtype = np.float32)
	
	r[0] = r0
	
	t[0] = t0

	aux = 1/6

	for n in range(0, n-1):
	
		t[n+1] = t[n] + h
		
		K1 = f(t[n], r[n])
		
		K2 = f(t[n]+0.5*h, r[n] + 0.5*K1*h)
		
		K3 = f(t[n]+0.5*h, r[n] + 0.5*K2*h)

		K4 = f(t[n] + h, r[n] + K3*h)
		
		r[n+1] = r[n] + aux*(K1+2*K2+2*K3+K4)*h
				
	return t, r