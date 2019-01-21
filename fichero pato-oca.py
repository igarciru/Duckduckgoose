import random
lista=["Andrea","Vanesa","Tania","Nacho"]

def ocapato(lista,posicion):
    return(lista[posicion])

posicion=random.randrange(int(len(lista)))

print(ocapato(lista,posicion))
