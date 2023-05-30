s1=str(input("Enter the first string :-"))
s2=str(input("Enter the Second string :-"))
if(len(s1)>len(s2)):
    temp=len(s2)
else:
    temp=len(s1)
for i in range(0,temp):
    if s1[i]!=s2[i]:
       flag=0
    else:
        flag=1

if(flag==1):
    print("equal")
else:
    print("bilkul bi ni ho sakta baba")