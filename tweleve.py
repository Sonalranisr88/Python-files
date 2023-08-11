# i=0
# while(i<50):
#     print(str(i))
#     i=i+1
# print("done")

# a=int(input("Enter a number:"))
# for i in range(11):
#     print(i*a)
 
# l1 = ["Harry","Sonal","Sachin","Rohan"]
# for i in l1:
#     if i.startswith("S"):
#         print("Hello "+ i)

num=int(input("Enter the number: "))
prime = True
for i in range(2,num):
    if(num%i == 0):
        prime = False
        break
if prime:
    print("This number is prime")
else:
    print("This is not a prime number")

# n=int(input("Enter number:"))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print("the sum is",sum)


# n=int(input("Enter the number:"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print("The factorial is:",fact)
n=int(input("enter numer:"))
for i in range(n):
    print("*"*(i+1))