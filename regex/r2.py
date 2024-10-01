#https://www.w3schools.com/python/python_regex.asp
#http://www.regex101.com

import re
#email validation

pattern=re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.-]+$')

def check(email):
 
    # pass the regular expression
    # and the string into the fullmatch() method
    if(pattern.fullmatch(email)):
        print("Valid Email")
 
    else:
        print("Invalid Email")
 
# Driver Code
if __name__ == '__main__':
 
    # Enter the email
    email = "swayam326@gmail.com"
 
    # calling run function
    check(email)
 