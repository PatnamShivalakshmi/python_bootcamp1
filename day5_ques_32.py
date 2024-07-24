#given input hello123 the output should be 6
str="hello12345678"
d="0123456789"
sum=0
for i in str:
    if i in d:
        sum+=int(i)
print(sum)
