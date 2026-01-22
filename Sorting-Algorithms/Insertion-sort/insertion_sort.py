def insertion_sort(arr):
    for i in range(1,len(arr)):
        temp = i
        j = i - 1

        while temp < arr[j] and j > -1:
            arr[j+1] = arr[j]
            arr[j] = temp
            j -=1

    return arr


print(insertion_sort([2,1,4,6,3,67,99]))
