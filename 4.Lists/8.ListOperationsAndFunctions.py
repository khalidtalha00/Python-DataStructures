#List Operations:

# + operator to concatenate two lists

a=[1,3,5]
b=[9,6,54,3]
c=a+b

print(c)

# * operator is used to repeat list elements

x=[0]
x=x*2
print(x)   # 0 will repeat two times

y=[0,1]
y=y*2
print(y)  # 0 and 1 will repeat two times


#List Functions = len(),max(),min(),sum() etc


mylist=[]
while (True):
    inp=input("Enter a number:")
    if inp=='done':
        break
    value=int(inp)
    mylist.append(value)
print(mylist)
print("Average:",sum(mylist)/len(mylist))