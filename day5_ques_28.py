#****STRINGS****
#string methods are : isalpha(),isnumeric(),isupper(),islower(),len(),isalum()
#swap case,converting to upper case,converting to lower case

str="hellaaaao woRld"
print(len(str))
print(str.isupper())
print(str.islower())
print(str.isalpha())
print(str.isalnum())
print(str.strip())
print(str.swapcase())
print(str.split('a'))#breaks at a
print(str.replace('a','z'))
print(str.capitalize())
print(str.title())

str="my name is shivalakshmi"
print(str.split('l'))

#isdigit
str="655793"
print(str.isnumeric())
print(str.isdigit())