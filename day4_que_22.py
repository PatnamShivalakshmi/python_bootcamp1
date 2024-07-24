#GCD of two numbers
#ecludian algorithm
a=int(input("enter 1st num: "))
b=int(input(" enter 2nd num: "))
while b!=0:
    a,b=b,a%b
print("GCD of 2 numbers is: ",a)