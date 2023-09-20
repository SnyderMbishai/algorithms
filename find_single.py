def crude_solution(arr):
    key_count = {}
    for i in arr:
        if i in key_count.keys():
            key_count[i] += 1
        else:
            key_count[i] = 1
    for item in key_count.keys():
        if key_count[item] < 2:
            return item


def crude_solution2(arr):
    checked = []
    for i in arr:
        if i not in checked:
            if arr.count(i) < 2:
                return i
            else:
                checked.append(i)


def solution(arr):
    n = len(arr)
    res = arr[0]
    for i in range(1, n):
        res = res ^ arr[i]
    return res


# Hashing - better solution O(n) complexity but takes more storage
print(crude_solution([1, 1, 2, 2, 3]))
# O(n2)
print(crude_solution2([1, 1, 2, 2, 3]))
# XOR - exclusive or
# if the bits are the same, result is zero, 0
# XOR of a number with 0 is number itself
print(solution([1, 1, 2, 2, 3]))
