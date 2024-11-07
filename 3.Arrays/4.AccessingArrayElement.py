# we can access an element of an array by its index number
def accessElement(array,index):
    if index>len(array):
        print("No element at this index")
    else:
        print(array[index])

from array import *
myArray1= array('i',[1,3,4,5,6,7,18])
accessElement(myArray1,3)

#accessElement(myArray1,7)  # array index out of range

accessElement(myArray1,8) # 8 > len(array)