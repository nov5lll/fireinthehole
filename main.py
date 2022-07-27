from RKF45 import *
# we need to define f, r0, t0, n, h, alpha, k, tol

# Defining the constants:
A = 3.8*(10**11)

m = 0.25

n = 1.5

u = 15.5

Ru = 8314         #------------- J/kmol.K

Ea = 15098*Ru     #------------- K

P = 101325        #------------- Pa

deltahc = 440602  #------------- kJ/kg

Cp = 1685.07      #------------- J/kg.K

M = 29            #------------- kg/mol




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
