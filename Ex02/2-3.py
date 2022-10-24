import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,0,0])
v = np.array([0,-1,0])
B = np.array([0,0,1])
# Define Lorentzforce
F = np.cross(v,B)

for seconds in range(10):
    xnew = x+v
    v_new = 
