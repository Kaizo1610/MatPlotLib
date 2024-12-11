import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Define the data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
product_A = [10, 25, 40, 45, 60, 100]
product_B = [20, 30, 60, 65, 75, 90]

#Create a line plot
plt.plot(months, product_A, color='blue', marker='o', linestyle='--', label='Product A')

plt.plot(months, product_B, color='red', marker='o', linestyle='--', label='Product B')

#Add labels and title
plt.xlabel('Months')
plt.ylabel('Monthly Revenue')
plt.title('MONTHLY REVENUE COMPARISON')

#Display the legend
plt.legend()

plt.show()