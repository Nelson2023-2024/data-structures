"""
Integer reversion exercise
Your task is to design an efficient algorithm to reverse a given integer. For example if the input of the algorithm is 1234 then the output should be 4321.

NOTE: the input is an integer (and not a string) !!!

Good luck!
"""

def reverse_integer(num):
    num_str = str(num)[::-1]
    return int(num_str)

print(reverse_integer(123))

# SOLUTION 2