"""
ciclo while

respite hasta que una condición 
sea True 

"""

contador = 1

while contador <= 10:
    print(contador)
    contador += 1
    
    
#actividad
"""    
estudiantes = []

opcion = input("Quiere continuar ? si o no ")

while opcion != "no":
    
    nombre = input("ingresa un estudiante: ")
    
    estudiantes.append(nombre)
    
    opcion = input("Quiere continuar ? si o no ")
    
print(estudiantes)
"""
estudiantes = []

while True:
    
    nombre = input("ingresa un estudiante: ")
    
    estudiantes.append(nombre)
    
    opcion = input("quieres continuar? si o no ")
    
    if opcion == "no":
        break


for estudiante in estudiantes:
    print("Hola", estudiante)