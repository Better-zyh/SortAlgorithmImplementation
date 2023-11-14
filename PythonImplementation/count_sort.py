def count_sort(arr):
    # Find the maximum element in the array
    max_element = max(arr)

    # Create a count array to store count of each element
    count = [0] * (max_element + 1)

    # Store count of each element in the count array
    for i in range(len(arr)):
        count[arr[i]] += 1

    # Modify the count array to store the actual position of each element in the sorted array
    for i in range(1, max_element + 1):
        count[i] += count[i - 1]

    # Create a sorted array
    sorted_arr = [0] * len(arr)
    for i in range(len(arr)):
        sorted_arr[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    return sorted_arr

# Demo test
arr = [4, 2, 2, 8, 3, 3, 1]
print("Original array:", arr)
sorted_arr = count_sort(arr)
print("Sorted array:", sorted_arr)
