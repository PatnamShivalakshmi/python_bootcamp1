#if a number if palindrome or not
num=int(input())
reverse=int(str(num)[::-1])
if num==reverse:
    print("Palindrome")
else:
    print("not a palindrome")