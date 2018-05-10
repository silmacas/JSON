#5. Una clasificación de los aeropuertos españoles en tamaño y mostrar su nombre.

import json
with open('airport.json') as data_file:    
	data = json.load(data_file)
listgrandes=[]
listmedianos=[]
listpequeños=[]
for aeropuerto in data:
	if aeropuerto["type"] == "airport" and aeropuerto["iso"] == "ES":
		if aeropuerto["size"] == "large" and aeropuerto["name"] is not None:
			listgrandes.append(aeropuerto["name"])
		if aeropuerto["size"] == "medium":
			listmedianos.append(aeropuerto["name"])
		if aeropuerto["size"] == "small":
			listpequeños.append(aeropuerto["name"])

print("Aeropuertos grandes.\n====================\n")
for nombre in listgrandes:
	print(nombre)

print("\nAeropuertos medianos.\n=================\n")
for nombre in listmedianos:
	if nombre is not None:
		print(nombre)
print("\nAeropuertos pequeños.\n====================\n")
for nombre in listpequeños:
	if nombre is not None:
		print(nombre)

