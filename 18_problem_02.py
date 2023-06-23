#  Problem : Repalce data give in the letter with your data
#  Letter : Dear <|Name|>
            # You are selected !
            # Date : <|Date|>

letter = '''\nDear, <|Name|>
             You Are Selected ! For the role of Software Developer Engineer (SDE) in Google .
             Greeting From Google , 
             We all Happy To Tell you about selection.
             Date : <|Date|>
'''
name = input("Enter Your Name : ") # enter use name .
date = input("Enter Date : ") # enter date from user.
letter = letter.replace("<|Name|>",name) #replace <|Name|> with user name. 
letter = letter.replace("<|Date|>",date) # replace <|Date|> with new date.
print(letter) # this print all updated information in letter. 













# Rohit Bhilare 23