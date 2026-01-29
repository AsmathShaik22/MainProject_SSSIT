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

print(reverse(123786))

print(reverse(123))

print(isPalindrome(123))
<<<<<<< HEAD
print(reverse(126))
print(isPalindrome(121))
=======
print(reverse(129))
print(isPalindrome(121))  
>>>>>>> 794dcaa8b3f6d6a3f409aa034f2c5e360b9b5fbd
print("=================================")
def getPalindromes(start,end):
    res=""
    for i in range(1,end+1):
        if isPalindrome(i):
            res=res+str(i)+","
    return res[:-1]+"."
print(getPalindromes(1,10000))

