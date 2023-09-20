def minimumSwaps(arr):
    swaps = 0
    value_index = dict(zip(arr, range(1, len(arr) + 1)))
    for i in range(1, len(arr) + 1):
        if value_index[i] != i:
            value_index[arr[i - 1]] = value_index[i]
            arr[value_index[i] - 1] = arr[i - 1]
            swaps += 1
    return swaps
