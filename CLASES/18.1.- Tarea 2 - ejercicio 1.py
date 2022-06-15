
def main():
    frase = input("Escriba una frase: ")
    letra_a_buscar = input("Escriba una letra: ")

    contador = 0
    for letra in frase: 
        if letra == letra_a_buscar:
            contador = contador + 1 
print("la letra " + letra_a_buscar + "aparece" + str(contador))

if __name__ == '__main__':
    main()
    