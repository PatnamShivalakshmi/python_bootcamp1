#check given number is prime or not
n=int(input())
r=n**0.5
cnt=0
if n==1: 
    print("not a prime number")
elif n==2:
    print("prime number")
for i in range(2,int(r+1)):
    if n%i==0:
        cnt+=1
        break
if cnt==0:
    print("prime number")
else:
    print("not prime")    