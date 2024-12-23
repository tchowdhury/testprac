# Import the Point geometry
from shapely.geometry import Point
import geopandas
import pandas as pd
import matplotlib.pyplot as plt
import contextily

# Construct a point object for the Eiffel Tower
eiffel_tower = Point(448935.6,5411371.9)


# Plot Eiffel Tower on the map
# fig, ax = plt.subplots(figsize=(18,12))
# ax.plot(eiffel_tower.x, eiffel_tower.y, 'o', markersize=10, color='green')
# # Add all restaurants with map at the background
# contextily.add_basemap(ax)
# plt.show()

# Print the result
#print(eiffel_tower)

#load the district and resturants spatial file
restaurants = pd.read_csv('../data/Paris/paris_restaurants.csv')
districts = geopandas.read_file('../data/Paris/paris_districts_utm.geojson')
stations = geopandas.read_file('../data/Paris/paris_sharing_bike_stations_utm.geojson')
trees = geopandas.read_file('../data/Paris/paris_trees_small.gpkg')

print(trees.columns)
print(districts.columns)
# The trees dataset with point locations of trees
#print(trees.head())

# convert restaurants data frame to geopanda geodataframe
restaurants = geopandas.GeoDataFrame(restaurants, geometry=geopandas.points_from_xy(restaurants.x, restaurants.y))


# Accessing the Montparnasse geometry (Polygon) and restaurant
district_montparnasse = districts.loc[52, 'geometry']
resto = restaurants.loc[956, 'geometry']


#print(district_montparnasse)
#print(resto)

# Is the Eiffel Tower located within the Montparnasse district?
print(eiffel_tower.within(district_montparnasse))

# Does the Montparnasse district contains the restaurant?
print(district_montparnasse.contains(resto))

# The distance between the Eiffel Tower and the restaurant?
print(eiffel_tower.distance(resto))

# Create a boolean Series
mask = districts.contains(eiffel_tower)

# Print the boolean Series
print(mask.head())

# Filter the districts with the boolean mask
print(districts[mask])

# The distance from each restaurant to the Eiffel Tower
dist_eiffel = restaurants.distance(eiffel_tower)

# The distance to the closest restaurant
#print(dist_eiffel.min())

# Filter the restaurants for closer than 1 km
restaurants_eiffel = restaurants[dist_eiffel > 800000 ]

# Make a plot of the close-by restaurants
# ax = restaurants_eiffel.plot()
# geopandas.GeoSeries([eiffel_tower]).plot(ax=ax, color='red')
# contextily.add_basemap(ax)
# ax.set_axis_off()
# plt.show()


#Download river shape data
url = 'https://github.com/nvkelso/natural-earth-vector/blob/master/50m_physical/ne_50m_rivers_lake_centerlines.shp'
rivers = geopandas.read_file('../data/ne_50m_rivers_lake_centerlines.shp')
amazon = rivers[rivers['name'] == 'Amazonas'].geometry.squeeze()
#print(amazon)
#mask = countries.intersects(amazon)
#print(countries[mask])

# Spatial join
# Join the districts and stations datasets
joined = geopandas.sjoin(stations, districts[['district_name', 'geometry']],predicate="within")

# Inspect the first five rows of the result
print(joined.head())

# Spatial join of the trees and districts datasets
joined1 = geopandas.sjoin(trees, districts[['district_name', 'geometry']],predicate="within")

# Inspect the first five rows of the result
#print(joined1.head())

# Calculate the number of trees in each district
trees_by_district = joined1.groupby('district_name').size()

# Convert the series to a DataFrame and specify column name
trees_by_district = trees_by_district.to_frame(name='n_trees')

# Inspect the result
#print(trees_by_district.head())

# Merge the 'districts' and 'trees_by_district' dataframes
districts_trees = pd.merge(districts, trees_by_district, on='district_name')

# Add a column with the tree density
districts_trees['n_trees_per_area'] = (districts_trees['n_trees'] / districts.geometry.area)*1000

# Make a choropleth of the number of trees
districts_trees.plot(column='n_trees', legend=True)
plt.show()

# Make a choropleth of the number of trees per area
districts_trees.plot(column='n_trees_per_area', legend=True)
plt.show()

# Make a choropleth of the number of trees
districts_trees.plot(column='n_trees_per_area', scheme='equal_interval',legend=True)
plt.show()

# Generate the choropleth and store the axis
ax = districts_trees.plot(column='n_trees_per_area', scheme='quantiles',
                          k=7, cmap='YlGn', legend=True)

# Remove frames, ticks and tick labels from the axis
ax.set_axis_off()
plt.show()

# Set up figure and subplots
fig, axes = plt.subplots(nrows=2)

# Plot equal interval map
districts_trees.plot(column='n_trees_per_area', scheme='equal_interval', k=5, legend=True, ax=axes[0])
axes[0].set_title('Equal Interval')
axes[0].set_axis_off()

# Plot quantiles map
districts_trees.plot(column='n_trees_per_area', scheme='quantiles', k=5, legend=True, ax=axes[1])
axes[1].set_title('Quantiles')
axes[1].set_axis_off()

# Display maps
plt.show()

