from numpy import random

def random_intro():

    # Generate a random integer from 0 to 100:
    x = random.randint(100)
    print(f'Random integer generated between 0 and 100 is {x}')

    #Generate a random float from 0 to 1:
    x = random.rand()
    print(f'Random float number generated is {x}')

    #Generate a 1-D array containing 5 random integers from 0 to 100:
    x = random.randint(100, size=5)
    print(f'Random array of 5 integer generated is {x}')

    #Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:
    x = random.randint(100, size=(3,5))
    print(f'Random 2D-array of integer with size 3x5 generated is {x}')

    #Generate a 1-D array containing 5 random floats:
    x = random.rand(5)
    print(f'Random 1D array with float number generated is {x}')

    #Generate a 2-D array with 3 rows, each row containing 5 random numbers:
    x = random.rand(3,5)
    print(f'Random 2D array with float number generated is {x}')

    #Return one of the values in an array:
    x = random.choice([3,7,8,1])
    print(f'Random choice of an element from an array is {x}')

    #Generate a 2-D array that consists of the values in the array parameter (3, 5, 7, and 9):
    x = random.choice([3, 5, 7, 9], size=(3,5))
    print(f'Random choice of an element from an array with 2D output is {x}')

    # generate n number of floting data uniformly distributed between two float number
    ran_arr = random.uniform(size=96, low=5.5, high=16.7)
    print(f'n number of uniformly distributed data betweeen ranges {ran_arr}')

def main():
   random_intro()

if __name__== "__main__":
    main()
