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
def coordenadas(id):
    pkmn=pokemonporid(id)
    a,b=[],[]
    for x in pkmn:
        if  x==("coordx" or "coordy"):
            a=pkmn["coordx"]
            b=pkmn["coordy"]
        if x != ("coordx"or "coordy"):
           pass 
    return a , b
