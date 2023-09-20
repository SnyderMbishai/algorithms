def find_missing_number(input):
    s1 = sum(input)
    n = len(input) + 1
    s2 = int(n * (n + 1) / 2)  # sum(range(0, n+1))
    return s2 - s1


print(find_missing_number([1, 2, 3, 4, 6]))
print(sum(range(0, 7)))
print(sum([1, 2, 3, 4, 6]))
