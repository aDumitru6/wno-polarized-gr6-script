# Uses the forward Euler method to simulate various mechanical artifacts 

import matplotlib.pyplot as plt
import numpy as np

# Real-life constants
E     = 3.0*10**9     # PMMA Young's modulus
G     = 1.2*10**9     # PMMA shear stress
rho   = 1180          # PMMA density
width = 0.029         # PMMA size
length= 0.060         # PMMA size
height= 0.015         # PMMA size

# Define some arbitrary parameters
I = (1/12)*rho*(width*length*height)*(length**2) # Moment of inertia
J = (np.pi/2) * 0.021**4
coefficient = [10**(-3), 10**(-3), 10**(-3), 10**(-6)]              # Frictional Coefficients (arbitrary)
theta    = 0     
vice_pos = 0.0001
k = G * J / width 

# Simulation characteristics
dt   = 0.000001
tmax = 2

def frictional_force(velocity, normal_force, coefficient, model = 'Coulomb'):
    '''Returns the frictional force on an object
    
    Arguments:
    velocity    -- Float showing the current relative velocity of the surfaces
    coefficient -- List showing the coefficients of friction describing the movement
    normal_force-- The transverse force on the two surfaces

    Keyword arguments:
    model       -- Model used for investigating the frictional forces (default is Coulomb)'''

    match model:
        case 'Coulomb':
            # Unpack the coefficient list
            mu = coefficient[0] 
            return -np.sign(velocity) * mu * normal_force
        case 'Stribeck':
            # Unpack the coefficient list
            Fc    = coefficient[0] * normal_force # Dynamic friction
            Fdds  = coefficient[1] * normal_force # Static - dynamic friction
            Fv    = coefficient[2] * abs(velocity)# Viscous sliding coefficient
            vs    = coefficient[3]                # Characteristic velocity
            return - np.sign(velocity) * (Fc + (Fdds / (1+(velocity/vs)**2))+ Fv)
        
def fwd_euler(ini,tf,dt):
  th0 = ini[0]
  om0 = ini[1]
  
  t=np.arange(0,tf,dt)
  th=np.zeros(len(t))
  th[0]=th0
  th[1]=th0+om0*dt

  vice_mvmt_tf  = 0.01
  vice_position = lambda t: float(t>1)*0.295#+ float(t<vice_mvmt_tf) * 0.001 * (5/360) * np.sin(t/vice_mvmt_tf) 
  normal_force  = lambda t: 1.120*9.81*2 #np.pi*(2.2**2-1.2**2)*10**(-4)*E*(vice_position(t)/width)

  for i in range(2,len(th)):
    om=(th[i-1] - th[i-2])/dt
    ep = (1/I) * (frictional_force(om,normal_force=normal_force(t[i-1]), coefficient=coefficient, model='Stribeck')) - k*(th[i-2] - vice_position(t[i-1]))
    if 1+1.5*dt> t[i-1] > 1:
      th[i]=100*dt+2*th[i-1]-th[i-2] 
    else:
      th[i]=ep*dt**2+2*th[i-1]-th[i-2] 

  return th

ini=[theta,100]


t=np.arange(0,tmax,dt)
plt.plot(t,fwd_euler(ini,tmax,dt))
plt.show()
