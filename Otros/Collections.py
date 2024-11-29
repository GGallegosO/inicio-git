"""

Lista 

Una coleccion ordenada de elementos
cualquier tipo de dato puede ser un elemento
son mutables (pueden cambiar en cualquier momento del código)

"""
##########.      0.       1.        2

myfruitList = ["apple", "banana", "cherry"]
print(myfruitList)
print(type(myfruitList))

print(myfruitList[1])
print(myfruitList[2])
print(myfruitList[0])


myfruitList[2] = "melón"

print(myfruitList)

myfruitList.append("tomate")

print(myfruitList)


myfruitList.remove("banana")


print(myfruitList)


"""
Tupla
Es una coleccion inmutable de elementos

o sea que es una lsita que no puede cambiar

Acepta repetidos

se usa " ( ) " en vez de " [ ] "
 

"""

myFinalAnswerTuple = ("empana", "cazuela", "choripan")

print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])


"""
Diccionario

Ser una coleccion de elementos clave valor

clave : entero o string

valor : cualquier tipo de dato

"""

fondosRestart = {
    "mario" : "amarillo",
    "luna" : "naranja",
    "jorge" : "negro",
    "matias" : "blanco"
    
    
}

print(fondosRestart)
print(type(fondosRestart))

### traer fondo de alguien aprticular

print(fondosRestart["jorge"])

fondosRestart["gustavo"] = "verde"

print(fondosRestart)

