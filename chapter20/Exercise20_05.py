# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(AVL tree animation) Write a program that animates the AVL tree insert, delete
and search methods'''

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from AVLTree import AVLTree

# Initialize the AVL tree
avlTree = AVLTree()

# Create a figure and axis for plotting
fig, ax = plt.subplots()
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_aspect('equal')

# Function to update the plot with AVL tree visualization
def updatePlot():
    ax.clear()
    # TODO: Update the plot with AVL tree visualization

# Function to animate the AVL tree operations
def animateOperations(*args):
    # TODO: Perform AVL tree insert, delete, or search operations
    # Update the plot after each operation
    updatePlot()

# Animate the AVL tree operations
ani = animation.FuncAnimation(fig, animateOperations, frames=range(10), interval=1000, repeat=False)
plt.show()

# GitHub Emojis for reference:
# :bar_chart: - Bar Chart
# :chart_with_upwards_trend: - Chart With Upwards Trend
# :chart_with_downwards_trend: - Chart With Downwards Trend
# :chart: - Chart Increasing
# :chart_decreasing: - Chart Decreasing
# :chart_with_ascending_trend: - Chart With Ascending Trend
# :chart_with_descending_trend: - Chart With Descending Trend
# :chart: - Chart Increasing
# :chart_with_upwards_trend: - Chart With Upwards Trend
# :chart_with_downwards_trend: - Chart With Downwards Trend
# :chart: - Chart Increasing
# :chart_with_upwards_trend: - Chart With Upwards Trend
# :chart_with_downwards_trend: - Chart With Downwards Trend
# :chart: - Chart Increasing
# :chart_with_upwards_trend: - Chart With Upwards Trend
# :chart_with_downwards_trend: - Chart With Downwards Trend
# :chart: - Chart Increasing
# :chart_with_upwards_trend: - Chart With Upwards Trend
# :chart_with_downwards_trend: - Chart With Downwards Trend
# :bar_chart: - Bar Chart
# :chart_with_upwards_trend: - Chart With Upwards Trend
# :chart_with_downwards_trend: - Chart With Downwards Trend

