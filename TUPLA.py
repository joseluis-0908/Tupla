#Tupla=("juan",13,10)
#convertir lista en tupla
Lista=list(Tupla)
print(Tupla)

#convierte la tupla en lista
Lista=["juan",13,10]
Tupla=tuple(Lista)
print("juan" in Tupla)

#contar los elementos de una tuupla
Lista=["juan",13,10,13]
Tupla=tuple(Lista)
#Len nos dice la longitud de la tupla
#print(len(Tupla))

#tupla unitaria
tupla=("juan",)
print(len (tupla))

#empaquetado y desempaquetado de tupla
tupla=("juan",13,1,1995)
nombre, dia, mes, año=tupla
print(nombre)
print(dia)
print(año)
print(mes)



 
