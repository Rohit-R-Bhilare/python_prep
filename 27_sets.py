#  Set : Set of non repitative elements.
a = {1,2,3,4,5,1,2}  # Set a
print(type(a))       # Checking type of a
print(a)             # printing set a

# [NOTE :- Please comment out another methods to understand the output of one method , Thank You]

# Empty set
b = set() # this is not equal to  " b ={} "
print(type(b))

# Adding values to empty set
b.add(4)
b.add(5)
b.add(5)
b.add(6)
b.add(6) #Repitation not allowed or add
         # b.add((4,5,6)) Cannot add list or dictionary to sets
         # b.add({4:5})
print(b) # Empty set b with added values

# Removing value
b.remove(5) # Removale of 5
print(b)    # 5 removed

# Length of set
print(len(b)) # After removing 5 length of set becomes 2.

# Pop : remove a specific element
print(b.pop())
print(b)


















# Rohit Bhilare 23 