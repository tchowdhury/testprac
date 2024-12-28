import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import folium
import webbrowser

def auto_open(path, f_map):
    html_page = f'{path}'
    f_map.save(html_page)
    # open in browser.
    new = 2
    webbrowser.open(html_page, new=new)

# Read in the Council districts geojson file
council_districts = gpd.read_file('../data/council_districts/council_districts.geojson')

council_districts = council_districts.to_crs(epsg=3857)
sqm_to_sqkm = 10**6

# Create an area column in council_districts
council_districts['area'] = council_districts.geometry.area / sqm_to_sqkm
council_districts = council_districts.to_crs(epsg=4326)

#print(council_districts.crs)
print(council_districts.columns)

# Read in the public art csv file
permits = pd.read_csv('../data/building_permits_2017.csv')

# Create a geometry column in permits from lat and lng
permits['geometry'] = gpd.points_from_xy(permits.lng , permits.lat)
#print(permits.head())
print(permits.columns)

# Build a GeoDataFrame: permits_geo
permits_geo = gpd.GeoDataFrame(permits, crs = council_districts.crs, geometry = permits.geometry)

print(f'crs for Permit = {permits_geo.crs}, crs for council_districts = {council_districts.crs}')

# Spatial join of permits_geo and council_districts
permits_by_district = gpd.sjoin(permits_geo, council_districts, predicate = 'within')
print(permits_by_district.head(2))

# Create permit_counts
permit_counts = permits_by_district.groupby(['district']).size()
print(permit_counts)

# Convert permit_counts to a DataFrame
permits_df = permit_counts.to_frame()
# Reset index and column names
permits_df.reset_index(inplace=True)
permits_df.columns = ['district', 'bldg_permits']
print(permits_df.head(2))

# Merge council_districts and permits_df:
districts_and_permits = pd.merge(council_districts, permits_df, on = 'district')
print(districts_and_permits.head(2))

# Print the type of districts_and_permits
print(type(districts_and_permits))
print(districts_and_permits.columns)

# Create permit_density column in districts_and_permits
districts_and_permits['permit_density'] = districts_and_permits.apply(lambda row: row.bldg_permits / row.area, axis = 1)

# Print the head of districts_and_permits
print(districts_and_permits.head())

# Simple plot of building permit_density
districts_and_permits.plot(column = 'permit_density', legend = True)
plt.show()


# Polished choropleth of building permit_density
districts_and_permits.plot(column = 'permit_density', cmap = 'BuGn', edgecolor  = 'black', legend = True)
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.xticks(rotation = 'vertical')
plt.title('2017 Building Project Density by Council District')
plt.show()


# Center point for Nashville
nashville = [36.1636,-86.7823]


#print(districts_and_permits['center'])

# Create map
m = folium.Map(location=nashville, zoom_start=10)

folium.Choropleth(
    geo_data=districts_and_permits,
    name='geometry',
    data=districts_and_permits,
    columns=['district', 'permit_density'],
    key_on='feature.properties.district',
    fill_color='Reds',
    fill_opacity=0.5,
    line_opacity=1.0,
    legend_name='2017 Permitted Building Projects per km squared'
).add_to(m)


# Create LayerControl and add it to the map
folium.LayerControl().add_to(m)

# Create center column for the centroid of each district
districts_and_permits['center'] = districts_and_permits.geometry.centroid


# # Build markers and popups
for row in districts_and_permits.iterrows():
    row_values = row[1]
    center_point = row_values['center']
    location = [center_point.y, center_point.x]
    popup = ('Council District: ' + str(row_values['district']) +
             ';  ' + 'permits issued: ' + str(row_values['bldg_permits']))
    marker = folium.Marker(location = location, popup = popup)
    marker.add_to(m)

# Display the map
auto_open('choropleth.html',m)