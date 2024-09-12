
string_input = input("Enter the string: ")
char_input = input("Enter the character to be searched: ")

index = -1

for i in range(len(string_input)):
    if string_input[i] == char_input:
        index = i
        break

if index != -1:
    print(f"{char_input} is found in string at index: {index}")
else:
    print(f"{char_input} is not found in the string")
