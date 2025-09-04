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
