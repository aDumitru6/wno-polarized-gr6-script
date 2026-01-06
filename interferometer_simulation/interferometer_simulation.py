import numpy as np
import matplotlib.pyplot as plt 

wavelength       = 700 * 10**(-9)          # The laser wavelength
biref_thickness  = 0.1                     # The birefringent block length
index_refraction = 1.49
blockArea        = 0.01                  # The area of the face to which stress is applied
idenitity_matrix = np.array([[1,0],[0,1]]) # 2x2 idenitity matrix
C_upper          = 1.0*10**(-10)           # Upper estimate for C
C_lower          = 5.3*10**(-12)           # Lower estimate for C
mass_max         = 15                     # Maximum mass to put on the block
g                = 9.81                    # Gravitational acceleration

auto_compute_system = lambda n: 1+np.cos((2*np.pi*biref_thickness/wavelength)*(index_refraction-1))*np.cos(np.pi*biref_thickness*n/wavelength)

# Get figure and axis objects
fig, ax = plt.subplots(ncols = 2, nrows = 1, sharey=True, constrained_layout=True)
fig.set_size_inches((13,6))

# Loop over some systems
index_refr_lower = np.linspace(0, C_lower*(mass_max*g)/(blockArea),1000)
index_refr_upper = np.linspace(0, C_upper*(mass_max*g)/(blockArea),1000)

# LOWBALL ESTIMATE
transmission_lower           = np.empty_like(index_refr_lower)

# Get the transmission for each angle and index
for i in range(len(index_refr_lower)):
    transmission_lower[i]=auto_compute_system(index_refr_lower[i])

# For each angle, plot the transmission against the mass placed on top of the PMMA block
ax[0].plot(index_refr_lower*(blockArea)/(C_lower*g), transmission_lower)

# Refine the figure
ax[0].set_title (f"Lowball estimate, T vs mass, interferometer, maxdiff = {round(max(list(transmission_lower))-min(list(transmission_lower)),4)}")
ax[0].set_ylabel("Transmission T")
ax[0].set_xlabel("Mass on the block, in kg")
ax[0].legend()

# HIGHBALL ESTIMATE
transmission_upper           = np.empty_like(index_refr_upper)

# Get the transmission for each angle and index
for i in range(len(index_refr_upper)):
    transmission_upper[i]=auto_compute_system(index_refr_upper[i])

# For each angle, plot the transmission against the mass placed on top of the PMMA block
ax[1].plot(index_refr_upper*(blockArea)/(C_upper*g), transmission_upper)

# Refine the figure
ax[1].set_title(f"Highball estimate, T vs mass, interferometer, maxdiff = {round(max(list(transmission_upper))-min(list(transmission_upper)),4)}")
ax[1].set_xlabel("Mass on the block, in kg")
ax[1].legend()

plt.show()
