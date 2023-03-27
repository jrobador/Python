"""
Solved with a function
"""

def fib(number):
    if (number == 0 or number == 1):
        return 1
    else:
        return fib(number-1) + fib(number-2)

print(fib(int(input())))

"""
Solved with Class
"""