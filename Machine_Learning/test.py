import numpy as np
import matplotlib.pyplot as plt

# Define the range for x (real part)
x = np.linspace(0, 5, 500)  # x > 0 for arg(z) = pi/4
y = x  # y = x for arg(z) = pi/4

# Plot the graph
plt.figure(figsize=(6, 6))
plt.plot(x, y, label="arg(z) = π/4", color="blue")
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")  # x-axis
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")  # y-axis

# Add labels and title
plt.title("Graph of {z | arg(z) = π/4}", fontsize=14)
plt.xlabel("Re(z)", fontsize=12)
plt.ylabel("Im(z)", fontsize=12)
plt.grid(alpha=0.3)
plt.legend()
plt.axis("equal")

# Show the graph
plt.show()