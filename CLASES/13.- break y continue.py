# break y continue 

def main(): 
   #imprimir los numeros impares
    for contador in range(1 , 101):
        if contador % 2 == 0:
            continue
        print(contador)


texto = input("ingrese un texto: ")
for letra in texto:
    if letra == 'o':
        break
    print(letra)
    
if __name__ == '__main__':
    main()
 