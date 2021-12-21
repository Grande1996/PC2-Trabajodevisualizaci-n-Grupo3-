import matplotlib
import matplotlib.pyplot as plt
import json
from funciones import  todoslospokemon,numprimo,coordenadas


#funcion del ejercicio 1
def ejercicio1():
    pokemons={}
    a=todoslospokemon()
    #iteramos con el bucle for en el archivo json 
    for x in a:
        for  y in x["weaknesses"]:# bucle para encontrar todos los tipos de debilidades
            #print(y)
            
            # usando estas codiciónales podemos crear las llaves y los valores
            if y not in pokemons:
                pokemons[y]=1 #si llave  y (que puede ser cualquier tipo de pokemon) esta en el diccionario pokemons se le asigna a su
                            # valor una cantidad de 1
            else:
                pokemons[y] +=1# pero si se encuentra la llave se le suma un cantidad de 1 al valor 
    print(pokemons)
    print()
    print(len(pokemons))
    llave=pokemons.keys()
    valores=pokemons.values()
    plt.bar(llave, valores, color = ['orangered', 'purple', 'red', 'teal', 'dodgerblue', 'greenyellow', 'lightgray', 'yellow', 'darkgoldenrod', 'sienna', 'fuchsia', 'maroon', 'cyan', 'slateblue', 'midnightblue','teal','peru'])
    #nombre de los valores del eje x
    plt.xlabel("tipos de debilidades")
    #titulo del grafico
    plt.title("Numero de pokemons por debilidad")
    #nombre de los valores de eje Y
    plt.ylabel("cantidad de pokemons segun su tipo debilidad")
    plt.show()


#funcion del ejercicio 2
def ejercicio2():
    lista_alturas=[]#  lista de alturas esta en el eje x
    lista_pesos=[]# lista e pesos esta en el eje y
    a=todoslospokemon()
    for pkmon in a:
        lista_alturas.append(float(pkmon["height"][:-2]))
    print(len(lista_alturas))
    #print(m) 
    for pkmon in a :
        lista_pesos.append(float(pkmon["weight"][:-3]))
    print(lista_alturas)
    print()
    print(lista_pesos)
    print()
    print(len(lista_pesos))
    plt.scatter(lista_alturas,lista_pesos,marker='o',color="red")
    plt.xlabel("Altura de pokemon en cm")
    plt.ylabel("Peso de pokemon en kg ")
    plt.title("Grafico altura vs peso")
    plt.show()

#función del ejercicio 3
def ejercicio3():
    image= plt.imread('Kanto.png')
    plt.imshow(image)
    a=todoslospokemon()
    
    id_primos=[]
    for pkmon in a:
        if numprimo(pkmon["id"])==True:
            id_primos.append(pkmon["id"])
    print(id_primos)
    for j in id_primos:
        a,b=coordenadas(j)# a= cordx[] ,  b= cordY[]
        plt.plot(a,b,'o',color="blue")
        print(j,coordenadas(j))
    plt.title("Localización de pokemons con id primo ")
    plt.show()


#fución del ejercicio4
def ejercicio4():
    pkmons=todoslospokemon()
    caramelos={"pokemons que no usan caramelos":0,"pokemons que usan caramelos":0}
    
    for x in pkmons:
        if x["candy"] =="None":
            caramelos["pokemons que no usan caramelos"] +=1
        else:
            caramelos["pokemons que usan caramelos"] +=1
    #print(caramelos)
    llaves=caramelos.keys()
    valores=caramelos.values()
    desfase=(0.1,0)
    #print(valores)
    #print()
    #print(llaves)
    
    plt.pie(valores,labels=llaves, autopct="%1.1f%%",explode=desfase)
    plt.title("Porcentaje de pokemons que usan o no caramelos")
    plt.show()
    
         
ejercicio1()
ejercicio2()
ejercicio3()
ejercicio4()
        




    




   

    



    
          

