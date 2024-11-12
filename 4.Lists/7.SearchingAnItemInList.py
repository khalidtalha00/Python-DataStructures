myList=[20,30,44,16,0,89,76]

# First Method--
def SearchInList(list,value):
    for num in list:
        if num==value:
            return list.index(value)
    return  "Element Not found"
print(SearchInList(myList,0))

def searchInList(list,value):
    for i in range(len(list)):
        if list [i]==value:
            return list.index(value)
    return  "Element not found"
print(searchInList(myList,440))
