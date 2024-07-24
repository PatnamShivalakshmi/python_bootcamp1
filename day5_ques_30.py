#print all the vowels followed by consonants
vowels="aeiou"
consonants="bcdfghjklmnpqrstvwxyz"
a=" "
str="howareyou"
s=str.lower()
for i in s:
    if(i in vowels):
      a+=i

for i in s:
   if(i in consonants):
      a+=i
print(a)