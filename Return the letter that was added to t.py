s = input("Enter string s: ")
t = input("Enter string t: ")

freq_s = {}
freq_t = {}

for char in s:
    freq_s[char] = freq_s.get(char, 0) + 1

for char in t:
    freq_t[char] = freq_t.get(char, 0) + 1

for char, count in freq_t.items():
    if char not in freq_s or count != freq_s[char]:
        print("The letter that was added to t is:", char)
        break
else:
    print("No difference found")
