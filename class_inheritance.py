class Humano:
    def __init__(self, edad, altura, peso, nombre):
        print ("Buen día")
        self.edad   = edad
        self.altura = altura
        self.peso   = peso
        self.nombre = nombre

    def Saludo(self):
        print (f"Buenas tardes soy {self.nombre} y tengo {self.edad} años")

class Deportista:
    def entrenar(self, actividad):
        print (f"Hoy voy a {actividad}")

class Futbolista(Humano):
    def competir(self):
        print ("hoy hay fulbo")