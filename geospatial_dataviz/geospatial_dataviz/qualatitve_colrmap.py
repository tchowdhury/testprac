# Import pandas and matplotlib.pyplot using their customary aliases
import pandas as pd
import matplotlib.pyplot as plt
import geopandas
from shapely.geometry import Point
import pprint
import folium
import webbrowser

def auto_open(path, f_map):
    html_page = f'{path}'
    f_map.save(html_page)
    # open in browser.
    new = 2
    webbrowser.open(html_page, new=new)


## Read in the School Districts geojson file
school_districts = geopandas.read_file('../data/school_districts.geojson')
# Read in the neighborhoods geojson file
neighborhoods = geopandas.read_file('../data/neighborhoods.geojson')
# Read in the public art csv file
art = pd.read_csv('../data/public_art.csv')
#print(art.head())
# Create a geometry column from lng & lat
#art['geometry'] = art.apply(lambda x: Point(float(x.Longitude), float(x.Latitude)), axis=1)
art['geometry'] = geopandas.points_from_xy(art.Longitude, art.Latitude)

# Create a GeoDataFrame from art and verify the type
art_geo = geopandas.GeoDataFrame(art, crs = neighborhoods.crs, geometry = art.geometry)
#print(type(art_geo))
# Create art_dist_meters using art and the geometry from art
art_dist_meters = geopandas.GeoDataFrame(art, geometry = art.geometry, crs = 'epsg:4326')
#print(art_dist_meters.head(2))

# Set the crs of art_dist_meters to use EPSG:3857
art_dist_meters.geometry = art_dist_meters.geometry.to_crs(crs = 3857)
#print(art_dist_meters.head(2))


# print(school_districts.head())
# print(school_districts.crs)
# print(school_districts.columns)
# # Print the first few rows of neighborhoods
# print(neighborhoods.head())
# print(neighborhoods.columns)
# print(neighborhoods.crs)
#
# print(art.columns)
# print(art_geo.head())
# print(art_geo.columns)

# Set legend style
lgnd_kwds = {'title': 'School Districts',
               'loc': 'upper left', 'bbox_to_anchor': (1, 1.03), 'ncol': 2}

# Plot the school districts using the tab20 colormap (qualitative)
school_districts.plot(column = 'district', cmap = 'tab20', legend = True, legend_kwds = lgnd_kwds)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Nashville School Districts')
plt.show()


school_districts.plot(column = 'district', cmap = 'summer', legend = True, legend_kwds = lgnd_kwds)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Nashville School Districts')
plt.show()

# Plot the school districts using Set3 colormap without the column argument
school_districts.plot(cmap = 'Set3', legend = True, legend_kwds = lgnd_kwds)
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.title('Nashville School Districts')
plt.show();

# Plot the neighborhoods, color according to name and use the Dark2 colormap
neighborhoods.plot(column = 'name', cmap = 'Dark2')

# Show the plot.
plt.show()

# Spatially join art_geo and neighborhoods
art_intersect_neighborhoods = geopandas.sjoin(art_geo, neighborhoods, predicate = 'intersects')
# Print the shape property of art_intersect_neighborhoods
print(art_intersect_neighborhoods.shape)

# Create art_within_neighborhoods by spatially joining art_geo and neighborhoods
art_within_neighborhoods = geopandas.sjoin(art_geo, neighborhoods, predicate = 'within')

# Print the shape property of art_within_neighborhoods
print(art_within_neighborhoods.shape)

# Spatially join art_geo and neighborhoods and using the contains predicate
art_containing_neighborhoods = geopandas.sjoin(art_geo, neighborhoods, predicate = 'contains')

# Print the shape property of art_containing_neighborhoods
print(art_containing_neighborhoods.shape)

# Spatially join neighborhoods with art_geo
neighborhood_art = geopandas.sjoin(art_geo, neighborhoods, predicate = "within")

# Print the first few rows
#print(neighborhood_art.head())
#print(neighborhood_art.columns)

# Get name and title from neighborhood_art and group by name
neighborhood_art_grouped = neighborhood_art[['name', 'Title']].groupby('name')

