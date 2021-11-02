def sum_list(lst):
    if len(lst)==1:
        return lst[0]
    else:
        return lst[0] + sum_list(lst[1:])

print(sum_list([1,2,3,4]))

def fibonacci(n):
    if n >= 3:
        return (fibonacci(n-1) + fibonacci(n-2))
    return 1

print(fibonacci(6))

def sum_digits(n):
    if n == 0:
        return 0
    return n%10 + sum_digits((n//10))

print(sum_digits(55))