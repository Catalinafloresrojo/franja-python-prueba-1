#palindromo 

#escribir un programa que identifique
# si un palabra es palindromo o no 

#funcion principal main/run 
from pickle import TRUE


def palindromo(palabra):
    palabra = palabra.replace(" ", " ") #se eliminan los espacios 
    palabra = palabra.lower() #todo en minuscula 
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return TRUE 
    else:
        return False


def main():
    palabra = input("ingrese una frase: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo:
        print("es palindromo")
    else:
        print("no es palindromo ")
    
#punto de entrada
#buena practica
if __name__=="__main__": #punto de entrada. ejecutara el main
    main()
