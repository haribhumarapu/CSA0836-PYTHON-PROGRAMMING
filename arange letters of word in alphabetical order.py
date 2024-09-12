
word_input = input("Enter the word: ")

word_sorted = sorted(word_input.lower())

print(f"Alphabetical Order Normal: {' '.join(word_sorted)}")
print(f"Alphabetical Order Reverse: {' '.join(word_sorted[::-1])}")
