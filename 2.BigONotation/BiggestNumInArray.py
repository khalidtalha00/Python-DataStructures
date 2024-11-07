def findBiggestNumber(sampleArray):
    biggestNum=sampleArray[0]   # O(1)
    for i in range(1,len(sampleArray)): # o(n)
        if sampleArray[i]>biggestNum:   #o(1)
            biggestNum=sampleArray[i] # O(1)
    print(biggestNum)  #O(1)
#total = O(n)
findBiggestNumber([2,4,5,1,17,99,0])
