#mr x is trying to create a new password for his insta account these are the required conditions 
#for creating a new password.conditions:1.minimum length is 8 max is 15.2.only @,/ are allowed in a
#password.3.no spaces are allowed.4.only alpha nummerics are allowed.you are suppose to print weak
#if length is exact eight,medium:if length is b/w 8-12,strong:if length is b/w 12-15.

pw=input()
if(len(str)<8):
    print("please follow the below conditions")
elif(len(str)==8):
    print("weak")
elif((len(str)>8) and (len(str)<12)):
    print("moderate")
elif((len(str)>12) and (len(str)<15)):
    print("strong")
else:
    print("invalid")            
