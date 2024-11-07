
from array import *

# 1. Create an array and traverse.
print("****Array Traversal****")
array1 = array('i',[12,4,56,1,1,1,1,8,9,0])
for i in array1:
    print(i)




# 2. Access individual elements through indexes
print("****Acessing Array element using index number****")
print(array1[2])


# 3. Append any value to the array using append() method
print("****Appending Values using append method****")
array1.append(100)
print(array1)


# 4. Insert value in an array using insert() method
print("****Inserting values using insert()****")
array1.insert(1,25)
print(array1)


# 5. Extend python array using extend() method
print("****Array Extend with extend() method****")
array2=array('i',[1,13,0,45,32])
array1.extend(array2)
print(array1)


# 6. Add items from list into array using fromlist() method
print("****Add items from list using fromList****")

myList = [1,2,3,14]
array1.fromlist(myList)
print(array1)


# 7. Remove any array element using remove() method

array1.remove(45)
print(array1)


# 8. Remove last array element using pop() method
print("****Removing last element using pop() method****")
array1.pop()
print(array1)


# 9. Fetch any element through its index using index() method
print("****Index method()****")
print(array1.index(12))


# 10. Reverse a python array using reverse() method
print("****Original Array****")
print(array1)
print("****Reversed Array****")
array1.reverse()
print(array1)

# 11. Get array buffer information through buffer_info() method
print("****Printing Buffer Information using buffer_info()")
print(array1.buffer_info())


# 12. Check for number of occurrences of an element using count() method
print(array1.count(1))

# 13. Convert array to string using tostring() method
# array1.tostring()
# print(array1)


# 14. Convert array to a python list with same elements using tolist() method
print("****Array to list****")
array1.tolist()
print(array1)

# print(my_array.tolist())
# 15. Append a string to char array using fromstring() method

# 16. Slice Elements from an array
print("****String Slicing****")
print(array1[0:5])





