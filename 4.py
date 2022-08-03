a=int(input("Enter first number :"))
b=int(input("Enter second number :"))
c=int(input("Enter third number :"))

if a>b and a>c:
    print(a, "is a largest number")
elif b>a and b>c:
    print(b," is a alargest number")
else:
    print(c," is a largest number")