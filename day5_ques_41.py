n=int(input())
for i in range(0,n):
    for j in range(0,n):
        print("*",end="")
    print()
#another
n=int(input())
for i in range(0,n):
    for j in range(0,n):
        if(i==j):
             print(" ",end="")
        else:
             print("*",end="")
    print()