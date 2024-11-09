import numpy as np
TwoDArray=np.array([[1,12,11,10],[11,23,43,55],[21,22,43,56],[76,87,65,0]])
print(TwoDArray)

def searchTwoDArray(array,value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if(array[i][j]==value):
                return 'Element is located at index ['+str(i)+"] ["+str(j)+"]"
    return "Element not found"

print(searchTwoDArray(TwoDArray,12))