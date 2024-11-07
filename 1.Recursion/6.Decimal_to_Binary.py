def Binary(n):
    assert  int(n)==n,"Number must be positive only!"
    if n==0:
        return 0
    else:
        return n%2 + 10*Binary(int(n/2))
print(Binary(10))