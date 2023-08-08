# Fibonacci series
# # num=int(input("Enter a number:"))
# # sum=0
# # n1,n2=0,1

# # if(num<=0):
# #     print("Enter number greater than zero")
# # else:
# #     for i in range(0,num):
# #         print(sum)
# #         n1=n2
# #         n2=sum
# #         sum=n1+n2

# prime or not
# # num=int(input("Enter a number:"))
# # if(num<=1):
# #     print("It is not a prime number.")
# # else:
# #     for i in range(2,num):
# #         if(num%i==0):
# #             print("It is not a prime numer.")
# #             break
# #     else:
# #         print("It is a prime number.")

# palindrome or not
# # num=input("Enter a number:")
# # a=num
# # b=0
# # b=(str(num[::-1]))
# # print("the reverse number is:",b)
# # if(a==b):
# #     print("It is a palindrome number.")
# # else:
# #     print("It is not a palindrome number")

# factorial of a number
# # num=int(input("Enter a number:"))

# # def fact(num):
# #     f=1
# #     if num==0 or num==1:
# #         return 1
# #     else:
# #         for i in range(1,num+1):
# #             f=f*i
# #         return f

# # a=fact(num)
# # print("the factorial of number is:",a)

# # #factorial of a number
# # num=int(input("Enter a number:"))

# # def fact(num):
# #     f=1
# #     if num==0 or num==1:
# #         return 1
# #     for i in range(1,num+1):
# #         f=f*i
# #     return f
# # a=fact(num)
# # print (a)

# reverse a string

# # num=input("enter any string:")
# # print("The original string is ",num)
# # b=0
# # b=(str(num[::-1]))
# # print("The reverse of a string is:",b)

# searching substring in a line
line="hello my name is sonal rani what about you?"
s="hello"

def searchstring(s):
    result= line.find(s)
    if result == -1:
        print("Line does not contain string")
    else:
        print("The substring is present in the index",result)

searchstring(s)