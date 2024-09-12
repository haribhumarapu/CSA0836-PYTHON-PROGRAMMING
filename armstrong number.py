num = int(input("Enter a number: "))
original_num = num
sum_of_cubes = 0

while num > 0:
    digit = num % 10
    sum_of_cubes += digit ** len(str(original_num))
    num //= 10

if sum_of_cubes == original_num:
    print(original_num, "is an Armstrong number")
else:
    print(original_num, "is not an Armstrong number")
