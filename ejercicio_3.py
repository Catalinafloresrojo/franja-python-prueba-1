# Escribir un programa que haga transformaciones de pesos a dólares. 
# Debe preguntarle al usuario si desea transformar de pesos mexicanos a dólares,
# de pesos chilenos a dólares, o desde pesos argentinos a dólares. 
# Mostrar por pantalla la cantidad de monedas a convertir, la moneda que se convirtió y el monto en dólares.

#Peso Chileno a dólar: 855
#Peso Mexicano a dólar: 20
#Peso Argentino a dólar: 115
dinero = float (input("ingrese la cantidad de dinero que desea convertir: "))

transformador_de_pesos=float (input("¿quiere transformar su dinero de pesos a dolares?:"))
print(dinero*855)
   


print(input("¿Desea transformar el dinero de pesos mexicanos a dolares?:"))
print(dinero * 20)

pesos_mexicanos_a_dolares=int(dinero ** 20)


print(input("¿desea transformar el dinero desde pesos argentinos a dolares?"))
print(dinero*115)