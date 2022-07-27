import numpy as np
import matplotlib.pylab as plt

def odeRKF(f, r0, t0, n, h, alpha, k, tol):

	N_eq = len(r0)

	r = np.zeros([n, N_eq], dtype = np.float64)

	t = np.zeros(n, dtype = np.float64)
	
	r[0]  = r0

	t[0]  = t0

	# Coeficientes auxiliares 1

	a1 = 16/135

	a2 = 6656/12825

	a3 = 28561/56430

	a4 = -9/50

	a5 = 2/55

	# Coeficientes auxiliares 2 Para 4 ordem

	a12 = 25/216

	a22 = 1408/2565

	a32 = 2197/4104

	a42 = -1/5

	q = np.zeros(n, dtype = np.float64)

	for n in range(0, n-1):

		while(True):

			# Calculo dos K
			
			K1 = f(t[n], r[n])
				
			K2 = f(t[n]+h/4, r[n] + K1*h/4)
				
			K3 = f(t[n]+3*h/8, r[n] + ((3*K1+9*K2)/32)*h)

			K4 = f(t[n] + 12*h/13, r[n] + ((1932*K1-7200*K2+7296*K3)/2197)*h)
				
			K5 = f(t[n] + h, r[n] + (439*K1/216-8*K2+3680*K3/513-845*K4/4104)*h)

			K6 = f(t[n] + h, r[n] + (-8*K1/27+2*K2-3544*K3/2565+1859*K4/4104-11*K5/10)*h)

			# Para quarta ordem e quinta

			y4 = r[n] + (a12*K1+a22*K3+a32*K4+a42*K5)*h

			y5 = r[n] + (a1*K1+a2*K3+a3*K4+a4*K5+a5*K6)*h

			q = min(alpha*(((tol*h)/(abs(y4-y5)))**(1/k)))

			#q = min(alpha*((tol*h)/(abs(y4-y5))**(1/k)))

			print(q)

			if(q >= 1):

				break
			
			else:

				h = q*h

		t[n+1] = t[n] + h	

		r[n+1] = y5	
		
		h = q*h

	return t, r, q
