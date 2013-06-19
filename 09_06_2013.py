#!/bin/python
from numpy import *
from pylab import *
from sys import *
# INPUTS
v_i = 0.01 # m^3/s.

## PARAMETERS
I = 100 # number of floors. adimentional
H = 1 # pile height. meters
DD = 1 # some constant
l1 = 400 # side length 1. meters
l2 = 400 # side length 2. meters
ll2 = 410
ll1 = 410

dt = 3600 # time constant. seconds
dx = float(1/I) # meters
SIMULATION_TIME = 30*24*3600 # simulation length. seconds. 
SIMULATION_STEPS = int(SIMULATION_TIME/dt) # adimentional.
rho = 1000 # flow density. kg/m³.
R_ef = 1 # effective hydraulic radius
g = 9.8 # gravity constantat. meters / second²

## RESULTS (empty vars)
dd1 = zeros( (I, SIMULATION_STEPS)) # diffussion array 1
dd2 = zeros( (I, SIMULATION_STEPS)) # diffussion array 2
cc = zeros( (I, SIMULATION_STEPS)) # conveccion array
mm = zeros( (I, SIMULATION_STEPS)) # masses array
AA = zeros(I) #area array for each floor.
pp = zeros( (I, SIMULATION_STEPS)) # momentum array
m0 = 0

print ('building Area array...')
for i in range(0,I):
	# Area
	new_ll1=l1+(ll1-l1)*(i/I)
	new_ll2=l2+(ll2-l2)*(i/I)
	AA[i]=new_ll1*new_ll2
	# Area
	
	# init mass array for t=0
	m[i,0] = m0
	# init mass array for t=0

# cuando parte en k=0.
# m[i,0] existe.
#
print ('init')
for k in range(0, int(SIMULATION_TIME/dt)):
	for i in range(0,I):
		print (str(i)+'_'+str(k))
		m[i,k+1]=m[i,k]+(qq_0[
			
print ('end!')	
	
#print (AA)
exit(0) 
## Equations
# 1  # h_t = m_t/(rho*A)
# 2  # m_t[i,k+1] = m_t[i,k] + rho*pi*R_ef*h_t^2*(v_i - v_o) * dt
# 3  # rho = 1000
# 4  # R_ef = 1
# 5  # mm_0 = zeros(I)
# 6  # (v_t + v_o_t)/2 = p_t /m_t
# 7  # v_o_t = 2*p_t/m_t -v_t
# 8 # p_t = p_0 + m_t*g - k*(p_t/m_t)^2
# 9 # p_0 = ...
# 10 # m_t[i,k+1] = m_t[i,k] + (qq_0[i,k+1] - qq_1[i,k+1] + cc)*dt

# 11 # qq_0[i,i+1,k+1] = D/dx*(a[i]+a[i+1])*0.5*(m_t[i,k]/(a[i]*dx) -m_t[i,k+1]/(a[i+1]*dx)
# 12 # qq_1[i-1,i,k+1] = D/dx*(a[i-1]+a[i])*0.5*(m_t[i-1,k]/(a[i]*dx) -m_t[i,k+1]/(a[i]*dx)


## In Equilibrium :
# [0]    # v_o_t = v_o = p/m = v 

# 8' + [0] # m_t*g = k(p_t/m_t)^2
# 8' + 7   # m_t*g = k*v^2
# $?       # m_t = k*v^2/g
# $? + 1   # h_t = k*v^2/(g*rho*pi*R_ef*h^2)
#          #              g*rho*A
# 99       # q_o_t = rho*A_ef*v_o_t

# ACTUAL SIMULATION: DIFUSION=d1, DIFUSION=d2, CONVECCION=cc
print ('init')
for k in range(0, int(SIMULATION_TIME/dt)):
	for i in range(0,I):
		print (str(i)+'_'+str(k))
			
print ('end!')

# ACTUAL SIMULATION: CHEMICAL REACTIONS: c(j={