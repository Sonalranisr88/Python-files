a=[]
size=int(input("enter size: "))
for i in range(size):
    val=int(input("numer: "))
    a.append(val)
i=0
j=size-1
while(i<j):
    t=a[i]
    a[i]=a[j]
    a[j]=t
    i=i+1
    j=j-1
print("list reversed=")
for i in range(size):
    print(a[i])