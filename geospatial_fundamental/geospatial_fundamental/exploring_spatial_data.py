import geopandas
import pandas as pd
import matplotlib.pyplot as plt
import contextily

# # Load the restaurants dataset
restaurants = pd.read_csv('../data/Paris/paris_restaurants.csv')
# convert restaurants data frame to geopanda geodataframe
restaurants_geo = geopandas.GeoDataFrame(restaurants, geometry=geopandas.points_from_xy(restaurants.x, restaurants.y))

# Read the geojson file
districts = geopandas.read_file('../data/Paris/paris_districts_utm.geojson')

# check first rows
#print(df.head())

# Calculate the number of restaurants of each type
type_counts = restaurants.groupby('type').size()

# Print the result
#print(type_counts)

# Take a subset of the African restaurants
african_restaurants = restaurants[restaurants['type'] == 'African restaurant']

# convert normal dataframe into geo data frame
african_rest = geopandas.GeoDataFrame(african_restaurants, geometry=geopandas.points_from_xy(african_restaurants.x, african_restaurants.y))

#print(type(african_rest))
#print(type(districts))

#Plot the history
#districts.plot(column='district_name')

# Make a multi-layered plot
fig, ax = plt.subplots(figsize=(18,9))
restaurants_geo.plot(ax=ax, color='grey')
african_rest.plot(ax=ax, color='red')
# Remove the box, ticks and labels
#ax.set_axis_off()


# Add a population density column
districts['population_density'] = districts['population'] / districts.area * 10**6

# Make a plot of the districts colored by the population density
districts.plot(column='population_density', legend=True)

plt.show()