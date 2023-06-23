# Marks from user (3 Subjects) if marks are less than 33 result fail . All over pecentage less than 40 then result fail
sub1 = int(input("Enter your first subject marks :- "))
sub2 = int(input("Enter your second subject marks :- "))
sub3 = int(input("Enter your third subject marks :- "))

if(sub1<33 or sub2<33 or sub3<33):
    print("You are fail")
elif((sub1+sub2+sub3)/3 < 40) :
    print("You are fail due to total percentage less than 40")
else:
    print("You Passed  !")




























# Rohit Bhilare 23