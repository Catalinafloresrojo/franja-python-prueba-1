#ejercicio 1
#escriba una funcion que aleatoriamente escoja un numero entero entre
# 1 y 10 que lo guarde en un fichero de nombre tabla-n.txt donde n es el numero 
# que salio.escribir en eñ archivo la tabla del numero.


import random 

def main (): 
    #rd.randint()
    numero_aleatorio = random.randint(1, 10)
    nombre_fichero = "./CLASES/archivos/tabla-" + str(numero_aleatorio) + ".txt"

    with open(nombre_fichero, 'w', encoding="utf-8") as file:
        for i in range (1, 13):
            linea = str(i) + "X" + str(numero_aleatorio) + " = " + str
            (numero_aleatorio * i)
            file.write(linea)
            file.write("\n")


if __name__ == "__main__":
    main()