# Aggregate the grouped data and count the artworks within each polygon
print(neighborhood_art_grouped.agg('count').sort_values(by = 'Title', ascending = False))

# Create urban_art from neighborhood_art where the neighborhood name is Urban Residents
urban_art = neighborhood_art.loc[neighborhood_art.name == 'Urban Residents']
#print(urban_art.columns)

# Get just the Urban Residents neighborhood polygon and save it as urban_polygon
urban_polygon = neighborhoods.loc[neighborhoods.name == "Urban Residents"]

# Plot the urban_polygon as ax
ax = urban_polygon.plot(color = 'lightgreen')

# Add a plot of the urban_art and show it
urban_art.plot( ax = ax, column = 'Type', legend = True);
plt.show()

# Print the head of the urban polygon
#print(urban_polygon.head())

# Create a copy of the urban_polygon using EPSG:3857 and print the head
urban_poly_3857 = urban_polygon.to_crs(epsg = 3857)
#print(urban_poly_3857.head())
#print(type(urban_poly_3857))

# Print the area of urban_poly_3857 in kilometers squared
area = urban_poly_3857.area / 10**6
#print(type(area1))
#print(area1[41])
print('The area of the Urban Residents neighborhood is ', area[41], ' km squared')

# Create downtown_center from urban_poly_3857
downtown_center = urban_poly_3857.geometry.centroid

# Print the type of downtown_center
print(type(downtown_center))

# Plot the urban_poly_3857 as ax and add the center point
ax = urban_poly_3857.plot(color = 'lightgreen')
downtown_center.plot(ax = ax, color = 'black')
plt.xticks(rotation = 45)

# Show the plot
plt.show()


# Add a column to art_meters, center
art_dist_meters['center'] = art_dist_meters.geometry.centroid[0]
#print(art_dist_meters[['geometry','center']])

# Build a dictionary of titles and distances for Urban Residents art
art_distances = {}
for row in art_dist_meters.iterrows():
    vals = row[1]
    key = vals['Title']
    ctr = vals['center']
    art_distances[key] = vals['geometry'].distance(ctr)

# Pretty print the art_distances
#pprint.pprint(art_distances)

#urban_polygon['center'] = urban_polygon.geometry.centroid[41]
urban_polygon['center'] = urban_polygon.loc[41,'geometry'].centroid

#print(urban_polygon.head())
#print(urban_polygon.loc[41,'geometry'])

# Create urban_center from the urban_polygon center
#urban_center = urban_polygon.center[41]
urban_center = urban_polygon.loc[41,'center']

# Print urban_center
print(urban_center)

# Create array for folium called urban_location
urban_location = [urban_center.y, urban_center.x]

# Print urban_location
print(urban_location)

# Construct a folium map with urban_location
#downtown_map = folium.Map(location = urban_location, zoom_start = 15)

# Create array for called folium_loc from the urban_polygon center point
point = urban_polygon.loc[41,'center']
folium_loc = [point.y, point.x]

# Construct a map from folium_loc: downtown_map
downtown_map = folium.Map(location = folium_loc, zoom_start = 15)

# Draw our neighborhood: Urban Residents
folium.GeoJson(urban_polygon.geometry).add_to(downtown_map)

#auto_open('neighbourhood.html',downtown_map)

# Print the urban_art titles
print(urban_art.Title)

#Print the urban_art descriptions
print(urban_art.Description)

# Replace Nan and ' values in description
urban_art.Description.fillna('', inplace = True)
urban_art.Description = urban_art.Description.str.replace("'", "`")

#Print the urban_art descriptions again
print(urban_art.Description)

# Iterate through the urban_art and print each part of tuple returned
for row in urban_art.iterrows():
  print('first part: ', row[0])
  print('second part: ', row[1])


# Create a location and marker with each iteration for the downtown_map
for row in urban_art.iterrows():
    row_values = row[1]
    location = [row_values['Latitude'], row_values['Longitude']]
    popup = (str(row_values['Title'])).replace("'", "`")
    marker = folium.Marker(location = location, popup=popup)
    marker.add_to(downtown_map)

#print(urban_art.columns)

# Display the map
auto_open('downtownmap.html',downtown_map)
