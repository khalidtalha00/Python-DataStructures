myList = ["a", "b", "c", "d", "e", "f"]
print(myList)

myList.pop(1)
print(myList)  # deletes element at index 1

myList.pop()  # deletes the last element if index is not provided
print(myList)

del myList[0]
print(myList)

# remove() method-- the remove method takes the value of the element to be removed as a parameter instead of index of the element

myList.remove("c")
print(myList)
