# Find the given entered number is prime or not.
num =int(input("Enter number :- "))

prime = True
for i in range(2, num):
    if (num%i == 0):
        prime = False
        break
if prime :
    print("Numberr is prime")
else:
    print("Number is not prime")

















# Rohit Bhilare 23