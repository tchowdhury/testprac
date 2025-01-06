import pandas as pd
import plotly.graph_objects as go


# Import MonthlySales data
monthly_sales = pd.read_csv('../data/monthly_sales.csv')
print(monthly_sales.head())

monthly_sales_dict = {'data' : [{'type': '', 'x': ['Jan', 'Feb', 'March'], 'y': [450, 475, 400]}],
'layout': {'title': {'text': ''}}}

# Examine the printed dictionary
#print(monthly_sales_dict)

# Update the type
monthly_sales_dict['data'][0]['type'] = 'bar'

# Update the title text
monthly_sales_dict['layout']['title']['text'] = 'Sales for Jan-Mar 2020'

# Create a figurecd
fig = go.Figure(monthly_sales_dict)

# Print it out!
fig.show()
