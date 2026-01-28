'''Write a program to find the reverse of the given nujmber'''
def reverse(num):
   rev=0
   while num>0:
      rev=rev*10+num%10
      num//=10
   return rev
def isPalindrome(num):
   return num==reverse(num)
print(reverse(121))
print(isPalindrome((121)))


