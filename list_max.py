a=[]
size=int(input("enter nsizze of list"))
for i in range(size):
    val=int(input("Enter number:"))
    a.append(val)
max=a[0]
for i in range(size):
    if(a[i]>max):
        max=a[i]

min=a[0]
for i in range(size):
    if(a[i]<min):
        min=a[i]

print("Min number:",min,"Max number: ", max)
