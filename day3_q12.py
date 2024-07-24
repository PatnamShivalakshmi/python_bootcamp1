#print the smallest number in the given list#
my_list=list(map(int,input().split()))
smallest_num=my_list[0]
for i in range(0,len(my_list)):
    if(my_list[i]<smallest_num):
        smallest_num=my_list[i]
print(smallest_num) 
