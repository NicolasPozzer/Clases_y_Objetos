class Estudiante:
    def __init__(self,
                 nombre,
                 edad,
                 grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print(self.nombre,"Esta estudiando...")


nombre = input("Ingrese nombre: ")
edad = input("Ingrese edad: ")
grado = input("Ingrese el Grado: " )

accion = input("ingrese la accion: ")

nico = Estudiante(nombre, edad , grado)

#Condicional para saber si esta estudiando!
if(accion == "estudiar"):
    nico.estudiar()
else:
    print(nico.nombre,"No esta estudiando!!!")
