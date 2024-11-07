from array import *

array1 = array('i', [1, 12, 34, 56, 7, 8, 59])


def searchInArray(arr, number):
    for i in arr:
        if i == number:
            return arr.index(number)
    return "Number not found"


print(searchInArray(array1, 12))
