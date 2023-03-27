def calc(x):
    perim = 4 * x
    area = x * x
    return perim, area
    

side = int(input())
p, a = calc(side)

print("Perimeter: " + str(p))
print("Area: " + str(a))