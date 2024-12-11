import numpy as np

import matplotlib.pyplot as plt

# Generate some data
data = np.random.rand(10, 10)

# Create the heatmap
plt.imshow(data, cmap='hot', interpolation='nearest')

# Add a color bar
plt.colorbar()

# Display the plot
plt.show()