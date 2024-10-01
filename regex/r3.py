#https://www.w3schools.com/python/python_regex.asp
#http://www.regex101.com

import re
#password validation
'''
At least 8 characters
Must be restricted to, though does not specifically require any of:
uppercase letters: A-Z
lowercase letters: a-z
numbers: 0-9
any of the special characters: @#$%^&+=
'''
pattern=re.compile(r'^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$')

def check(password):
 
    # pass the regular expression
    # and the string into the fullmatch() method
    if(pattern.fullmatch(password)):
        print("Valid Password")
 
    else:
        print("Invalid Password")
 
# Driver Code
if __name__ == '__main__':
 
    # Enter the email
    password = "3n04Jbk$aT"
 
    # calling run function
    check(password)
 