n=int(input())
fact=0
for i in range(1,n+1):
    if(n==0 or n==1):
             return 1
else:
        return(n*fact(n+1))