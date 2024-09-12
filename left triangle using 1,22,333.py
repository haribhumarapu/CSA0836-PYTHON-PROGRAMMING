rows =int(input("Enter the number of rows:"))
for i in range(1, rows + 1):
    print(" ".join(str(i) for _ in range(i)))
