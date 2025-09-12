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

# slice/delete  list

mylist = ["a", "b", "c", "d", "e", "f"]

print(mylist[0:2])
print(mylist[1:])
print(mylist.pop(2))
print(mylist)
del mylist[1]
print(mylist)
if "c" in mylist:
    mylist.remove("c")
print(mylist)

# searching for an element in list

mylist = [10, 20, 30, 40, 50, 60, 70, 80, 90]

target = 50
if target in mylist:
    print(f"{target} is in list")
else:
    print(f"{target} is not in the list")


# -----------linear search--------
def linear_search(p_list, p_target):
    for i, value in enumerate(p_list):
        if value == p_target:
            return i
    return -1


linear_search(mylist, target)

# -------list operation/functions---------
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
a = [0, 1]
a = a * 4
print(a)
d = [0, 12, 3, 34, 432, 3222, 940, 888]
print(min(d))
print(max(d))
print(len(d))
print(sum(a))
print(sum(d) / len(d))

# -----list vs Array------

import numpy as np

myarray = np.array([1, 2, 3, 4, 5, 6])
mylist = [1, 2, 3, 4, 5]

print(myarray / 2)
# print(mylist / 2)  list cant be divided

# --------list comprehension--------
prev_list = [1, 2, 3]
new_list = [i * 2 for i in prev_list]

print(prev_list)
print(new_list)

language = "python"
new_list = [letter for letter in language]
print(new_list)
