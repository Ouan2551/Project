import numpy as np
import matplotlib.pyplot as plt
import json
import math
from scipy.constants import c # library import speed of light value

# Open .json file from directory
with open(r"D:\Important files Nannaphat\coding\My-project\SUT_Astro_coding_challenge #1\Challenge2_data.json", "r") as file:
    data = json.load(file)

# Extract data from JSON
m_values = data["Apparent Magitude (m)"]
M_values = data["Absolute Magnitude (M)"]
z_values = data["Redshift (z)"]

# Calculate distance (d) and velocity (v)
d_values = [math.exp((m - M + 5) / 5) for m, M in zip(m_values, M_values)]
v_values = [c * z for z in z_values]  # Corrected velocity formula
# line 17 variable 'c' use value of speed of light

# Sort d_values and v_values together
d_values, v_values = zip(*sorted(zip(d_values, v_values)))

# Convert to numpy arrays
d_values = np.array(d_values)
v_values = np.array(v_values)

# Calculate slope (gradient)
slopes = (np.gradient(v_values, d_values))* 3.242542 * (10**-19) # Use numpy gradient for slope

# Filter out NaN values from slopes
valid_slopes = slopes[~np.isnan(slopes)]

# Calculate the sum and average of valid slopes
if len(valid_slopes) > 0:
    slope_sum = np.sum(valid_slopes)
    avg_slope = np.mean(valid_slopes)
    t_value = 1 / avg_slope if avg_slope != 0 else np.inf
else:
    slope_sum = 0
    avg_slope = 0
    t_value = np.inf

# Print results
print(f"Sum of slopes: {slope_sum}")
print(f"Average slope: {avg_slope}")
print(f"t value: {t_value}")

# Plot the graph
plt.figure(figsize=(8, 6))
plt.plot(d_values, v_values, label="d vs v")
plt.xlabel("Distance (d)")
plt.ylabel("Velocity (v)")
plt.title("Distance vs Velocity")
plt.legend()
plt.grid(True)
plt.show()