#remove all the brackets from the given algegraic expression
exp=input()
for i in exp:
    if ord(i)==40 or ord(i)==41 or ord(i)==91 or ord(i)==93 or ord(i)==123 or ord(i)==125:
        pass
    else:
        print(i,end="")
print()
            