import  numpy as np
array1=np.array([[12,13,11,12],[10,12,34,56],[12,45,32,78],[0,56,45,11]])
print(array1)
print()

newTwoDArray=np.delete(array1,0,axis=0)  # Removed first row
print(newTwoDArray)
print("Removing second row")
newTwoDArray=np.delete(array1,1,axis=0)  # Removed second row
print(newTwoDArray)

newTwoDArray=np.delete(array1,0,axis=1) # removed first column
print(newTwoDArray)
print("Removing Second Column")
newTwoDArray=np.delete(array1,1,axis=1)
print(newTwoDArray)
