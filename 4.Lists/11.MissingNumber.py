mylist=[1,2,3,4,6,7,8,9,10]
# sum of n natural numbers=n(n+1)/2
def findMissing(list,n):
    sum1=n*(n+1)/2
    sum2=sum(list)
    print(int(sum1-sum2))  # this will give the missing number
findMissing(mylist,10)