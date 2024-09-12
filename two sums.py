nums = [2, 7, 11, 15]  # Example input
target = 9
result = []

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            result = [i, j]
            break
    if result:
        break

print(result)  # Output: [0, 1]
