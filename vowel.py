a=input("Enter a string")
vowel=0
cons=0
for i in range(0,len(a)):
    if(a[i]=="a" or a[i]=="e" or a[i]=="i" or a[i]=="o" or a[i]=="u" or
        a[i]=="A" or a[i]=="E" or a[i]=="I" or a[i]=="O" or a[i]=="U"):
        vowel = vowel+1
    else:
        cons= cons+1
print("Total vowels =", vowel)
print("Total cons= ",cons)