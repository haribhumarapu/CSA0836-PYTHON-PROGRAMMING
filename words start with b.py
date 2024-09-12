str=str(input("Enter the string:"))
words=str.split()
count=0
for word in words:
    if word.startswith('B') or word.startswith ('b'):
        count+=1
        print(count)
