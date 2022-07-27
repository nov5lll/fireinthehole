## Code developed 25 jul 11:09am ##

# Defining molar mass #
from cmath import exp


MW = 1

# Defining Cp which's constant #
Cp = 1

# Defining A/F #
a = 2


####################################

## Equations ##

wf = -A*exp(-Ea/Ru*T)


## Equations ##

####################################


####################################

# Fuel rate #

## needs to be integrate ##

Yi = ((Ru*T)/P)*wi

DT = (-wf*hfF*Ru*T)/(2*Cp*PYf*(1+a))

## needs to be integrate ##

####################################