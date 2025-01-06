import plotly.express as px
import pandas as pd


# Import penguine data
penguins = pd.read_csv('../data/penguins.csv')
print(penguins.head())
print(penguins.columns)

fig1 = px.histogram(data_frame=penguins, x='Body Mass (g)',nbins=10)
fig1.show(renderer='browser')

fig = px.box(data_frame=penguins,y="Flipper Length (mm)", facet_col="Species", hover_data=['Body Mass (g)','Region'])
fig.show(renderer='browser')
