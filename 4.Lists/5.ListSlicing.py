myList = ["a", "b", "c", "d", "e", "f"]
print(myList[0:2])
print(myList[:2])  # both same
print(myList[0:])
print(myList[:])  # both same

# to update first two elements--
myList[0:2] = ['x', 'y']
print(myList)
print(myList[0:-2])
