#Use NumPy and MatPlotLib to graph one period of sine and cosine on the same set of axes

import matplotlib.pyplot as plt
import numpy as np

# Synopsis
# The np sin & cos functions take an array_like and return an array_like
# Docs : https://docs.scipy.org/doc/numpy/reference/generated/numpy.sin.html#numpy.sin


#Create an array of angle values for 1 time period
x_angles = np.linspace(0, 2*np.pi, 100)

# Add the sine and cosine of the values in x_angles array)like
plt.plot(x_angles , np.sin(x_angles ))
plt.plot(x_angles , np.cos(x_angles ))

# Add Labels
plt.title('Sine and Cosine wave')
plt.xlabel('Radians')
plt.ylabel('Sin & Cos values')
plt.legend(['sin(x)', 'cos(x)'])
plt.axis('tight')

# Show chart
plt.show()