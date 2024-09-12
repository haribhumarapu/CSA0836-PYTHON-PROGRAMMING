strs = ["flower", "flow", "flight"]  
prefix = ""

if strs:
    for i in range(len(strs[0])):
        char = strs[0][i]
        if all(len(s) > i and s[i] == char for s in strs):
            prefix += char
        else:
            break

print(prefix) 
