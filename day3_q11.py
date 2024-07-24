#print the large number in the given list#
my_list=list(map(int,input().split()))
large_num=0
for i in range(0,len(my_list)):
    if(my_list[i]>large_num):
        large_num=my_list[i]
print(large_num) 
