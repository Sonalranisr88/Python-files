i= int(input("enter number: "))
org=i
sum =0
while(i>0):
    sum= sum+(i%10)*(i%10)*(i%10)
    i=i//10
if org == sum:
    print("armstrong")
else:
    print("not armstrong")