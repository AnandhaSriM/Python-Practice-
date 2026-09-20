# Password Strength Checker
password = input("Enter your password: ")
length = len(password)
upper = 0
lower = 0
digit = 0
special = 0
for c in password:
    if c.isupper():
        upper = 1
    elif c.islower():
        lower = 1
    elif c.isdigit():
        digit = 1
    else:
        special = 1
score = upper + lower + digit + special
if length < 8:
    print("Password Strength: Weak")
elif score < 4:
    print("Password Strength: Moderate")
else:
    print("Password Strength: Strong")# Python-Practice-
My Python practice programs and learning exercises.
