myDictionary = {
    "Fast" : "In a quick manner", # Comma is very important ","
    "Rohit" : "A Student",
    "newdictionary" : {'Rohit' : 'Youtuber'}, #another dictionary in main dictionary.
    "Marks" : [1,2,3,4,5]
}

# [NOTE :- Please comment out another methods to understand the output of one method , Thank You]

# Method :  .keys
print(list(myDictionary.keys())) # print the keys in the dictionary.

# Method 1 :  .values
print(myDictionary.values()) # print the values in the dictionary.

# Method 2 :  .items
print(myDictionary.items()) # print the items( keys,value ) in the dictionary.

# Method 3 : Update
UpdateDict = {
    "Lovish" : "Friend",
    "Darshan" : "Best Friend"
}
myDictionary.update(UpdateDict) # Update the dictionary by adding the key-values 

print(myDictionary)

#  Method 4 : .get --> It gives the values of keys and if not present in the Dictionary we get None as output.
print(myDictionary.get("Rohit")) # present in dictionary
print(myDictionary.get("Ovi")) # absent in dictionary 



















# Rohit Bhilare 23