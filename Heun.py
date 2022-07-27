import numpy as np
import matplotlib.pylab as plt

def odeHeun(f, r0, t0, n, h):

	N_eq = len(r0)

	x = np.zeros(n, dtype=np.float32)
	y = np.zeros(n, dtype=np.float32)
	t = np.zeros(n, dtype=np.float32)

	x[0], y[0] = r0
	t[0] = t0

	for n in range(0, n-1):
		t[n+1] = t[n] + h
		K1x , K1y = f(t[n], x[n], y[n])
		K2x , K2y = f(t[n+1], x[n] + K1x*h, y[n] + K1y*h)
		x[n+1] = x[n] + 0.5*(K1x+K2x)*h
		y[n+1] = y[n] + 0.5*(K1y+K2y)*h

	return t, x, y 
