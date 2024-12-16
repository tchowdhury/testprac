import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

sns.lineplot([0, 1, 2, 3, 4, 5],linestyle='dotted', color='magenta', linewidth=5)
plt.show()

sns.histplot([0, 1, 2, 3, 4, 5], bins=10, color='green')
plt.show()

sns.displot([0, 1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14])
plt.show()

