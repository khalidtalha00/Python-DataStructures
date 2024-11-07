def factorial(n):
    assert n >=1 and int(n)==n,'Number must be a positive  integer 0nly'  # so that user does not input negetive numbers
    if n in [0, 1]:   # base condition or termination condition
        return 1
    else:

        return n*factorial(n-1)


print(factorial(5))
#print(factorial(-2)) # will throw an assertion error