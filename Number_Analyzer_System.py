print("*** Number Analyzer System ***")
r=int(input("enter number to repeat loop : "))

for i in range(1,r+1):
    print("\nRound ",i)
    a=int(input("enter 1st number : "))
    b=int(input("enter 2nd number : "))
    c=int(input("enter 3rd number : "))
    print("Entered Numbers : ",a,b,c)
    if a>=b and a>=c:
        largest = a
    elif b>=a and b>=c :
        largest = b
    else:
        largest = c
    addition=a+b+c
    avg=round(addition/3,2)
    print("Largest number is :",largest)
    print("Sum of 3 numbers :",addition)
    print("Average :",avg)