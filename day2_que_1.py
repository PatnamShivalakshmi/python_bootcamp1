##check the number if positive and even if satisfies print positive even and do it for 
##positive-odd,negative even,negative-odd
n=int(input())
if(n>0 and n%2==0):
    print("positive-even")
elif(n>0 and n%2!=0):
    print("positive-odd")
elif(n<0) and((n%2)==0):
    print("negative-even")
else:
    print("negative-odd")
    
    