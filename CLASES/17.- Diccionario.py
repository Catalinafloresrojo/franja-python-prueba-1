#diccionarios

diccionario = {}

diccionario_capitales = {
    'chile ': 'santiago',   #lleva coma (,)
    'españa': 'madrid',
    'argentina' : 'mendoza'
}

print (diccionario_capitales['españa'].upper())
for pais, capital in diccionario_capitales.items():
    print(pais)