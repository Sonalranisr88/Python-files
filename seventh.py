name=input("Enter your name:")
date=input("Enter the date:")
letter=('''Dear <|name|>
you are Selected!
<|date|>''')
letter=letter.replace("<|name|>",name)
letter=letter.replace("<|date|>",date)
print(letter)