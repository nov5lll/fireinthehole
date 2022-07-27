from Heun import *
import matplotlib.pylab as plt
# we need to define f, r0, t0, n, h, alpha, k, tol

def f(t,x,y):
    return np.array([x-x*y, -y+x*y])

r0 = (10, 10)

t0 = 0

n = 10000

h = 0.0001

t,x,y = odeHeun(f, r0, t0, n, h)

plt.plot(t, x)
plt.plot(t, y)
plt.show()