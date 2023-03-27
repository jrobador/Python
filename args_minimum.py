def my_min(*args):
    for i in range(0, len(args)):
        if i == 0:
            minimo = args[0]
        else: 
            if args[i] < minimo:
                minimo = args[i]
    return minimo


print(my_min(8, 13, 4, 42, 120, 7,23,2,33,123,4213,41,2,17,37,-92,-22))