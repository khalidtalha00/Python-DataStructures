def sumOfNums(n):
    assert n>=0 and int(n)==n,'Non integer and negetive nums are not allowed'  #constraint or unintensional case
    if n==0:  # base condition
        return 0
    else:
        return int(n%10)+sumOfNums(int(n/10))   # sum of digits of a num  is quotient + remainder when divided by 10
print(sumOfNums(10))
print(sumOfNums(1562))