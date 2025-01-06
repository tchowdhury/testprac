import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

height = [62,64,69,75,68,66,65,71,76,73]
weight = [120,136,148,175,137,165,152,172,200,187]
gender = ['female','female','female','female','male','male','male','male','male','male']
# draw scatter plot
#sns.scatterplot(x=height, y=weight)
#plt.show()

# draw Countplot
#sns.countplot(x=gender)
#plt.show()

#load the country csv file into a pandas dataframe
df = pd.read_csv('../countries-of-the-world.csv')
df = df.reset_index()  # make sure indexes pair with number of rows
#print(df.dtypes)
#print(df.head())
#print(df.columns)
#print(df['Region'])


# Loop through the data frame and load the gdp, phone and percent_literate seperately into an array

gdp = []
phone =[]
percent_literate = []
region = []

for index, row in df.iterrows():
    region.append(row['Region'].strip())
    gdp.append(row['GDP ($ per capita)'])
    phone.append(float(str(row['Phones (per 1000)']).replace(",",".")))
    percent_literate.append(float(str(row['Literacy (%)']).replace(",",".")))

#print(region)
#print(gdp)
#print(phone)
#print(percent_literate)

# Create scatter plot with GDP on the x-axis and number of phones on the y-axis
#sns.scatterplot(x=gdp,y=phone)
#plt.show()

# Change this scatter plot to have percent literate on the y-axis
#sns.scatterplot(x=gdp, y=percent_literate)
# Show plot
#plt.show()

# Create count plot with region on the y-axis
#sns.set_theme(style="whitegrid")
#sns.set_color_codes("pastel")
#sns.countplot(x="Region", data=df, hue="Region")
# Show plot
#plt.show()

#tips = sns.load_dataset('tips')
#print(tips.head())

#hue_colors = {'Yes': 'black', 'No': 'green'}
#hue_colors = {'Yes': '#808080', 'No': '#00FF00'}
#sns.scatterplot(data=tips, x="total_bill", y="tip", hue="smoker", hue_order=["No","Yes"], palette=hue_colors)
#plt.show()

# load student dataset
df_student  = pd.read_csv('../student-alcohol-consumption.csv')
df_student = df_student.reset_index()  # make sure indexes pair with number of rows
print(df_student.head())
print(df_student.columns)

# Draw relationship between the number of absences they have in school and their final grade in the course, segmented by where the student lives (rural vs. urban area)
sns.scatterplot(data = df_student, x='absences' , y='G3', hue='location', hue_order=['Rural','Urban'])
plt.show()


# Create a dictionary mapping subgroup values to colors
palette_colors = {"Rural": "green", "Urban": "blue"}

# Create a count plot of school with location subgroups
sns.countplot(x="school",data=df_student, hue='location', palette=palette_colors)
plt.show()