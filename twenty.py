# a=input("Enter String: ")
# b=a[-1::-1]
# if(a==b):
#     print("palindrome")
# else:
#     printso("not palindrome")

# print(b)

# n=int(input("Enter any value: "))
# i=1
# sum=0
# while(i<=n):
#     sum=sum+(i)
  
#     # sum=i*i
#     i=i+2
# print(sum)
    

i=int(input("enter the value:"))
sum=0
while(i>0):
    sum=sum+i%10
    i=i//10
print(sum)