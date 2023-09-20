# from collections import Counter

# def char_in_substring(substring, string):
#     for char in string:
#         if char in substring:
#             return True
#     return False

# def is_unique(string):
#         if len(string) == len(Counter(string)):
#             return True
#         return False


def maxLength(A):
    dp = [set()]
    for a in A:
        if len(set(a)) < len(a):
            continue
        a = set(a)
        for c in dp[:]:
            print(a, c)
            print(a & c)
            if a & c:
                continue
            dp.append(a | c)
    return max(len(a) for a in dp)


print(maxLength(["qwert", "hjkl"]))
