# # ---TASK 1 calculate Average Temparature-------
# numdays = int(input("how many days's temprature you waant to count?\n"))
# total = 0
# for i in range(1, numdays + 1):
#     nextdays = int(input("day " + str(i) + "'s high temparature: "))
#     total += nextdays

# avg = round(total / numdays, 2)
# print("\naverage = " + str(avg))

# # question  -Missing number

# mylist = [
#     1,
#     2,
#     3,
#     4,
#     5,
#     6,
#     7,
#     8,
#     9,
#     10,
#     11,
#     12,
#     13,
#     14,
#     15,
#     16,
#     17,
#     18,
#     19,
#     20,
#     21,
#     22,
#     23,
#     24,
#     25,
#     26,
#     27,
#     28,
#     29,
#     30,
#     31,
#     32,
#     33,
#     34,
#     35,
#     36,
#     37,
#     38,
#     39,
#     40,
#     41,
#     42,
#     43,
#     44,
#     45,
#     46,
#     47,
#     48,
#     49,
#     50,
#     51,
#     52,
#     53,
#     54,
#     55,
#     56,
#     57,
#     58,
#     59,
#     60,
#     61,
#     62,
#     63,
#     64,
#     65,
#     66,
#     67,
#     68,
#     70,
#     71,
#     72,
#     73,
#     74,
#     75,
#     76,
#     77,
#     78,
#     79,
#     80,
#     81,
#     82,
#     83,
#     84,
#     85,
#     86,
#     87,
#     88,
#     89,
#     90,
#     91,
#     92,
#     93,
#     94,
#     95,
#     96,
#     97,
#     98,
#     99,
#     100,
# ]


# def findmissing(list, n):
#     sum1 = 100 * 101 / 2
#     sum2 = sum(list)
#     print(sum1 - sum2)


# findmissing(mylist, 100)


# # questions 2 - find pairs
# # write a program to  find all pairs of integers whose sum is equal to a given number
# def findpairs(nums, target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] == nums[j]:
#                 continue
#             elif nums[i] + nums[j] == target:
#                 print(i, j)


# mylist = [1, 2, 3, 2, 3, 4, 5, 6]
# findpairs(mylist, 6)

# # question 3 - how to check if an array contains a number in python
# import numpy as np

# myarray = np.array(
#     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# )


# def findnumber(array, number):
#     for i in range(len(array)):
#         if array[i] == number:
#             print(i)


# findnumber(myarray, 13)


# question 4 - permutations
def permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False


list1 = ["a", "c", "d"]
list2 = ["a", "c", "d"]

print(permutation(list1, list2))
