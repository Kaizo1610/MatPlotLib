import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
traffic = [100, 200, 300, 400, 500, 600]

#Create a line plot
plt.plot(months, traffic, color='blue', marker='o', linestyle='--')

plt.xlabel('Months')
plt.ylabel('Monthly Traffic')
plt.title('MONTHLY TRAFFIC REPORT')

plt.show()