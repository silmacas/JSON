#4. Pedir el continente por teclado y que me muestre el nombre y tipo de aeropuerto de los que sean de tamaño medio.(seaplanes, heliport, airport)


import json
with open('airport.json') as data_file:    
	data = json.load(data_file)
continente=input("Introduce las siglas de un continente: ")
for contin in data:
	if contin["continent"] == continente and contin["size"] == "medium":
		print("El tipo de aeropuerto es: ", contin["type"])
		print(" ")
		print("Su nombre es: ", contin["name"])
		print("-------------------------------")

