import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the height matrix
height_matrix = [[12,13,1,12],
                [13,4,13,12],
                [13,8,10,12],
                [12,13,12,12],
                [13,13,13,13]]

# Convert to numpy array
data = np.array(height_matrix)

# Create the figure and 3D axes
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Create x and y coordinates for each point
x_len = len(data[0])
y_len = len(data)
x_coords, y_coords = np.meshgrid(np.arange(x_len), np.arange(y_len))

# Flatten the arrays for bar plot
x_coords_flat = x_coords.flatten()
y_coords_flat = y_coords.flatten()
z_coords = data.flatten()

# Set the size of each bar
dx = dy = 1.0

# Create the 3D bar plot
ax.bar3d(x_coords_flat, y_coords_flat, np.zeros_like(z_coords), dx, dy, z_coords, 
         shade=True, color='lightgrey', alpha=0.8)

# Add surface plot to connect the bars
surf = ax.plot_surface(x_coords, y_coords, data, alpha=0.3, color='lightgrey')

# Add elevation numbers on top of bars
for x, y, z in zip(x_coords_flat, y_coords_flat, z_coords):
    ax.text(x + dx/2, y + dy/2, z, f'{int(z)}', 
            horizontalalignment='center',
            verticalalignment='bottom')

# Customize the plot
ax.set_title('3D Elevation Grid', fontsize=14, pad=20)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Height')

# Adjust the viewing angle for better visualization
ax.view_init(elev=30, azim=45)

# Show the plot
plt.show()
