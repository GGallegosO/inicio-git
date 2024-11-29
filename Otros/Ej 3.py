#pide en consola al usuario

vocales = ["a", "e", "i", "o", "u"] 

palabra = input("ingrese palabra: ")
contador = 0

for letra in palabra:
    print(letra)
    if letra in vocales:
        contador += 1

    print(f"La palabra {palabra} tiene {contador} vocales")
