my_list=list(map(int,input().split()))
n=len(my_list)+1
k=sum(my_list)
sum=n*(n+1)//2
print(sum-k)