from Heun import *
from RKF45 import *
from RK4 import *
import matplotlib.pylab as plt
# we need to define f, r0, t0, n, h, alpha, k, tol


# Here we'll define the ODE
def f(t, r):
    x, y = r

    return np.array([x-x*y, -y+x*y])


# Here we need to define the constants, where

# the initial position
r0 = (10, 10)

# First step of time
t0 = 0

# Number of steps
n = 3000

# lenght of the step
h = 0.001

#t,x,y = odeHeun(f, r0, t0, n, h)

#t,x,y = odeHeun(f2, r0, t0, n, h)

#t,r = odeRK(f, r0, t0, n, h)

t, r, q = odeRKF(f, r0, t0, n, h, 1, 5, 0.001)

x = r[:,0]
y = r[:,1]

plt.plot(t, x)
plt.plot(t, y)
plt.show()
