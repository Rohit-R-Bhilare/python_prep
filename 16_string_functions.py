# 1 --> Length function : returns the length of the string .
data = "i am engineering student and now I am in First semester ." #sample data
print(len(data)) # we use len() to count the numbers of characters.

# 2 --> string.count() : count total numbers f occurance of any character
print(data.count("i")) # count occurance of I
print(data.count("a")) # count occurance of a
print(data.count("am")) # count occurance of am

# 3 --> string.endswith : This function check that the give string end with ....
print(data.endswith("semester .")) # my string ends with semester . , so it give True as a output

# 4 --> string.count : Check the Occurance of any character / data .
print(data.count("e")) # Occurance of "e" is given by this function.

# 5 ---> string.capitalize : Capitalize first letter of string .
print(data.capitalize()) # changes "i" to "I"

# 6 --> string.find : find string in the data (only first occurance). 
print(data.find("and")) # and is present , on 25 index.
# print(data.find("Rohit"))# Rohit is not present in the given data so it give -1 as a output.

# 7 --> string.replace : replace present string with new string.
print(data.replace("First","Second")) # replace first with second .




















# Rohit Bhilare 23