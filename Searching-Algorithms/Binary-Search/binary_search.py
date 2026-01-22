

def binary_search(n,arr):
    start_index = 0
    end_index = len(arr) - 1

    while start_index <= end_index:
        mid_point = (start_index + end_index) // 2

        if arr[mid_point] == n:
            return f"{n} found at index {mid_point}"
        elif arr[mid_point] < n:
            start_index = mid_point + 1
        elif arr[mid_point] > n:
            end_index = mid_point - 1

    return f"{n} not found"



print(binary_search(2,[1,2,3,4,5,6,7,8,9,10,11]))