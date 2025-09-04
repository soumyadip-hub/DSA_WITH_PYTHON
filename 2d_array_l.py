import numpy as np

# 2D array making simple
twoDarray = np.array(
    [[12, 23, 43, 45], [34, 22, 44, 65], [87, 98, 77, 99], [55, 44, 66, 33]]
)
print(twoDarray)

# adding row in 2D Array
newTwoDarray = np.insert(twoDarray, 0, [1, 2, 3, 4], axis=0)
print(newTwoDarray)

# adding row in last row in 2D Array
newTwoDarray = np.append(twoDarray, [[4, 5, 6, 7]], axis=0)
print(newTwoDarray)


# acess Element of 2D array
def acessElements(array, rowindex, colindex):
    if rowindex >= len(array) and colindex >= len(array[0]):
        print("incorrect index")
    else:
        print(array[rowindex][colindex])


acessElements(twoDarray, 2, 3)

# traversing Two Dimensional Array


def traverseTDarray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])


traverseTDarray(twoDarray)

# searching of two dimensional array


def searchTDarray(array, value):
    for i in range(len(array)):  # loop through rows
        for j in range(len(array[0])):  # loop through columns
            if array[i][j] == value:  # check if element matches
                return "The value is located at index (" + str(i) + ", " + str(j) + ")"
    return "The element is not found"


print(searchTDarray(twoDarray, 1))
print(searchTDarray(twoDarray, 44))
print(searchTDarray(twoDarray, 99))
print(searchTDarray(twoDarray, 55))

# deletion of 2D array

newTDarray = np.delete(twoDarray, 0, axis=0)
print(newTDarray)
