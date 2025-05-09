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
    d = math.exp((M - m) / 5) + 1
    d_values.append(d)
    
for i, (z) in enumerate(zip(z_values), start=1):
    v = (3 * 10^8) * z
    v_values.append(v)
    
# sort the value 'd' and 'v'
d_values.sort()
v_values.sort()

# use for test array store value
plt.xlabel("d")
plt.ylabel("v")
plt.title('d and v graph test version')

plt.plot(d_values, v_values)
plt.show()

for i, (v_values,d_values) in enumerate(zip(v_values, d_values), start=1):
    t = d_values/v_values
    print(t)