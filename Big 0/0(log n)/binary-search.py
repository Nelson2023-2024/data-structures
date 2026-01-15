lst = [1,2,3,4,5,6,7,8,9]

def binary_search(lst,taget):
    start_index = 0
    end_index = len(lst) - 1

    while start_index <= end_index:
        # we get the midpoint
        mid_point = (start_index + end_index) // 2

        if lst[mid_point] == taget:
            return f"{taget} found at index {mid_point}"
        elif lst[mid_point] < taget:
            start_index =mid_point + 1
        elif lst[mid_point] > taget:
            end_index = mid_point - 1

    return f"{taget} not found"
print(binary_search(lst, 9))
