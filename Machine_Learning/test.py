import numpy
import matplotlib.pyplot as plt

# First scatter plot data
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

# Second scatter plot data using normal distributions
m = numpy.random.normal(5.0, 1.0, 1000)
n = numpy.random.normal(10.0, 2.0, 1000)

# Create a figure with two subplots: 1 row, 2 columns
plt.figure(figsize=(12, 6))

# First subplot: Scatter plot for x, y
plt.subplot(1, 2, 1)  # (rows, columns, index of subplot)
plt.scatter(x, y)
plt.title('First Scatter Plot')
plt.xlabel('X axis')
plt.ylabel('Y axis')

# Second subplot: Scatter plot for m, n
plt.subplot(1, 2, 2)  # (rows, columns, index of subplot)
plt.scatter(m, n)
plt.title('Second Scatter Plot')
plt.xlabel('M axis')
plt.ylabel('N axis')

# Show both plots
plt.tight_layout()  # Adjusts layout so that plots don't overlap
plt.show()
