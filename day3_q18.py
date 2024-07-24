n=1234
even_sum=0
while(n>0):
    r=n%10
    if(r%2==0):
       even_sum=even_sum+r
    n=n//10
print(even_sum)