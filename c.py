list=[]
n=int(input("Number of Names :"))
for a in range(n):
    list.append(input("Enter name :"))
for i in list:
    print(i)
list.append(input("Enter new name :"))
print("Printing new list....")
for i in list:
    print(i)
p=int(input("Enter Index number to update name :"))
list[p] =input("Enter name to update :")
print("Printing updated list....")
for i in list:
    print(i)
a=(input("Enter name to remove :"))
list.remove(a)
print("Printing current list....")
for i in list:
    print(i)
