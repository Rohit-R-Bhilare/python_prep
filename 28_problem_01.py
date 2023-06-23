# Problem 
myDict = {
    "Dost":"Friend",
    "Bhai":"Brother",
    "Behen":"Sister",
    "Kapda":"Cloth",
    "Bal":"Hairs"


}
print("Options are : ",myDict.keys())
a = input ("\nEnter your Hindi word :- ")
 
print("\nThe meaning of your word is : ",myDict.get(a))
#  we use  .get method to get None as output rather than error.(special cases)
























# Rohit Bhilare 23