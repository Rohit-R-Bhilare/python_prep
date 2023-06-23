# Spam Detector : make a lot of money,buy now,click this,subscribe this if this text present in your 
text = input("Enter your text :- ")

if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("click this" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
else:
    spam = False

if(spam):
    print("This text is a spam !")
else:
    print("This text is not a spam !")





















# Rohit Bhilare 23