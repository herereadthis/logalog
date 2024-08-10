import matplotlib.pyplot as plt

# Define the coordinates with the last point returning to the starting point
coords = [
    (95, 619.5),
    (470, 309.5),
    (946, 16.5),
    (1082, 138.5),
    (1169.5, 367.5),
    (1008.5, 512.5),
    (824, 726.5),
    (616, 1114),
    (95, 619.5)  # Closing the polygon
]

# Extract x and y coordinates
x, y = zip(*coords)

# Plot the polygon
plt.figure(figsize=(10, 8))
plt.plot(x, y, marker='o', linestyle='-', color='b')
plt.fill(x, y, color='lightblue', alpha=0.5)

# Set the aspect of the plot to be equal
plt.gca().set_aspect('equal', adjustable='box')

# Invert the y-axis to have (0,0) at the top left
plt.gca().invert_yaxis()

# Set labels and title
plt.xlabel('X-coordinate')
plt.ylabel('Y-coordinate')
plt.title('Polygon Visualization with Coordinates')

# Show the plot
plt.grid(True)
plt.show()