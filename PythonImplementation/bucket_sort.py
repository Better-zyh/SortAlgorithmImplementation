def bucket_sort(arr):
    # Find maximum value in the array and calculate bucket size
    max_val = max(arr)
    bucket_size = max_val / len(arr)

    # Create empty buckets
    buckets = [[] for _ in range(len(arr))]

    # Add elements to the appropriate bucket
    for i in range(len(arr)):
        j = int(arr[i] / bucket_size)
        if j != len(arr):
            buckets[j].append(arr[i])
        else:
            buckets[len(arr) - 1].append(arr[i])

    # Sort each bucket and concatenate them
    sorted_arr = []
    for i in range(len(arr)):
        insertion_sort(buckets[i])
        sorted_arr += buckets[i]

    return sorted_arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Demo test
arr = [29, 25, 3, 49, 9, 37, 21, 43]
print("Unsorted array:", arr)
sorted_arr = bucket_sort(arr)
print("Sorted array:", sorted_arr)
