def wave_sort(arr):
    arr.sort()  # Step 1: Sort the array
    
    # Step 2: Swap adjacent elements to create a wave pattern
    for i in range(0, len(arr) - 1, 2):  
        arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr

# Test it
print(wave_sort([3, 6, 5, 10, 7, 20]))  
# Expected Output: A wave-like sorted array
