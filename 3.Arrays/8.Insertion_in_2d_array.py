import numpy as np

array1=np.array([[1,2,3],[4,5,6],[8,9,10]])
print(array1)
print("")
newArray=np.insert(array1,0,[[12,13,14]],axis=0) # adding 12,13,14 as a row at index of row 0
#newArray=np.insert(array1,1,[12,13,14],axis=0) # adding 12,13,14 as a row at index of row 1
#newArray=np.insert(array1,1,[12,13,14],axis=1) # adding 12,13,14 as a column at index of row 1
# here 0 is the row number and axis=0 means we are adding a new row at row no1
# if axis =1 it means we are adding a new column
# print(newArray)
#
new2DArray=np.append(array1,[[0,12,19]],axis=0)  # append() method adds the new array automaticalyy to the last index
print(new2DArray)
