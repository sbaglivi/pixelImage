import os
from skimage import io
from matplotlib import pyplot as plt
import numpy as np

#filename = os.path.join(skimage.data_dir, 'moon.png')
filename = './moon.jpeg'
moon = io.imread(filename)
print(moon.shape)
luminosity = np.empty((moon.shape[0],moon.shape[1])) 
for row in range(moon.shape[0]):
    for col in range(moon.shape[1]):
        luminosity[row][col] = moon[row][col].mean()/255

print(luminosity.shape)
plt.imshow(luminosity,cmap='Greys')
plt.show()

"""
plt.imshow(moon)
plt.show()
"""
