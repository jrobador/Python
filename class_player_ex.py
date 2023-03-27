class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def intro(self):
        print(self.name + " (Level " + self.level + ")")

#your code goes here
nombre = input()
level = input()

Pl1 = Player(nombre,level)

Pl1.intro()