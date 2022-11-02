import numpy as np
import matplotlib.pyplot as plt
import random
from layout import layout

# Read in the layout file (i parsed it from a simple string, was easier to download via ssh)
m = np.zeros((100,100))
metallic = np.zeros((100,100))
for i in range(100):
    for ii in range(100):
        if (layout[ii+i*100] == '0'):
            m[i][ii] = random.uniform(0,2)
            #m[i][ii] = 0
        else:
            m[i][ii] = layout[ii+i*100]
            metallic[i][ii] = 1

plt.figure()
plt.imshow(m)
plt.colorbar()
plt.title('Speed x1')
plt.tight_layout()
plt.savefig('3-1_0.png')
plt.figure()
plt.imshow(metallic)
plt.savefig('3-1m.png')

def phi(x,y):
    return m[x][y]
def Laplace(x,y,d):
    return 1/4*(phi(x+d,y)+phi(x-d,y)+phi(x,y+d)+phi(x,y-d))
def Laplace_step(matrix,d):
    for i in range(len(matrix)):
        for ii in range(len(matrix[0])):
            if metallic[ii][i]: continue
            matrix[ii][i] = Laplace(ii,i,d)

for i in range(25):
    name = '3-1_'+str(i+1)
    Laplace_step(m,1)
    plot_steps=1
    if (i%plot_steps == 0):
        plt.figure()
        plt.title('Speed x1')
        plt.imshow(m,vmin=0,vmax=2)
        plt.colorbar()
        plt.tight_layout()
        plt.savefig(name)






