def linear_search(n, arr):
    for i in range(len(arr)):
        if arr[i] == n:
            print(f"{n} found at index {i}")
            return i
    print(f"{n} not found")

    return None


print(linear_search(9999,list(range(1_000_000))))