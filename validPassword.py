import re

def validate(passwd):
    # password must be between 6 and 20 char, one lowercase, one uppercase, one digit, one special char
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    
    comp = re.compile(reg)
    
    search = re.search(comp, passwd)
    
    if search:
        print("Password is valid.")
    else:
        print("Password is invalid.")
    
validate('Johndoe1234&')