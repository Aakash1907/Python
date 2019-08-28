#Python program to find the strong number using recursion 



def f(i):                   #factorial function
{
    if (i==1):
        return 1 
    else
        return i*f(i-1)
        
}
num=int(input("Enter the number here:"))
s=0
temp=num
while(num>0):
    dig=num%10
    s+=f(dig)             #function call to obtain the sum of the factorial of each digit of the given number
    num=int(num/10)
if (temp==s):
    {
        print("The number is a strong number");
    }
else:
    {
        print("It  is not a strong number")
    }
