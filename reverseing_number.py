#write a program to find the reverse of the given number.
n=int(input("Enter a number:"))
rev=0
while n!=0:
    r=n%10
    rev=(rev*10)+r
    n=n//10
print("reversing a number:",rev)
