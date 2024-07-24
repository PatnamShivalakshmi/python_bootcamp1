#given string is ABC and skip value is 4 then print EFG
str="ABC"
for i in str:
    print(chr(ord(i)+4),end="")
