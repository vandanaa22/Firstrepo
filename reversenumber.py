'''Write a program to find the reverse of the given nujmber'''
num=int(input("Enter a number "))
r=0
while num>0:
    rev=num%10
    r=(r*10)+rev
    num=num//10
print(r)
