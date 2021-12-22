# PC2-visualización de datos(Grupo3)
## Visualización de datos.
En el presente Proyecto  usaremos la visualización de datos para poder representar de manera gráfica la información de los pokemon de la region kanto.
## Integrantes:
* Alexander Josue Grande Romero  (10)
* Marcelo Jaramillo Alfaro       (10)
* Alessandro Zevallos Espinoza   (10)
* Maricielo Patricia Valverde Quispe	 (10)

## Instrucciones del proyecto
### Lectura del archivo json como un diccionario:
```py
import json

f = open('<pokemon>.json')
d = json.load(f)
```
### Recordando uso de la liberia matplotlib e instalación para visualizar los datos :
```py
import matplotlib.pyplot as plt
```

```sh
pip install matplotlib
```

### Recordando algunas funciones de matplotlib
```py
plt.xlabel(): Sirve para poner etiquetas de los valores del eje X

plt.ylabel():Sirve para poner etiquetas de los valores del eje Y

plt.title(): Sirve para poner el titulo del grafico
```

## Graficos
###  Grafico en barras
***obs***:
***color***: Es un parámetro que resive una lista de colores.

```py
colores=[lista de colores]
keys=[lista de tipos de pokemon]
values=[lista de la cantidad de pokemons que tienen un tipo de pokemon como debilidad]

plt.bar(<keys>, <values>,color=colores)
plt.title("Numero de pokemons por debilidad")
plt.xlabel("tipos de debilidades")
plt.ylabel("cantidad de pokemons segun su tipo debilidad")
plt.show()
```
***recordar***: Que la lista de los valores y las llaves son de igual longitud.

![](https://github.com/Grande1996/PC2-Trabajodevisualizaci-n-Grupo3-/blob/main/Figure_1.png)

## Scatterplot (Grafico de dispersion)
  ***obs***: Por tener muchos valores las lista solo se hara referencia a ellos en los valores X y Y.

```py
Valores x = lista de alturas
valores Y = lista de pesos

plt.scatter(<valores x>, <valores y>,'o',color="red")
plt.xlabel("Altura de pokemon en cm")
plt.ylabel("Peso de pokemon en kg ")
plt.title("Grafico altura vs peso")
plt.show()
```
***recordar***: Que la lista de los valores  'x' y 'y' son de igual longitud.

![](https://github.com/Grande1996/PC2-Trabajodevisualizaci-n-Grupo3-/blob/main/Figure_2.png)

## Grafico en el mapa de Kanto
```py

valores x = coordenasX
Valores y = CoordenasY

im = plt.imread('kanto.png')
implot = plt.imshow(im)
```
```py
plt.plot(<Valores x>, <Valores y>,'o',color="colores")
plt.title("Localización de pokemons con id primo ")
plt.show()
```


![](https://github.com/Grande1996/PC2-Trabajodevisualizaci-n-Grupo3-/blob/main/Figure_3.png)

## Grafico Pastel
```py

caramelos = {"pokemons que no usan caramelos":0,"pokemons que usan caramelos":0}
colores=['yellowgreen','darkorchid']
llaves=caramelos.keys()
valores=caramelos.values()

plt.pie(x=valores, labels=llaves,autopct="%1.1f%%",explode= (0.1,0),colors=colores)
plt.title("Porcentaje de pokemons que usan o no caramelos")
plt.show()
```
### obs:
  ***autopct***: Es un parámetro sirve para mostrar los valores porcentuales de las partes de la gráfica.
  
  ***explode***: Parámetro opcional que resive en una lista o tupla con tantos valores como sectores haya. cada valor indica cuanto separar los pedazos del pastel respecto al   centro .
 
 ***colors***: Es un parámetro que resive una lista de colores.
  
![](https://github.com/Grande1996/PC2-Trabajodevisualizaci-n-Grupo3-/blob/main/Figure_4.png)
