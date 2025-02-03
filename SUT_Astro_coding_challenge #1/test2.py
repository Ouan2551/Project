import numpy as np
import matplotlib.pyplot as plt
import json
import math
from scipy.constants import c  # Speed of light

# Open the JSON file with data
with open(r"D:\Important files Nannaphat\coding\Project\SUT_Astro_coding_challenge #1\Challenge2_data.json", "r") as file:
    data = json.load(file)

# Get data from JSON file
apparent_magnitude = data["Apparent Magitude (m)"]
absolute_magnitude = data["Absolute Magnitude (M)"]
redshift = data["Redshift (z)"]

# Calculate distance (d) using distance modulus formula
distance = []
for m, M in zip(apparent_magnitude, absolute_magnitude):
    d = math.exp((m - M + 5) / 5)
    distance.append(d)

# Calculate velocity (v) using redshift and speed of light
velocity = []
for z in redshift:
    v = c * z  # v = z * speed of light
    velocity.append(v)

# Sort distance and velocity together
distance, velocity = zip(*sorted(zip(distance, velocity)))

# Convert lists to numpy arrays for calculations
distance = np.array(distance)
velocity = np.array(velocity)

# Calculate slope using numpy's gradient function
slope = np.gradient(velocity, distance) * 3.242542 * (10 ** -19)

# Filter out NaN values
valid_slopes = slope[~np.isnan(slope)]

# Calculate the sum, average, and t value
if len(valid_slopes) > 0:
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

# Plot the graph
plt.figure(figsize=(8, 6))
plt.plot(distance, velocity, label="Distance vs Velocity")
plt.xlabel("Distance (d)")
plt.ylabel("Velocity (v)")
plt.title("Distance vs Velocity")
plt.legend()
plt.grid(True)
plt.show()