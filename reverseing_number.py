#write a program to find the reverse of the given number.
##n=int(input("Enter a number:"))
##rev=0
##while n!=0:
##    r=n%10
##    rev=(rev*10)+r
##    n=n//10
##print("reversing a number:",rev)
def reverse (num):
    rev=0
    while num>0:
        rev=rev*10+num%10
        num//=10
    return rev
def isPalindrome(num):
    return num==reverse(num)
print(reverse(123))
print(isPalindrome(123))
print(reverse(121))
print(isPalindrome(121))

