class Celular:
    def __init__(self,
                 marca,
                 modelo,
                 camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    def llamar(self):
        print("LLamando con: ", self.marca)

celular1 = Celular("Samsung","s23","48mp")
celular2 = Celular("iPhone", "15 Pro Max", "12MP")

print("El celular 1 es:", celular1.marca, celular1.modelo, celular1.camara)
print("El celular 2 es: ", celular2.marca, celular2.modelo, celular2.camara)

celular1.llamar()