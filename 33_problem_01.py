# Problem : Get input from user ( 4 numbers) , find greatest number
num1 =int(input("Enter your number 1:- "))
num2 =int(input("Enter your number 2:- "))
num3 =int(input("Enter your number 3:- "))
num4 =int(input("Enter your number 4:- "))

if(num1>num4):
    f1 = num1
else:
    f1 = num4

if(num2>num3):
    f2 = num2
else:
    f2 = num3

if(f1>f2):
    print(str(f1) + " is Greatest number.")
else:
    print(str(f2) + " is Greatest number.")



















# Rohit Bhilare 23