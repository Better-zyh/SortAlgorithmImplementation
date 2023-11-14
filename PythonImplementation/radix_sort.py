def radix_sort(arr):
    if not arr:
        return arr

    # Determine the maximum number of digits in the largest number
    max_digits = len(str(max(arr)))

    # Iterate over each digit from right to left
    for i in range(max_digits):
        # Create 10 buckets for each digit (0-9)
        buckets = [[] for _ in range(10)]

        # Place each number in the appropriate bucket based on its i-th digit
        for num in arr:
            digit = (num // 10 ** i) % 10
            buckets[digit].append(num)

        # Reconstruct the list by concatenating the buckets in order
        arr = []
        for bucket in buckets:
            arr.extend(bucket)

    return arr


# Demo test
if __name__ == '__main__':
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    sorted_arr = radix_sort(arr)
    print(sorted_arr)
