import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


# tips = sns.load_dataset('tips')
# print(tips.head())
# print(tips.columns)

# sns.set_style('ticks')
# sns.set_palette('RdBu')
# sns.set_context('talk')
# sns.catplot(data=tips, x="smoker", y="total_bill",  kind="point", hue="sex")
# plt.show()


#load the country csv file into a pandas dataframe
df = pd.read_csv('../countries-of-the-world.csv')
df = df.reset_index()  # make sure indexes pair with number of rows
print(df.dtypes)
print(df.head())
print(df.columns)

g = sns.catplot(data=df, x="Region", y="Birthrate",  kind="box")
g.fig.suptitle("Plot Title")
#g.set_titles("Plot Title", y=1.03)
g.set(xlabel="Region ho ho", ylabel="birthrate hi hi")
plt.xticks(rotation=90)
plt.yticks(rotation=0)
plt.show()
