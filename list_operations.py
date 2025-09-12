# Acessing and Traversing lists..

shoppinglist = ["milk", "cheese", "butter"]

print(shoppinglist)
print(shoppinglist[1])
print("butter")

print("butter" in shoppinglist)
for i in shoppinglist:
    print(i)

for i in range(len(shoppinglist)):
    shoppinglist[i] = shoppinglist[i] + "+"
    print(shoppinglist[i])

# update/insert list

mylist = [1, 2, 3, 4, 5, 6, 7]
print(mylist)
newlist = [69, 690, 6900, 6969]
mylist.insert(4, 11)
mylist.append(55)
mylist.extend(newlist)
print(mylist)
