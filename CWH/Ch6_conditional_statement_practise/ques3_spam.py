text=input("Enter the text\n")
spam=False

if("make a lot money" in text):
    spam=True
elif("buy now" in text):
    spam=True
elif("click this" in text):
    spam=True        
elif("subcribe" in text):
    spam=True
else:
    spam=False   

if(spam==True):
    print("The given text is spam")
else:
    print("The given text is not spam")    
