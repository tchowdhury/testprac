import geopandas
import pandas as pd
import matplotlib.pyplot as plt
from shapely.geometry import Point
import contextily


#load the geospatial file
districts = geopandas.read_file('../data/Paris/paris_districts_utm.geojson')
restaurants = pd.read_csv('../data/Paris/paris_restaurants.csv')

# convert restaurants data frame to geopanda geodataframe
restaurants = geopandas.GeoDataFrame(restaurants, geometry=geopandas.points_from_xy(restaurants.x, restaurants.y))

# Print the CRS information
print(districts.crs)

# Plot the districts dataset
districts.plot()
plt.show()

# Convert the districts to the RGF93 reference system
districts_RGF93 = districts.to_crs(epsg=2154)

# Plot the districts dataset again
districts_RGF93.plot()
plt.show()

# Construct a Point object for the Eiffel Tower
eiffel_tower = Point(2.2945,48.8584 )

# Put the point in a GeoSeries with the correct CRS
s_eiffel_tower = geopandas.GeoSeries([eiffel_tower], crs={'init': 'epsg:4326'})

# Convert to other CRS
s_eiffel_tower_projected = s_eiffel_tower.to_crs(epsg=2154)

# Print the projected point
print(s_eiffel_tower_projected)

# Extract the single Point
eiffel_tower = s_eiffel_tower_projected[0]

# Ensure the restaurants use the same CRS
restaurants = restaurants.to_crs(s_eiffel_tower_projected.crs)

# The distance from each restaurant to the Eiffel Tower
dist_eiffel = restaurants.distance(eiffel_tower)

# The distance to the closest restaurant
print(dist_eiffel.min())


# Convert to the Web Mercator projection
restaurants_webmercator = restaurants.to_crs(epsg=3857)


# Plot the restaurants with a background map
ax = restaurants_webmercator.plot(markersize=1)
contextily.add_basemap(ax)
plt.show()

# Import the land use dataset
land_use = geopandas.read_file("paris_land_use.shp")
print(land_use.head())

# Make a plot of the land use with 'class' as the color
land_use.plot(column='class', legend=True, figsize=(15, 10))
plt.show()

# Add the area as a new column
land_use['area'] = land_use.geometry.area

# Calculate the total area for each land use class
total_area = land_use.groupby('class')['area'].sum() / 1000**2
print(total_area)

# Plot the two polygons
geopandas.GeoSeries([park_boulogne, muette]).plot(alpha=0.5, color=['green', 'blue'])
plt.show()

# Calculate the intersection of both polygons
intersection = park_boulogne.intersection(muette)

# Plot the intersection
geopandas.GeoSeries([intersection]).plot()
plt.show()

# Print proportion of district area that occupied park
print(intersection.area / muette.area)

# Print the land use datset and Notre-Dame district polygon
print(land_use.head())
print(type(muette))


# Calculate the intersection of the land use polygons with Notre Dame
land_use_muette = land_use.intersection(muette)

# Print the first rows of the overlay result
print(combined.head())

# Add the area as a column
combined['area'] = combined.area

# Take a subset for the Muette district
land_use_muette = combined[combined['district_name'] == 'Muette']

# Visualize the land use of the Muette district
land_use_muette.plot(column= 'class')
plt.show()

# Calculate the total area for each land use class
print(land_use_muette.groupby('class')['area'].sum() / 1000**2)

# Plot the intersection
land_use_muette.plot(edgecolor='black')
plt.show()

# Print the first five rows of the intersection
print(land_use_muette.head())

# Print the first five rows of both datasets
print(land_use.head())
print(districts.head())

# Overlay both datasets based on the intersection
combined = geopandas.overlay(land_use, districts, how='intersection')

# Print the first five rows of the result
print(combined.head())