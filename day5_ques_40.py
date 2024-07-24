#input format is hello-----wor----ld
#output format is ----------hello world
str=input()
count=0
ans=""
for i in str:
    if(i=='-'):
        count+=1
    else:
        ans=ans+i    
print("-"*count+ans)