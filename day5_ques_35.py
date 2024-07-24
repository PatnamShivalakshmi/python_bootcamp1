#sum of digits of a number using ascii values
str=input()
sum=0
for i in str:
    if(ord(i)>47 and ord(i)<58):
        sum+=int(i)
print(sum)
