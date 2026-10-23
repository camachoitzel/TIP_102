""" Recursion"""
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(6))

def mystery(n):
    if n == 0:
        return

    mystery(n - 1)
    print(n)

mystery(3)

def fibonacci(n):
    if n ==0:
        return 0

    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))