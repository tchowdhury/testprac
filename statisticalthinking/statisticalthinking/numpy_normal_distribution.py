from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#Generate a random normal distribution of size 2x3:
x = random.normal(size=(2,3))
print(x)
sns.lineplot(x)
plt.show()

#Generate a random normal distribution of size 2x3 with mean at 1 and standard deviation of 2:
y = random.normal(loc=1, scale=2, size=(2,3))
print(y)
sns.lineplot(y)
plt.show()

# generate n number of floting data uniformly distributed between two float number
ran_arr = random.uniform(size=96, low=5.5, high=16.7)
print(f'n number of uniformly distributed data betweeen ranges {ran_arr}')
sns.lineplot(ran_arr)
plt.show()