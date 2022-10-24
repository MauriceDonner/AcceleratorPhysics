import numpy as np
import matplotlib.pyplot as plt
plt.style.use('bmh')

V = 1000
B = 1
q = 1
m = 1.67e-27

def E(n):
    return n*V

def r(n):
    return np.sqrt(2*m*V)/q/B*np.sqrt(n)

xaxis = np.linspace(0,200,1000)
plt.figure()
plt.title('Particle Energy')
plt.plot(xaxis,E(xaxis)/10**6)
plt.ylabel('Particle Energy [MeV]')
plt.xlabel('# of half turns')
plt.tight_layout()

plt.figure()
plt.title('Cyclotron Radius')
plt.plot(xaxis,r(xaxis))
plt.ylabel('Cyclotron Radius [m]')
plt.xlabel('# of half turns')
plt.tight_layout()

xaxis = np.linspace(0,8*np.pi,1000)
plt.figure()
plt.title('Phase offset')
plt.plot(xaxis,np.sin(xaxis),label='voltage')
plt.plot(xaxis,np.sin(xaxis+np.pi),label='particle')
plt.legend()
plt.tight_layout()

plt.show()

