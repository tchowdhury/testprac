import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

#load student dataset
# df_student  = pd.read_csv('../young-people-survey-responses.csv')
# df_student = df_student.reset_index()  # make sure indexes pair with number of rows
# print(df_student.head())
# print(df_student.columns)

# # Let's use a count plot to break down the number of survey responses in each category and then explore whether it changes based on age.
# sns.catplot(data=df_student, x='Internet usage', kind='count')
# plt.show()
#
# #Separate this plot into two side-by-side column subplots based on "Age Category", which separates respondents into those that are younger than 21 vs. 21 and older.
# sns.catplot(data=df_student, y='Internet usage', kind='count', col='Age')
# plt.show()
#
# #Use the survey_data DataFrame and sns.catplot() to create a bar plot with "Gender" on the x-axis and "Interested in Math" on the y-axis.
# sns.catplot(data=df_student, x='Gender', y='Mathematics', kind='bar')
# plt.show()

# load student dataset
# df_student  = pd.read_csv('../student-alcohol-consumption.csv')
# df_student = df_student.reset_index()  # make sure indexes pair with number of rows
# print(df_student.head())
# print(df_student.columns)
#
# #Use sns.catplot() to create a bar plot with "study_time" on the x-axis and final grade ("G3") on the y-axis, using the student_data DataFrame.
# # Rearrange the categories
# _ord = ["<2 hours","2 to 5 hours","5 to 10 hours",">10 hours"]
# sns.catplot(data=df_student, x='study_time', y='G3', kind='bar', order=_ord, ci=None)
# plt.show()

tips = sns.load_dataset('tips')
print(tips.head())
print(tips.columns)
#
# sns.catplot(data=tips, x="time", y="total_bill",  kind="box", order=['Dinner','Lunch'], whis=[0,100])
# plt.show()

#Use sns.catplot() and the student_data DataFrame to create a box plot with "study_time" on the x-axis and "G3" on the y-axis. Set the ordering of the categories to study_time_order.
# _ord = ["<2 hours", "2 to 5 hours", "5 to 10 hours", ">10 hours"]
# sns.catplot(data=df_student, x='study_time', y='G3', kind='box', order=_ord)
# plt.show()

sns.catplot(data=tips, x="smoker", y="total_bill",  kind="point")
plt.show()