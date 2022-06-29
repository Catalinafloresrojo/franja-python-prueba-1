#




# como importar numpy en el codigo 
#import numpy as np 

import numpy as np 

def main ():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print (lista)

    #crear un arreglo
    arreglo = np.array(lista)
    print(arreglo)
    print(type (arreglo))

    #crear arrglo de 2 dimensiones 
    matriz = np.array ([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(matriz)

    #indexacion de arreglo 
    print(arreglo[0])
    print(arreglo[0] + arreglo[1])

    #indexacion matrices 
    print(matriz[0])
    print(matriz[0,0])
    print(matriz[0,1] + matriz[0,0])
    
    print(arreglo[0:3])

if __name__ == '__main__':
    main()
