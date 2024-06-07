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



estudiante = Estudiante(nombre, edad , grado)
exit = ""

while exit.lower() != "exit":
    #Ingresa por pantalla la accion
    accion = input("ingrese la accion: ")

    #.lower convierte lo que se ingresa por teclado a minuscula si o si.
    if(accion.lower() == "estudiar"): #Condicional para saber si esta estudiando!
        estudiante.estudiar()
    else:
        print(estudiante.nombre,"No esta estudiando!!!")

    exit = input("Digite Exit si desea terminar el programa: ")