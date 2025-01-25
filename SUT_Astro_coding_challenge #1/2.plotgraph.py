import numpy as np
import matplotlib.pyplot as plt
import json

with open('G:\Important files Nannaphat\coding\My-project\SUT_Astro_coding_challenge #1\learning\Challenge2_data.json', 'r') as f:
    data = json.load(f);
print(data)

#x = np.array("Apparent Magitude (m)")
#y = np.array("Absolute Magnitude (M)")

#get data from json files
x_values = [data["Apparent Magitude (m)"]]
y_values = [data["Absolute Magnitude (M)"]]
z_values = [data["Redshift (z)"]]

#declare name graph
plt.xlabel("Apparent Magitude (m)")
plt.ylabel("Absolute Magnitude (M)")
plt.title('Plot of Data from JSON')

#output graph
plt.plot(x_values,y_values)
plt.show()