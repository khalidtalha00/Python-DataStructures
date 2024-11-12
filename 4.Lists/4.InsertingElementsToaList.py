myList = [1, 2, 3, 4, 5, 6, 7, 8]
print(myList)

myList[1] = 33
print(myList)

# insert method()
myList.insert(5, 101)
print(myList)

# append method()--append method adds items to the end of the list

myList.append(1)
print(myList)

# extend() method-- extend() method adds another list to a list
list1 = [11, 22, 33, 44, 55]
myList.extend(list1)
myList.extend(list1)
print(myList)
