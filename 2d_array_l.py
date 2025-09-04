import numpy as np

# 2D array making simple
twoDarray = np.array([[12, 23, 43, 45], [34, 22, 44, 65], [87, 98, 77, 99]])
print(twoDarray)

# adding row in 2D Array
newTwoDarray = np.insert(twoDarray, 0, [1, 2, 3, 4], axis=0)
print(newTwoDarray)
# adding row in last row in 2D Array
newTwoDarray = np.append(twoDarray, [[4, 5, 6, 7]], axis=0)
print(newTwoDarray)
