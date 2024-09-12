
n=int(input("enter the nth term:"))
n1,n2=0,1
count=0
if n<=0:
    print(" Please Enter a Postive integer")
elif n==1:
        print("Fibnacci series upto",n)
        print(n1)
else:
            print("Fibnacci Series")
            while count<n:
                print(n1)
                nth=n1+n2
                n1=n2
                n2=nth
                count+=1
