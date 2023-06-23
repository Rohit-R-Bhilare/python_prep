#  Syntax of the Dictionary :- 1) Unordered 2) Mutable 3) Indexed 4) Cannot contain duplicate keys. eg "Marks" :[1,2,3] / "Marks" : [4,5,6]

myDictionary = {
    "Fast" : "In a quick manner", # Comma is very important ","
    "Rohit" : "A Student",
    "newdictionary" : {'Rohit' : 'Youtuber'}, #another dictionary in main dictionary.
    "Marks" : [1,2,3,4,5]
}

print(myDictionary['Fast'])
print(myDictionary['Rohit'])   # main dictionary
print(myDictionary['Marks'])   # main dictionary

myDictionary['Marks']=[23,24]  # We can change the values in Dictionaries       
print(myDictionary['Marks'])   # Output of new marks
print(myDictionary['newdictionary']['Rohit'])  # Output of sub dictionary













# Rohit Bhilare 23