n=int(input("Enter a number:")) 
a=1
sum=0
fact=1
for a in range (1,n+1,1):
    print(a)
    sum=sum+a
    fact=fact*a

print("sum :",sum)
print("Factorial :",fact)