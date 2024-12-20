from numpy import random

# Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9. with respective probablity (0.1, 0.3,0.6 and 0)

x = random.choice([3,5,7,9], size=(100), p=[0.3, 0.3,0.3,0.1])
print(f'Generate a 1-D array with probablistic data {x}')


# Generate a 2-D array containing 100 values, where each value has to be 3, 5, 7 or 9. with respective probablity (0.1, 0.3,0.6 and 0)

x = random.choice([3,5,7,9], size=(3,5), p=[0.3, 0.3,0.3,0.1])
print(f'Generate a 2-D array with probablistic data {x}')