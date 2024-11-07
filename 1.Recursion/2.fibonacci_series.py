def fibonacci(n):
    assert n>=0 and int(n)==n,'Non integer and negetive nums are not allowed'
    if n in[0,1]:  # base condition
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

#print(fibonacci(-4))  # will print out the number in the fibonacci series  at index 4
prmpt = int(input("How many numbers fibonacci series do you want?:"))
for i in range(0,prmpt):
    print(fibonacci(i),end=" ")