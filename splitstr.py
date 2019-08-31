
s=input("Enter the string")               #input paragraph
n=int(input("Enter the line length:"))    #taking the width from the user
l=list(s)                               
print(s)
for i in range(0,len(l),n):
    {
    print("".join(l[i:i+n]))
    }
