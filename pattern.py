# ____*
# ___**
# __***
# _****
# *****
i=1
while i<=5:
    b=1
    while b<=5-i:
        print("_",end="")              
        b=b+1
    j=1
    while j<=i:
        print("*",end="")
        j=j+1
    print()
    i=i+1
# 1
# 22
# 333
# 4444
# 55555
i=1
while i<=5:
    j=1
    while j<=i:
        print(j,end="")
        j=j+1
    print()
    i=i+1
