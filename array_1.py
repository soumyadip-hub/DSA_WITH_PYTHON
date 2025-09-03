# array can store data of specified type
# elements of an array are located in a contigious
# each elements of an array has a unique index
# -------types of ARRAY----------
# ----1. one dimensional ArrayHaving been with a single index)
# ----2. Multi Dimensional Array
# ________---- [i]two dimensional Array(an array with a bnch of values having been declared with double index), [ii] three dimensional array,[iii]... n dimensional array
#
#
#

# arr = [1, 2, 3, 4, 5]
# arr.append(6)
# print(arr)
# ------------------------

# -----insertion of array--------

# arr = [1, 2, 3, 4, 5]
# arr.append(8)
# print(arr)

# arr.insert(2, 99)
# print(arr)

# ---------traversal array-------

# from array import array

# arr1 = array("i", [1, 2, 3, 4, 5, 6])
# arr2 = array("d", [1.2, 1.3, 1.4, 1.5])


# def traverseArray(array):
#     for i in array:
#         print(i)


# traverseArray(arr1)

# -------------acess array element----

# from array import *

# arr1 = array("i", [1, 2, 3, 4, 5, 6])


# def acessElement(array, index):
#     if index > len(array):
#         print("there is not an element")
#     else:
#         print(array[index])


# acessElement(arr1, 8)

# ------searching an elment in array-------

import array

my_array1 = array.array("i", [1, 2, 3, 4, 5])


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


print(linear_search(my_array1, 5))
