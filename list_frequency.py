a=[]
size=int(input("Enter the size of list: "))
for i in range(size):
    val=int(input("enter number: "))
    a.append(val)
key=int(input("Enter number of frequency: "))
count=0
for i in range(size):
    if(a[i]==key):
        count=count+1
print("Frequency",count)    
