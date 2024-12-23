# Import all packages
import geopandas
import matplotlib.pyplot as plt
import contextily
import pandas as pd

# Read the geojson file
districts = geopandas.read_file('../data/Paris/paris_districts_utm.geojson')

# Read the restaurants csv file
df = pd.read_csv('../data/Paris/paris_restaurants.csv')

# Convert it to a GeoDataFrame
restaurants = geopandas.GeoDataFrame(df, geometry=geopandas.points_from_xy(df.x, df.y))

# Inspect the first rows of restaurants
print(districts.head())

# Inspect the first rows of the restaurants GeoDataFrame
print(restaurants.head())

# get area undr each plygon
#print(districts.geometry.area)

# Make a plot of all districts
districts.plot("district_name")


# Make a plot of the restaurants
ax = restaurants.plot(markersize=1)
contextily.add_basemap(ax)
plt.show()

