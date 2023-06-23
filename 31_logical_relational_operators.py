# Operators : 1) Logical    2) Relational
#             1) Relational --> 1] ==  2] =>  3] <=
#             2) Logical--> 1> and  2> or  3> not


# [NOTE :- Please comment out another methods to understand the output of one method , Thank You]

age = int(input("Enter your age :- "))
# 1. and : if both conditions are true then it print output.
# This program is for finding employee ( Age :- 20+ and 30-)
if( age>30 and age>20):
    print("Your age is greater than 30 . Sorry !")
elif( age>= 20 and age <=30):
    print("Your age is perfect . Great !")
else:
    print("Your age is less than 20 . Sorry !")

# 2. or : if only one value is true then it print output.
balance = int(input("Please enter your balance :- "))
if( balance >= 20000 or balance <= 40000):
    print("Balance is greater than 20000")
else:
    print("Balance is less than 20000")


























# Rohit Bhilare 23