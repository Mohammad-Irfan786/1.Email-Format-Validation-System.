import re

# Validation Codes
# 0 -> Invalid
# 1 -> Valid
# 2 -> Strongly Valid

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if not re.match(pattern, email):
        return 0
    
    username, domain = email.split("@")
    
    if len(username) < 3:
        return 1
    
    if len(username) >= 5 and domain.endswith((".com", ".edu", ".org", ".in")):
        return 2
    
    return 1


def get_result(code):
    if code == 0:
      
        return "invalid"
    elif code == 1:
        return "valid"
    else:
        return "strongly valid"


# Test Emails
emails = [
    "abc@gmail.com",
    "ab@gmail.com",
    "student@edu.in",
    "user123@yahoo.com",
    "wrongemail.com",
    "name@domain"
]

# Output
for email in emails:
    result = get_result(validate_email(email))
    print(f"The email address '{email}' is {result}.")
