password = input("Enter your new password: ")

result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True

result["digits"] = digit

upperCase = False
for i in password:
    if i.isupper():
        upperCase = True

result["upper-case"] = upperCase

print(result)
print(result.values())

if all(result.values()):
    print("Strong Password")
else:
    print("Weak password")

# In dictionaries, we have {'Key' : Value} Pairs represented as like this
# append function is not valid in dictionaries
