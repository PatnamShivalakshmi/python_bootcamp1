#find the duplicate elements#
my_list=list(map(int,input().split()))
new=[]
#new.append(a[0])
#for i in a:
#     if(i not in new):
#         new.append(i)
#print(*new)
for i in my_list:
    if(i in new):
        new.append(i)
print(my_list[i])