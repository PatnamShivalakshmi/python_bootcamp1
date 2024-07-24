#print the unique characters ina string
str="shivalakshmi"
count=0
a=""
for i in str:
    if(str.count(i)==1):
        a+=i
print(a)
        