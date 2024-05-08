import matplotlib.pyplot as plt

# Create a canvas for artwork
fig, ax = plt.subplots()

# Draw patterns on the canvas
# Example: Drawing a checkerboard pattern
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            ax.add_patch(plt.Rectangle((i, j), 1, 1, color='black'))
        else:
            ax.add_patch(plt.Rectangle((i, j), 1, 1, color='white'))

# Customize the plot
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(0, 8)
ax.set_ylim(0, 8)

# Add title
plt.title('Checkerboard Pattern')

# Display the artwork
plt.show()
