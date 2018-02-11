#!/usr/bin/python
# vim: set fileencoding=<encoding name> :

# Import some packages from matplotlib
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# Uncomment the next line for use in a Jupyter notebook
#%matplotlib inline

# Define the filename, read and plot the image
filename = 'sample.jpg'
image = mpimg.imread(filename)
plt.imshow(image)
plt.show()