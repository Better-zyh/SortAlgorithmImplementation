def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Demo test
if __name__ == '__main__':
    arr = [5, 2, 4, 6, 1, 3]
    sorted_arr = insertion_sort(arr)
    print(sorted_arr)
