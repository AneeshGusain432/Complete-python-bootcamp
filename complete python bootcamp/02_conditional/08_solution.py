password = "aneesh8755"
# password_length = len(password)

if len(password) < 6:
    strength = "weak"
elif len(password) <= 10:
    strength = "Medium"
else:
    strength = "Strong"
    
print("password strength is:", strength)