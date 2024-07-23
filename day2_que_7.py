#take input from user if user enters 1 append,2 pop,3 sort,4 print good morning,5 length
my_list=[1,2,3,4,5,6]
print("enter ur choice:1.append() 2.pop() 3.sort() 4.print good morning 5.length()")
choice=int(input())
if(choice==1):
    my_list.append(12)
elif(choice==2):
    my_list.pop(1)
elif(choice==3):
    my_list.sort()
elif(choice==4):
    print("good mrng")
else:
    my_list.length()
print(*my_list)