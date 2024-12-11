import numpy as np

import matplotlib.pyplot as plt

# Sample data
np.random.seed(10)
data = [np.random.normal(0, std, 100) for std in range(1, 4)]

# Create a box plot
plt.boxplot(data, vert=True, patch_artist=True)

# Adding title and labels
plt.title('Box Plot Example')
plt.xlabel('Category')
plt.ylabel('Values')

# Show the plot
plt.show()