# Import pandas and matplotlib.pyplot using their customary aliases
import pandas as pd
import matplotlib.pyplot as plt

## Load the dataset
schools = pd.read_csv('../data/schools.csv')

print(schools.head())
#print(schools.columns)
#print(schools[['Latitude','Longitude','Mapped Location']])

# Plot the locations of all Nashville chicken permits
plt.scatter(x = schools.Longitude, y = schools.Latitude)

# Show the plot
plt.show()