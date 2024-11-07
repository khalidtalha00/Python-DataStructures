def power(base,exponent):
    assert exponent >=0 and int(exponent)==exponent ,"Exponent cannot be negetive or decimal"
    if exponent==0:
        return 1
    if exponent ==1:
        return base
    else:
        return base*power(base,exponent-1)
print(power(5.6,4))
