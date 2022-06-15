#cadena de caracteres

from locale import normalize


nombre = input("¿cual es su nombre: ?")
nombre = nombre.upper() #upper para dejar las letras en mayuscula
print(nombre)

nombre = nombre.capitalize() #capitalize deja la primera letra con mayuscula 
print(nombre)

nombre = nombre.strip() #quita el espacio final del texto
print(nombre)

nombre = nombre.lower()# lower lleva todo a minuscula 
print(nombre)

nombre = nombre.replace("e", " ") #replace reemplaza letras 
print(nombre)

print(nombre[1]) #para recorrer cadena de textos

letra = nombre[2]
print(letra)

largo_cadena = len(nombre) #para saber el largo de la cadena de texto
print(largo_cadena)

largo_texto = len("franja")
print("franja  ")
print(largo_texto)

cadena_texto = "franja   "
cadena_texto = cadena_texto.strip()
print(len(cadena_texto))
