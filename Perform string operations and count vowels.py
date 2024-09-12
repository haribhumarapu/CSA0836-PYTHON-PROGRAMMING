S1 = 'welcome'
S2 = 'Homely'


S3 = S1 + S2


vowels = 'aeiou'
vowel_count = sum(1 for char in S3.lower() if char in vowels)

print(S3)
print(f"Vowels count in S3 = {vowel_count}")
