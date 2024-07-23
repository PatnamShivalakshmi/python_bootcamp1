##lists##
my_list=[1,2,3,4]
print(*my_list,end=" @")
# * is used to remove the braces#

my_list=[1,2,3,4]
my_list.append(999)
my_list.insert(8000,999)
print(*my_list)
##append inserts the element by default at last position,but insert asks for specific position##

my_list=[1,2,3,4]
#my_list.append(999)
#my_list.insert(8000,999)
my_list.pop()
print(*my_list)

my_list=[1,2,3,4]
#my_list.append(999)
#my_list.insert(8000,999)
my_list_2=[5,6,7,8]
new_list=my_list+my_list_2
print(*new_list)


my_list=[1,2,2,3,4]
#my_list.append(999)
#my_list.insert(8000,999)
#my_list_2=[5,6,7,8]
#new_list=my_list.copy()
#new_list.pop()
#print(*new_list)
cnt=my_list.count(2)
print(cnt)

my_list=[1,2,3,4]
my_list.append(999)
my_list.insert(8000,999)
#my_list_2=[5,6,7,8]
#new_list=my_list.copy()
#new_list.pop(77)
#print(*new_list)
#cnt=my_list.count(2)
my_list.sort()
print(*my_list)

my_list=[1,-2-13,41,28,2,4,9999]
#pop:it will default pop the last element#
my_list.pop(3)
print(*my_list)