def fib(x):
  if x == 0 or x == 1:
    return 1
  else: 
    return fib(x-1) + fib(x-2)
print(fib(4))


"""
fib(4) -> return (fib (3) + fib(2)) = 3 + 2 = 5

fib(3) -> return (fib(2) + fib(1)) = 2 + 1 = 3

fib (2) -> return (fib(1) + fib(0)) = 1 + 1 = 2

fib(1) = 1
fib(0) = 1

"""