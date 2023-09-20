"""
Min Moves to Obtain String Without 3 Identical Consecutive Letters
Given a string S containing N letters, 'a' and/or 'b', in one move,
you can swap one letter for another. 'a' for 'b' or 'b' for 'a'.
Write a function that , given S, returns the minimum number of moves 
required to obtain a string with no 3 consecutive letters
"""


def replace_item(a):
    if a == "a":
        a = "b"
    a = "b"
    return a


def min_moves(S):
    count = 0
    n = 0
    S = list(S)

    while n < len(S) - 2:
        if S[n] == S[n + 1] and S[n] == S[n + 2]:
            S[n + 2] = replace_item(S[n + 2])
            count += 1
            n += 3
        else:
            n += 1

    print(S)
    print(count)
    return count


min_moves("baaaaa")
min_moves("baaabbaabbba")
min_moves("baabab")
