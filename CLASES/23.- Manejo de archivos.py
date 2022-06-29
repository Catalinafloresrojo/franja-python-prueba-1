# manejo de archivos

#with: manejador contextual. si el programa se cierra inesperadamente,
#  evita que se corrompa el archivo

#modos de apertura 
# r solo lectura 
# r+ lectura y escritura 
# w solo escritura. sobrescribe el archivo si existe, lo crea si no existe 
# w+ escritura y lectura. sobrescribe el archivo si existe, lo crea si no existe 
# a Añadido (agrega contenido). crea el archivo si no existe
# a+ Añadido (agrega contenido) y lectura. Crea el archivo si np existe 

def leer (): 
    numeros = []
    with open('./archivos/numeros.txt', 'r') as file: 
        for linea in file: 
            numeros.append(int(linea))
            
    print (numeros)    


def escribir ():
    nombres = ['catalina' , 'andrea', 'pedro', 'david','rocio']
    with open('./CLASES/archivos/nombres.txt', 'a', encoding="utf-8") as file: #as file para abrir archivos
        for nombre in nombres: 
            file.write(nombre)
            file.write("\n")

        
def main():
    escribir()


if __name__ == '__main__':
    main()
