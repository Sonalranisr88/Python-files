# sum of natural numbers

n=int(input("Enter any value: "))
i=1
sum=0
while(i<=n):
    sum=sum+(i)
  
    # sum=i*i
    i=i+2
print(sum)
    
# digits sum

i=int(input("enter the value:"))
sum=0
while(i>0):
    sum=sum+i%10
    i=i//10
print(sum)