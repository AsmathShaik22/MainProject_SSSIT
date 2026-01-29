num=int(input("Enter a number:"))
def isAdam(num):
  return square(num)==reverse(reverse(square(num)))
a=isAdam(12)
print("Adam number is:"a)
