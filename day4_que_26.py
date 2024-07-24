#*****leap year******
n=int(input())
if n%4==0 and n%100!=0:
    print("leap year")
else:
    print("not a leap year")

#leap year in agiven range
a,b=list(map(int,input().split()))
for i in range(a,b):
    if i%400==0 or i%4==0 and i%100!=0:
        print(i)

