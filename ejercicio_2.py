#Escribir un programa que le pregunte al usuario una cantidad a invertir,
#el interés porcentual anual y el número de años, 
# y muestre por pantalla el capital obtenido en la inversión redondeado a dos decimales

inversion = float(input ("¿cuanto dinero quiere invertir?:"))
interes_porcentual_anual = float(input("¿cuanto interes desea anualmente?:"))
cantidad_de_anos = float(input("¿en cuantos años quiere su inversion?:"))

capital_obtenido = (inversion + ((interes_porcentual_anual/100) +1 ))**cantidad_de_anos
print("el capital obtenido es:")

print(round(capital_obtenido,2))

