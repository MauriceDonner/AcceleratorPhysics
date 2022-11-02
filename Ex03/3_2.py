import numpy as np
import matplotlib.pyplot as plt
import random
from layout import layout

# Read in the layout file (i parsed it from a simple string, was easier to download via ssh)
m = np.zeros((100,100))
metallic = np.zeros((100,100))

# Initialize the empty space with random potential values, and mark metallic structures
for i in range(100):
    for ii in range(100):
        if (layout[ii+i*100] == '0'):
            m[i][ii] = random.uniform(0,2)
        else:
            m[i][ii] = layout[ii+i*100]
            metallic[i][ii] = 1

# Plot the initial case
plt.figure()
plt.imshow(m)
plt.colorbar()
plt.tight_layout()
plt.savefig('3-1_0.png')

def phi(x,y):
    return m[y][x]
def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)
def Laplace(x,y,d):
    L = 1/4*(phi(x+d,y)+phi(x-d,y)+phi(x,y+d)+phi(x,y-d))
    return L-phi(x,y)
def Laplace_step(matrix,d,w):
    for i in range(len(matrix)):
        for ii in range(len(matrix[0])):
            if metallic[i][ii]: continue
            matrix[i][ii] = clamp(matrix[i][ii]+Laplace(ii,i,d)*w,0,2)

n = 2500
c = np.zeros((n))
for i in range(n):
    Laplace_step(m,d=1,w=1)
    c[i] = m[50][60]
    print(i,"/",n,end="\r")

xaxis = np.arange(n)
plt.figure()
plt.style.use('bmh')
plt.plot(xaxis,c)
plt.title("Convergence of point (50,60)")
plt.savefig("Convergence_new.png")

# for i in range(100):
#     name = '3-1_'+str(i+1)
#     Laplace_step(m,d=1,w=1.5)
#     plot_steps=10
#     if (i%plot_steps == 0):
#         plt.figure()
#         plt.imshow(m,vmin=0,vmax=2)
#         plt.colorbar()
#         plt.tight_layout()
#         plt.savefig(name)





