#Una panadería vende barras de pan a 3.49€ cada una.
#  El pan que no es el día tiene un descuento del 60%.
#  Escribe un programa que comience leyendo el número de barras vendidas que no son del día. 
# Después tu programa debe mostrar el precio habitual de una barra de pan,
#  el descuento que se le hace por no ser fresca y el coste final total.

barras_de_pan = int(input("cuantas barras de pan no son frescas:"))
precio_barras = 3.49
print(input("el precio habitual de las barras de pan es 3.49€"))
descuento_total = 0.6
print(input("se le hara un descuento de 60% por no ser fresca las barras de pan"))
precio_final_barras = (barras_de_pan * precio_barras * (1- descuento_total))

print(input("el precio final de la barra de pan es:"))
print(precio_final_barras)




