# listas metodos 
#crear punto de entrada
def main (): 
    numeros = [1,3,5,7,8,9,0]
    print (type (numeros))
    print (numeros[4])

    objetos = ['hola' , 2, 4.5, True]
    print(objetos)

#agregar elementos
    objetos.append(False) #agregamos elementos
    print(objetos)

    objetos.append(45)
    objetos.append("hola mundo")
    print(objetos)

    #eliminar elementos 
    objetos.pop(0) #el numero es para eliminar de esa posicion
    print(objetos)

    objetos.pop() #elimina el ultimo objeto de la lista 
    print(objetos)

    #recorrer lista 
    for objeto in objetos:  #muestra todos los objetos de la lista 
        print(objeto)

    #ordenar lista
    print (objetos[::-1]) #da vuelta toda la lista
    
    #sumar listas
    numero_1 = [1,2,3]
    numero_2 = [4,5,6]
    lista_final = numero_1 + numero_2
    print(lista_final)

    #multiplicar listas
    print(numero_1 * 3) #la repite 3 veces 

    



if __name__ == '__main__':
    main()


