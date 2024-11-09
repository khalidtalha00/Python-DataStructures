import numpy as np
TwoDArray=np.array([[1,12,11,10],[11,23,43,55],[21,22,43,56],[76,87,65,12]])
print(TwoDArray)

def TraverseTwoDArray(array):
    for i in range(len(array)) :# row
        for j in range(len(array[0])): # column
            print(array[i][j])

TraverseTwoDArray(TwoDArray)
