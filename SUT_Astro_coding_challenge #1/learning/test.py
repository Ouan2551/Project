import numpy as np
import matplotlib.pyplot as plt
import json
import math

# Load JSON data
with open("D:/Important files Nannaphat/coding/My-project/SUT_Astro_coding_challenge #1/Challenge2_data.json", "r") as file:
    data = json.load(file)

# Extract values
m_values = data["Apparent Magitude (m)"]
M_values = data["Absolute Magnitude (M)"]
z_values = data["Redshift (z)"]

d_values = []
v_values = []

# Calculate distance 'd' using the distance modulus formula
for m, M in zip(m_values, M_values):
    d = 10 ** ((m - M + 5) / 5)  # Correct formula
    d_values.append(d)

# Calculate velocity 'v'
for z in z_values:
    v = (3 * 10**8) * z  # Correct exponentiation operator
    v_values.append(v)

# Plot the graph
plt.figure(figsize=(8, 6))
plt.xlabel("Distance (d) [parsecs]")
plt.ylabel("Velocity (v) [m/s]")
plt.title("Distance vs. Velocity Graph")
plt.plot(d_values, v_values, marker='o', linestyle='-', color='blue')
plt.grid()
plt.show()

# Calculate and print the ratio t = d / v
print("Distance (d), Velocity (v), Ratio (t = d/v):")
for d, v in zip(d_values, v_values):
    t = d / v
    print(f"d = {d:.2e} parsecs, v = {v:.2e} m/s, t = {t:.2e} s")