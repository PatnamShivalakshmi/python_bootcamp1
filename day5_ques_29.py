#how many vowels are there in a string
str="RadhaKrishna"
cnt=0
vowels=['a','e','i','o','u']
for i in str:
    if i in vowels:
        cnt=cnt+1
print(cnt)

#consonants count
str="Beautiful"
s=str.lower()
cnt=0
vowels=['a','e','i','o','u']
for i in str:
    if i not in vowels:
        cnt=cnt+1
print(cnt)

#another method
vowel="aeiou"
consonents="abcdefghijklmnopqrstuvwxyz"
cnt=0
c=0
str="Beautiful"
s=str.lower()
for i in s:
    if(i in vowel):
        cnt+=1
for i in s:
    if(i in consonents):
        cnt+=1
print(cnt)