# Importacion de los moudulos necesarios.
import time
import requests
import json
import os

# Clase para manejar los metodos solicitados.
class Contador:
    data = requests.get('https://api.disneyapi.dev/characters')
    datos = data.json()

    # Respuesta 1
    def contador_palabras(self):
        contador_palabra = 0
        for objeto in self.datos["data"]:
            for propiedad,valor in objeto.items():
                if type(valor) == str:
                    if str(valor).lower().count("princess"):
                        contador_palabra += 1
                elif type(valor) == list:
                    for elemento in valor:
                        if elemento.lower().count("princess"):
                            contador_palabra +=1

        return contador_palabra


    # Respuesta 2
    def contador_vocales(self):
        vocales = ["a","e","i","o","u"]
        palabras = ""
        contador_vocales = 0

        for objeto in self.datos["data"]:
            for propiedad,valor in objeto.items():
                if propiedad != "url" and propiedad != "imageUrl":
                    if type(valor) == str:
                            palabras += valor
                    elif type(valor) == list:
                        for elemento in valor:
                                palabras += elemento

        for vocal in vocales:
            for palabra in palabras:
                if palabra.count(vocal):
                        contador_vocales +=1 

        return contador_vocales



if __name__ == "__main__":
    # Manejamos el tiempo de ejecucion con esta variable.
    inicio = time.time()
    
    contador = Contador()
    
    data = {}
    data["data"] = []

    data["data"].append({
        "value":"princess",
        "count":contador.contador_palabras()
    })

    data["data"].append({
        "value":"a, e, i, o, u",
        "count":contador.contador_vocales()
    })

    fin = time.time()
    data["time"] = fin-inicio

    with open(os.path.dirname(os.path.abspath(__file__))+"/data.json", 'w') as file:
        json.dump(data, file, indent=4)