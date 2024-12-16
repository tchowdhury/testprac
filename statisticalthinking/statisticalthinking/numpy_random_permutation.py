from numpy import random
import numpy as np


# Randomly shuffle elements of following array:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(f'before shuffling array: {arr}')
random.shuffle(arr)
print(f'after shuffling array: {arr}')

#Generate a random permutation of elements of following array:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(f'before permutation array: {arr}')
x = random.permutation(arr)
print(f'after permutation array: {arr}')
print(f'permutated array: {x}')