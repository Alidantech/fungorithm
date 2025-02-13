def fun_sort(arr):
    if len(arr) == 0:
        return []

    arr_sorted = [arr[0]]  # Start with the first element

    # Loop through the array, keeping elements that maintain order
    for i in range(1, len(arr)):  # Start from index 1
        if arr[i] >= arr_sorted[-1]:  
            arr_sorted.append(arr[i])

    return arr_sorted

# Test case
print(fun_sort([3, 1, 4, 2, 5]))  # Output: [3, 4, 5]
