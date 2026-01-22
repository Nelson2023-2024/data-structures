def ternary_search(target, arr):

    start_index,end_index = 0 , len(arr) -1

    while start_index <= end_index:
        #calculate midpoint by dividing the arr into 3 parts
        mid_point1 = start_index + (end_index - start_index) // 3
        mid_point2 = end_index - (end_index - start_index) //3

        # check if target is present in the 2 midpoint
        if target == arr[mid_point1]:
            return f"{target} found at index {mid_point1}"

        if target == arr[mid_point2]:
            return f"{target} found at index {mid_point2}"

        if target < arr[mid_point1]:
            end_index = mid_point1 - 1
        elif target > arr[mid_point2]:
            start_index = mid_point2 + 1
        else:
            start_index = mid_point1 + 1
            end_index = mid_point2 - 1

    return f"{target} not found"

print(ternary_search(9,[1,2,3,4,5,6,7,8,9]))
