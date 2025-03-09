# two lists are permutations of each other they have the same numbers or alphabets and equal lengths
def checkPermutation(list1,list2):
    if len(list1) != len(list2):
        return False
    else:
        list1.sort()
        list2.sort()
        if list1 == list2:
            return  True
        else:
            return False
listx=['c','a','t']
listy=['t','c','a']

print(checkPermutation(listx,listy))

lista=[1,2,3]
listb=[2,4,1]
print(checkPermutation(lista,listb))