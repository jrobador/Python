# A simple generator for Fibonacci Numbers
def fib(limit):
     
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1
 
    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b

# Iterating over the generator object using for
# in loop.
print("\nUsing for in loop")
for i in fib(10):
    print(i)

