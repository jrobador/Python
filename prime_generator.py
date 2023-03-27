def isPrime(x):
    if x < 2:
        return False
    elif x == 2:
        return True  
    for n in range(2, x):
        if x % n ==0:
            return False
    return True

def primeGenerator(a, b):
    list = []
    for i in range(a,b):
        if (isPrime(i) == True):
            list.append(i)
    return list

    #primero saco los primos del numero maximo
    #segundo los filtro con los primos del numero minimo
f = int(input())
t = int(input())

print(list(primeGenerator(f, t)))