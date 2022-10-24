import numpy as np
import matplotlib.pyplot as plt
plt.style.use('bmh')

q = 1
B = 1

def cyclotron_frequency(p,m):
    return 10**6*q*B/(2*np.pi*m*np.sqrt(1+(p/m)**2))

xaxis = np.linspace(0,100,1000)

plt.figure()
plt.title('Relativistic case electron')
plt.ylabel('Cyclotron frequency [1/s]')
plt.xlabel('Particle momentum in MeV')
plt.plot(xaxis,cyclotron_frequency(xaxis,0.511),label = 'electron')
plt.tight_layout()
plt.figure()
plt.title('Relativistic case proton')
plt.ylabel('Cyclotron frequency [1/s]')
plt.xlabel('Particle momentum in MeV')
plt.plot(xaxis,cyclotron_frequency(xaxis,938),label = 'proton')
plt.tight_layout()
plt.show()
