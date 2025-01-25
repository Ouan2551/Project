import numpy as np
import matplotlib.pyplot as plt
import json
import math

# Open .json file from directory
with open(r"D:\Important files Nannaphat\coding\My-project\SUT_Astro_coding_challenge #1\Challenge2_data.json", "r") as file:
    data = json.load(file)

# Extract data from JSON
m_values = data["Apparent Magitude (m)"]
M_values = data["Absolute Magnitude (M)"]
z_values = data["Redshift (z)"]

# Calculate distance (d) and velocity (v)
d_values = [10**((m - M + 5) / 5) for m, M in zip(m_values, M_values)]
v_values = [3 * 10**8 * z for z in z_values]  # Corrected velocity formula

d_values.sort()
v_values.sort()

# Calculate slope (gradient)
slopes = np.gradient(v_values, d_values)  # Use numpy gradient for slope

# Plot the graph
plt.figure(figsize=(8, 6))
plt.plot(d_values, v_values, label="d vs v")
plt.xlabel("Distance (d)")
plt.ylabel("Velocity (v)")
plt.title("Distance vs Velocity")
plt.legend()
plt.grid(True)
plt.show()

# Print slopes for debugging
for d, v, s in zip(d_values, v_values, slopes):
    print(f"d: {d:.2f}, v: {v:.2e}, slope: {s}")

slopes = list(slopes)
sum = 0
for i in range(0, len(slopes)):
    if slopes[i] == nan:
        break
    sum = sum + slopes[i]
    print("sum : ", sum)

result = sum/len(slopes)
print("result : ", result)
print("t : ", 1/result)

# find avg slope
# problem now code t value is nan