statement = "Modi Birthday @ September 17, #&$% is the wishes code for him."
special_chars = 0
for char in statement:
    if not char.isalnum() and not char.isspace():
        special_chars += 1
print("Number of special characters:", special_chars)
