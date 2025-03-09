# Find Maximum product of two integers in an array where all elements are positive

import numpy as np
myArray=np.array([1,20,30,34,5,56,57,9,10,31,14,35,21,19])
def findMaxProduct(array):
    maxProduct=0
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i]*array[j]> maxProduct:
                maxProduct=array[i]*array[j]
                pairs=str(array[i])+","+str(array[j])
    print("Pairs:",pairs)
    print("Max Product:",maxProduct)
findMaxProduct(myArray)
