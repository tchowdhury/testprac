import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Import data
df = pd.read_csv('../schoolimprovement2010grants.csv')
df = df.reset_index()  # make sure indexes pair with number of rows
print(df.columns)
print(df.dtypes)
print(df.head())

df['Award_Amount'].plot.hist()
# fig, ax = plt.subplots()
# ax.hist(df['Award_Amount'])
plt.show()

