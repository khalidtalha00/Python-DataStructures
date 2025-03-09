import numpy as np

TwoDArray = np.array([[1, 12, 3], [12, 9, 87], [12, 32, 45], [12, 3, 43]])
print(TwoDArray)


# print(len(TwoDArray)) # length of the row
# print(len(TwoDArray[0]))  #this shows the length of  column of an array

def AccessTwoDArray(array, rowIndex, columnIndex):
    if (rowIndex >= len(array) or columnIndex >= len(array[0])):
        print("Wrong Index number")
    else:
        print(array[rowIndex, columnIndex])


AccessTwoDArray(TwoDArray, 2, 1)
