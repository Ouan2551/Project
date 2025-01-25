import numpy as np
import matplotlib.pyplot as plt
import json
import math

with open("D:\Important files Nannaphat\coding\My-project\SUT_Astro_coding_challenge #1\Challenge2_data.json", "r") as file:
    data = json.load(file)

m_values = data["Apparent Magitude (m)"]
M_values = data["Absolute Magnitude (M)"]
z_values = data["Redshift (z)"]

d_values = []
v_values = []

for i, (m, M) in enumerate(zip(m_values, M_values), start=1):
    d = 10**((m - M + 5) / 5)
    d_values.append(d)

for i, z in enumerate(z_values, start=1):
    v = (3 * 10^8) * z
    v_values.append(v)

# sort the value 'd' and 'v'
d_values.sort()
v_values.sort()

# calculate t
for d, v in zip(d_values, v_values):
    t = d / v
    print(t)

# use for test array store value
plt.xlabel("d")
plt.ylabel("v")
plt.title("d and v graph")

# show graph
plt.plot(d_values, v_values)
plt.show()