principal=int(input("Enter the Amount:"))
time=int(input("Enter the time period:"))
senior=input( "Enter 'y' if you are a senior,otherwise'n':" )
si=0
if senior=="y":
    si=principal*time*12/100
    print("Simple Intrest:",si)
else:
    si=pincipal*time*10/100
    print("Simple Intrest:",si)
