# logarithminc time
import math


def logFuc(n):
    if n==0:
        return "Done"
    n = math.floor(n / 2)
    print(n)
    return logFuc(n)

print(logFuc(8))


print()
def logn(n):
    while n > 1:
        n = math.floor(n/2)
        print(n)

print(logn(8))