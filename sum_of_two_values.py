def solution(n, arr):
    checked = []
    for i in arr:
        diff = n - i
        if diff in checked:
            return True
        checked.append(i)
    return False

print(solution(10, [5,7,1,2,8,4,3]))