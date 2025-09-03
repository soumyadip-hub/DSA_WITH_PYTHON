from array import *

# 1. create an array and traverse.
my_array = array("i", [1, 2, 3, 4, 5])

for i in my_array:
    print(i)

# 2.acess individual elements through indexes
print("step 2")
print(my_array[0])
print(my_array[2])
print(my_array[3])

# 3.Append any value to the array using append() method
print("step 3")
my_array.append(6)
print(my_array)

# 4.Insert value in an array using extend() method
print("step 4")
my_array.insert(0, 11)
print(my_array)

# 5.extend python array element using extend() method
print("step5")
my_array1 = array("i", [10, 11, 12])
my_array.extend(my_array1)
print(my_array)

# 6.add items from list into array using fromlist() method
print("step 6")
templist = [20, 21, 22]
my_array.fromlist(templist)
print(my_array)

# 7.Remove any array element using remove() method
print("step 7")
my_array.remove(11)
print(my_array)

# 8.remove last array element using pop() method
print("step 7")
my_array.pop()
print(my_array)

# 9.fetch any elements through its index using index() method
print("step 9")
print(my_array.index(21))

# 10.Reverse a python array using reverse() method
print("step 10")
my_array.reverse()
print(my_array)

# 11.get array buffer information  through buffer_info() method
print("step 11")
print(my_array.buffer_info)
# 12.chech for number of occurance of an element using count() method
print("step 12")
my_array.append(11)
print(my_array.count(11))
print(my_array)

# 13.covert array to bytes using tobytes() method
print("step 13")
strtemp = my_array.tobytes()
print(strtemp)
ints = array("i")
ints.frombytes(strtemp)
print(ints)
# 14.convert array to a python list with same element  using tolist() method
print("step 14")
print(my_array.tolist())
# 15.append a string to char array using fromstring() method
# 16.slice element from an array
print("step 16")
print(my_array[:])
