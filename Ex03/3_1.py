import numpy as np
import matplotlib.pyplot as plt
import random
from layout import layout

# Read in the layout file (i parsed it from a simple string, was easier to download via ssh)
m = np.zeros((100,100))
for i in range(100):
    for ii in range(100):
        m[i][ii] = layout[ii+i*100]

plt.imshow(m)
plt.savefig('3-1.png')

