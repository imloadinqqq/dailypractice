import re
import sys

def validate(passwd):
    # password must be between 6 and 20 char, one lowercase, one uppercase, one digit, one special char
    reg = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    
    if re.fullmatch(reg, passwd):
        print("Password is valid.")
    else:
        print("Password is invalid.")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 validPassword.py '<password>'")
        sys.exit(1)
    
    password = sys.argv[1]
    validate(password)
