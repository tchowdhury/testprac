import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

tips = sns.load_dataset('tips')
print(tips.head())
print(tips.columns)
#
# hue_colors = {'Yes': 'black', 'No': 'green'}
# hue_colors = {'Yes': '#808080', 'No': '#00FF00'}
# sns.relplot(data=tips, x="total_bill", y="tip", hue="smoker", hue_order=["No","Yes"],  kind="scatter", col="smoker",  row= "time")
# plt.show()
#
#
# sns.relplot(data=tips, x="total_bill", y="tip", hue="smoker", hue_order=["No","Yes"],  kind="scatter", col="day", col_wrap=4)
# plt.show()

# sns.relplot(data=tips, x="total_bill", y="tip", kind='scatter', size='size', hue='size')
# plt.show()
#
# sns.relplot(data=tips, x="total_bill", y="tip", kind='scatter', size='smoker', hue='smoker')
# plt.show()
#
# sns.relplot(data=tips, x="total_bill", y="tip", kind='scatter', alpha=0.6)
# plt.show()

# load student dataset
df_student  = pd.read_csv('../student-alcohol-consumption.csv')
df_student = df_student.reset_index()  # make sure indexes pair with number of rows
print(df_student.head())
print(df_student.columns)

# Draw relationship between the number of absences that a student has in school and their final grade in the course, creating separate subplots based on each student's weekly study time

# sns.relplot(data=df_student, x='absences', y='G3', kind="scatter",col='study_time')
# plt.show()
# sns.relplot(data=df_student, x='absences', y='G3', kind="scatter",row='study_time')
# plt.show()

# Let's try to control for these two factors by creating subplots based on whether the student received extra educational support from their school or family.
# sns.relplot(data=df_student, x='G1', y='G3', kind='scatter', col="schoolsup", col_order=["yes","no"], row='famsup', row_order=["yes","no"])
# plt.show()

mpg = sns.load_dataset('mpg')
print(mpg.head())
print(mpg.columns)

#What is the relationship between the power of a car's engine ("horsepower") and its fuel efficiency ("mpg")? And how does this relationship vary by the number of cylinders ("cylinders") the car has?

# sns.relplot(data = mpg, x="horsepower", y="mpg", hue="cylinders", kind="scatter", size="cylinders")
# plt.show()
#
# #relationship between how fast a car can accelerate ("acceleration") and its fuel efficiency ("mpg"). Do these properties vary by country of origin ("origin")?
#
# sns.relplot(data = mpg, x="acceleration", y="mpg", hue="origin", kind="scatter", size="origin")
# plt.show()

#How has the average miles per gallon achieved by these cars changed over time? Let's use line plots to find out!
sns.relplot(data = mpg, x="model_year", y="mpg",  kind="line")
plt.show()

# use a line plot to visualize how the distribution of miles per gallon has changed over time.
sns.relplot(data = mpg, x="model_year", y="mpg",  kind="line", ci="sd")
plt.show()

#Use relplot() and the mpg DataFrame to create a line plot with "model_year" on the x-axis and "horsepower" on the y-axis. Turn off the confidence intervals on the plot.
sns.relplot(data = mpg, x="model_year", y="horsepower",  kind="line", errorbar=None, hue="origin", markers=True, dashes=False)
plt.show()