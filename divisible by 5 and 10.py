num=int(input("Enter a Number" "="))
if num%5==0:
    print(num,"is divisible by 5")
    if num%10==0:
        print(num,"is divisble by 10")
    else:
        print(num,"is not divisible by 10 ")
else:
    print(num,"is not divisble by 5")
