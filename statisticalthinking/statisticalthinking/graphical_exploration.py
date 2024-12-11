import pandas as pd
import matplotlib.pyplot as plt

df_swing = pd.read_csv('../2008_swing_states.csv')

#print(df_swing.head(5))
print(df_swing[['state', 'county','dem_share']])