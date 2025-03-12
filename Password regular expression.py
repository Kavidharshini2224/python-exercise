import re


def validate_password(password):
   
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()_+]).{8,}$'
   
    if re.match(pattern, password):
        return True
    else:
        return False


passwords = [
    "Password123!",  
    "password",       
    "PASSWORD123!",  
    "Pass123",        
    "P@ssw0rd!",   
    "12345678",       
]


for password in passwords:
    if validate_password(password):
        print(f"'{password}' is a valid password.")
    else:
        print(f"'{password}' is an invalid password.")
