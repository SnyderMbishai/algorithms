def fibonacci(n):
    if (n == 0):
        return 0
    if (n==1 or n == 2):
        return 1
    else:
        return (fibonacci(n-1)+fibonacci(n-2))

n = 5

for i in range(n):
    print(fibonacci(i))
