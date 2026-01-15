"""
Reversing an array in-place exercise
In this exercise, you have to reverse a list in O(N) linear time complexity and we want the algorithm to be in-place as well - so the algorithm can not use additional memory (it means you have to manipulate the input list and not create an independent list)!

For example: input is [1,2,3,4,5] then the output is [5,4,3,2,1]

Good luck!
"""


def reverse_list(lst):
    # point to 1st element
    start_index = 0
    #point to last element
    end_index = len(lst) - 1



print(reverse_list([1,2,3,4,5,6,7,8,9]))