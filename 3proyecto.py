#3. Pedir por teclado el País (siglas) y mostrar los nombres de su helipuerto y decir cual es su estado (abierto=1/cerrado=0).

import json
with open('airport.json') as data_file:    
	data = json.load(data_file)
pais=input("Introduce las siglas de un País: ")
for helipuerto in data:
	if helipuerto["iso"] == pais:
		if helipuerto["type"] == "heliport":
			print("Su nombre es: ", helipuerto["name"])
			print(" ")
			if helipuerto["status"] == 1:
				print("El helipuerto actualmente está abierto.")
			else:
				print("Este helipuerto está cerrado.")
			print("---------")
