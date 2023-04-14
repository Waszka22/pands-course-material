import numpy as np
import matplotlib.pyplot as plt

# Define the range of x values from 0 to 4
x = np.linspace(0, 4, 100)

# Define the functions f(x), g(x), and h(x)
f = x
g = x**2
h = x**3

# Plot the functions on one set of axes
plt.plot(x, f, 'r', label='f(x) = x')
plt.plot(x, g, 'g', label='g(x) = x^2')
plt.plot(x, h, 'b', label='h(x) = x^3')

# Add title, labels, and legend to the plot
plt.title('Functions f(x), g(x), and h(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Show the plot
plt.show()