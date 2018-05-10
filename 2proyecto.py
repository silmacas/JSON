#2. Contar los aeropuertos en el que su tamaño sea pequeño.
#2. contar el número de puertos de hidroaviones que hay.

import json
with open('airport.json') as data_file:    
	data = json.load(data_file)
contador=0
for aeropuerto in data:
	if aeropuerto["type"] == "airport" and aeropuerto["size"] == "small":
		contador=contador+1

print("Hay" , contador, "aeropuertos pequeños.")

"""
import json
with open('airport.json') as data_file:    
	data = json.load(data_file)
contador=0
for hidroavion in data:
	if hidroavion["type"] == "seaplanes":
		contador=contador+1
print("Hay", contador, "aeropuertos de hidroaviones.")
"""
