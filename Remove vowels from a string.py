
string_input = input("Enter a string: ")

string_without_vowels = ''.join([char for char in string_input if char.lower() not in 'aeiou'])

print(f"The string without vowels is: {string_without_vowels}")
