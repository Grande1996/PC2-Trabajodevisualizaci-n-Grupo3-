import json


#funcion para leer el archivo json 
def todoslospokemon():
    f = open('pokemon.json')
    return json.load(f)


#funciones necesarias para el ejercicio3
#que me permite encontrar el pokemon a traves del id
def pokemonporid(id):
    a=todoslospokemon()
    for pkmn in a:
        if pkmn["id"] == id:
           return pkmn    

#funcion para encontrar si un numero es primo
def numprimo(num):
   resultado=True
   if num>1:
    cont=0
    for i in range(2,num):
        resto= num % i 
        if resto==0:
            cont +=1
    if cont==0:
        resultado=True
    else:
        resultado=False
    return resultado

#funcion para encontrar las cordenadas de posición del pokemon con su id
def localización(id):
    pkmn=pokemonporid(id)
    coordx, coordy = [], []
    try:
        coordx = pkmn["coordx"]
        coordy = pkmn["coordy"]
    except:
        pass
    return coordx, coordy





primos=[]
primos2=[]
lista=[1,2,3,4,12,8,9,63,23,21]
for i in lista:
   if numprimo(i)==True:
       primos.append(i)
#print(primos)
