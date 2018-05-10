#1. Mostrar el nombre y el país de los seaplanes.

import json
with open('airport.json') as data_file:    
	data = json.load(data_file)

for aeropuerto in data:
	if aeropuerto["type"] == "seaplanes":
		print(aeropuerto['name'])
		print(aeropuerto['iso'])
		print("----------")
