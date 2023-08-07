a=[]
size= int(input("How many elements you want to enter"))
for i in range(size):
    val = int(input("Enter number:"))
    a.append(val)
sum=0
for i in range(size):
    sum=sum+a[i]
print("Sum of List Elemts =", sum)