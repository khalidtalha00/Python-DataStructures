# wap to find a number from an array

import numpy as np
myArray=np.array([12,34,21,45,67,89,34,2,1,9])

def findNum(num,array):
    found=False
    for i in range(len(array)):
        if array[i]==num:
            print("Element at index:",i)
            found=True
    if found==False:
        print("Number not found")
findNum(21,myArray)
