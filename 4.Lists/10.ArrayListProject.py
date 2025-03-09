# Find no. of days above average temperature
temps=[]
days=int(input("How many day's Temperature?:"))
i=1
while(i<=days):
    inpts=input(f"Day {i}'s high temperature:")
    values=int(inpts)
    temps.append(values)
    i=i+1;
print(temps)
avgTemp=sum(temps)/len(temps)
print("Average temp:",avgTemp)

abovetemp=0
for i in temps:
    if i>avgTemp:
        abovetemp+=1
print(abovetemp,"day(s) above average temperature")