import numpy as np
import matplotlib.pyplot as plt
import json
from scipy.constants import c  # Speed of light

# Load data from JSON file
with open(r"D:\Important files Nannaphat\coding\Project\SUT_Astro_coding_challenge #1\Challenge2_data.json", "r") as file:
    data = json.load(file)

# Extract data from JSON
apparent_magnitude = data["Apparent Magitude (m)"]
absolute_magnitude = data["Absolute Magnitude (M)"]
redshift = data["Redshift (z)"]

# Calculate distance using the distance modulus formula: d = 10^((m - M + 5)/5)
distance = 10 ** ((np.array(apparent_magnitude) - np.array(absolute_magnitude) + 5) / 5)

# Calculate velocity using redshift: v = z * speed of light
velocity = np.array(redshift) * c

# Sort distance and velocity together
sorted_indices = np.argsort(distance)
distance = distance[sorted_indices]
velocity = velocity[sorted_indices]

# Calculate the slope of the distance-velocity relationship
# Using numpy's gradient function: slope = dv/dd
slope = np.gradient(velocity, distance)

# Convert slope to Hubble constant units (1/s)
slope *= 3.242542e-19  # Conversion factor from km/s/Mpc to 1/s

# Filter out NaN values (if any)
valid_slopes = slope[~np.isnan(slope)]

# Calculate the sum, average, and t value (Hubble time)
if valid_slopes.size > 0:
    sum_of_slopes = np.sum(valid_slopes)
    average_slope = np.mean(valid_slopes)
    t_value = 1 / average_slope if average_slope != 0 else float('inf')
else:
    sum_of_slopes = 0
    average_slope = 0
    t_value = float('inf')

# Print the results
print(f"Sum of slopes: {sum_of_slopes}")
print(f"Average slope: {average_slope}")
print(f"t value (in seconds): {t_value}")
print(f"t value (in years): {t_value / 31556926}")  # Convert seconds to years

# Plot the distance-velocity graph
plt.figure(figsize=(8, 6))
plt.plot(distance, velocity, label="Distance vs Velocity", marker='o', linestyle='-', markersize=5)
plt.xlabel("Distance (Mpc)")
plt.ylabel("Velocity (km/s)")
plt.title("Distance vs Velocity")
plt.legend()
plt.grid(True)
plt.show()