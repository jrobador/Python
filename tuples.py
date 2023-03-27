contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]

name = input()

for i in range (0,len(contacts)):
    if contacts[i][0] == name:
        print("{a} is {b}".format(a=name, b=contacts[i][1]))
        break
    else:
        if i == (len(contacts)-1):
            print ("Not Found")