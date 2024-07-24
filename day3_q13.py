#replace the elements in an array with the average of maximum and minimum elements
a=list(map(int,input().split()))
avg=0
max=a[0]
for i in range(len(a)):
    if(max<a[i]):
        max=a[i]
min=a[0]
for i in range(len(a)):
    if(min>a[i]):
        min=a[i]
avg=(min+max)//2
print(avg)
for i in range(len(a)):
    a[i]=avg
print(a)
            