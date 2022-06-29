#modulo random 

#import random as rd #se puede usar como rd 
import random 

def main (): 
    #rd.randint()
    numero_aleatorio = random.randint(1, 100)
    print(numero_aleatorio)

    lista_numeros = [ 1,2, 'hola', 4, True, 6 , 7]
    numero_aleatorio = random.choice(lista_numeros)  #escojera cualquier elemento de la lista
    print(numero_aleatorio)
    




if __name__ == '__main__':
    main()



