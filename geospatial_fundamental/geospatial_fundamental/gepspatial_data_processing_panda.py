# Import all packages
import pandas as pd
import matplotlib.pyplot as plt
import contextily

# Read the restaurants csv file
restaurants = pd.read_csv('../data/Paris/paris_restaurants.csv')

# Inspect the first rows of restaurants
#print(restaurants.head())

#print(restaurants['type'].value_counts())

#filt_restaurants = restaurants[(restaurants['type']=='Caribbean restaurant') & (restaurants['type']=='European restuarant')]
#print(filt_restaurants.head())


# Make a plot of all points
# fig, ax = plt.subplots(figsize=(18,12))
# ax.plot(restaurants['x'],restaurants['y'], 'o', markersize=1)
# # Add all restaurants with map at the background
# contextily.add_basemap(ax)
# plt.show()