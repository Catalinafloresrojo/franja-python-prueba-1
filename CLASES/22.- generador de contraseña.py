#generador de contraseña 

import random 

def generar_contrasena():
    mayusculas = [ 'A', 'B', 'C', 'D', 'E', 'F']
    minusculas = ['a', 'b', 'c' , 'd', 'e', 'f']
    numero = ['1', '2', '3','4','5', '6', '7','8','9','0']
    simbolos = ['#', '$', '%', '&', '/']

    caracteres = mayusculas +minusculas + numero + simbolos 
    contrasena = []

    for i in range(15): 
        caracter_aleatorio = random.choice(caracteres )
        contrasena.append(caracter_aleatorio)

    #convertir lista a string 
    # "" o ' simboliza un string vacio 
    # .join accedemos al metodo join 

    contrasena = 'hola'.join(contrasena) 

    contrasena = ''.join(contrasena) #juntara todo 

    return contrasena


def main (): 
    contraseña = generar_contrasena ()
    print ("Su contraseña es: " + contraseña)

if __name__ == '__main__':
    main()
