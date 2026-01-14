
def square(n):
    for i in range(n):
        for j in range(n):
            print(i,j)


square(10)



"""
*
**
***
****
*****

"""

def triangle(n):
    for i in range(n):
        for j in range(i + 1):
            print("*", end="")
        print()

triangle(5)


"""
********
********
********
********


"""

print()

def rectange(rows,columns):
    for i in range(rows):
        for j in range(columns):
            print("*", end="")
        print()

rectange(4,8)