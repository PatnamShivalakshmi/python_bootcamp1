#********Peak element*********

my_list=list(map(int,input().split()))
cnt=0
for i in range(1,len(my_list)-1):#we are running the loop from 1 to avoid the range out of bound 
    if my_list[i]>my_list[i-1] and my_list[i]>my_list[i+1]:
        cnt+=i
        break
print(my_list[cnt])

#print all peak elements
my_list=list(map(int,input().split()))
cnt=0
for i in range(1,len(my_list)-1):#we are running the loop from 1 to avoid the range out of bound 
    if my_list[i]>my_list[i-1] and my_list[i]>my_list[i+1]:
        cnt+=i
        #print(my_list[i],end=" ")
if(my_list[-1]>my_list[-2] and my_list[-1]>cnt):
    cnt=len(my_list)-1
print(my_list[cnt])

