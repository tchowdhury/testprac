# Import GeoPandas and Matplotlib
import geopandas
import matplotlib.pyplot as plt
from shapely.geometry import Point

# Read the mining site data
mining_sites = geopandas.read_file('../data/Mines/ipis_cod_mines.geojson')
# Read the national parks data
national_parks = geopandas.read_file("../data/Mines/cod_conservation/Conservation/RDC_aire_protegee_2013.shp")

# Print the first rows and the CRS information
print(mining_sites.head())
print(mining_sites.crs)

# Make a quick visualisation
mining_sites.plot()
plt.show()

# Print the first rows and the CRS information
print(national_parks.head())
print(national_parks.crs)

# Make a quick visualisation
national_parks.plot()
plt.show()

# Plot the natural parks and mining site data
ax = national_parks.plot()
mining_sites.plot(ax=ax, color='red')
plt.show()

# Convert both datasets to UTM projection
mining_sites_utm = mining_sites.to_crs(epsg=32735)
national_parks_utm = national_parks.to_crs(epsg=32735)

# Write converted data to a file
# mining_sites_utm.to_file('../data/Mines/ipis_cod_mines_utm.gpkg', driver='GPKG')
# national_parks_utm.to_file('../data/Mines/cod_conservation_utm.shp', driver='ESRI Shapefile')

# Plot the converted data again
ax = national_parks_utm.plot()
mining_sites_utm.plot(ax=ax, color='red')
plt.show()

# Read the new mining site data
mining_sites_new = geopandas.read_file('../data/Mines/ipis_cod_mines_utm.gpkg')
# Read the new national parks data
national_parks_new = geopandas.read_file("../data/Mines/cod_conservation_utm.shp")

# Plot of the parks and mining sites
ax = national_parks_new.plot(color='green')
mining_sites_new.plot(ax=ax, markersize=5, column='mineral', legend=True)
ax.set_axis_off()
plt.show()

#set the  city of Goma as shape point
goma = Point(746989.5594829298,9816380.942287602)

# goma is a Point
print(type(goma))

# Create a buffer of 50km around Goma
goma_buffer = goma.buffer(50000)

# The buffer is a polygon
print(type(goma_buffer))

# Check how many sites are located within the buffer
mask = mining_sites_new.within(goma_buffer)
print(mask.sum())

# Calculate the area of national park within the buffer
print(national_parks_new.intersection(goma_buffer).area.sum() / (1000**2))


# Extract the single polygon for the Kahuzi-Biega National park
kahuzi = national_parks_new[national_parks_new['NAME_AP'] == "Kahuzi-Biega National park"].geometry.squeeze()

# Take a subset of the mining sites located within Kahuzi
sites_kahuzi = mining_sites_new[mining_sites_new.geometry.within(kahuzi)]

print("sites_kahuzi data")
print(sites_kahuzi.head())

print(mining_sites_new.columns)
print(national_parks_new.columns)

# Determine in which national park a mining site is located
sites_within_park = geopandas.sjoin(mining_sites_new, national_parks_new[['NAME_AP','geometry']], predicate='within', how='inner')
print(sites_within_park.head())

# The number of mining sites in each national park
print(sites_within_park['NAME_AP'].value_counts())

# Get the geometry of the first row
single_mine = mining_sites_new.geometry[0]

# Define a function that returns the closest national park
def closest_national_park(geom, national_parks):
    # Calculate the distance from each national park to this mine
    dist = national_parks_new.distance(geom)

    # The index of the minimal distance
    idx = dist.idxmin()

    # Access the name of the corresponding national park
    closest_park = national_parks.loc[idx, 'NAME_AP']

    return closest_park

# Call the function on single_mine
print(closest_national_park(single_mine, national_parks_new))

# Apply the function to all mining sites
mining_sites_new['closest_park'] = mining_sites_new.geometry.apply(closest_national_park, national_parks=national_parks_new)
print(mining_sites_new.head())

#managing rater data
# Import the rasterio package
import rasterio

# Open the raster dataset
src = rasterio.open("central_africa_vegetation_map_foraf.tif")

# Import the plotting functionality of rasterio
import rasterio.plot

# Plot the raster layer with the mining sites
ax = rasterio.plot.show(src)
mining_sites.plot(ax=ax, markersize=1, color='red')
plt.show()

# Import the rasterstats package
import rasterstats

# Extract the nearest value in the raster for all mining sites
vegetation_raster = "central_africa_vegetation_map_foraf.tif"
mining_sites['vegetation'] = rasterstats.point_query(mining_sites.geometry, vegetation_raster, interpolate='nearest')
print(mining_sites.head())

# Replace numeric vegation types codes with description
mining_sites['vegetation'] = mining_sites['vegetation'].replace(vegetation_types)

# Make a plot indicating the vegetation type
mining_sites.plot(column='vegetation', legend=True)
plt.show()