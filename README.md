# PC2-visualización de datos(Grupo3)
## Visualización de datos.
En el presente Proyecto  usaremos la visualización de datos para poder representar de manera gráfica la información de los pokemon de la region kanto.
## integrantes
* Alexander Josue Grande Romero
* Marcelo Jaramillo Alfaro
* Alessandro Zevallos Espinoza
* Maricielo Patricia Valverde Quispe	
## instrucciones del proyecto
### lectura del archivo json como un diccionario:
```py
import json

f = open('<pokemon>.json')
d = json.load(f)
```
### uso de la liberia matplotlib e instalación para visualizar los datos :
```py
import matplotlib.pyplot as plt
```

```py
pip install matplotlib
```

## Grafico de barras

```py
plt.bar(<keys>, <values>,color="colores")
plt.title("titulo del grafico")
plt.show()
```

![](https://github.com/Grande1996/PC2-Trabajodevisualizaci-n-Grupo3-/blob/main/Figure_1.png)

## Scatterplot (Grafico de dispersion)
  ### obs:
  por tener muchos valores las lista solo se hara referencia a ellos en los valores X y Y

```py
Valores x= lista de alturas

valores Y= lista de pesos

plt.scatter(<valores x>, <valores y>,'o',color="red")
plt.show()
```
![](https://github.com/Grande1996/PC2-Trabajodevisualizaci-n-Grupo3-/blob/main/Figure_2.png)

## Grafico en el mapa de Kanto
```py
valores x= coordenasX
Valores y= CoordenasY

im = plt.imread('kanto.png')
implot = plt.imshow(im)
```
```py
plt.plot(<Valores x>, <Valores y>,'o',color="colores")
plt.show()
```


![](https://github.com/Grande1996/PC2-Trabajodevisualizaci-n-Grupo3-/blob/main/Figure_3.png)

## Grafico Pastel
```py
caramelos={"pokemons que no usan caramelos":0,"pokemons que usan caramelos":0}

plt.pie(x=valores, labels=keys(uso o no de caramelos), autopct="%1.1f%%",explode)
plt.show()
```
### obs:
  ***autopct***: es un parámetro sirve para mostrar los valores porcentuales de las partes de la gráfica.
  
  ***explode***: Es un parámetro opcional que consiste en una lista o tupla que indica cuanto separar los pedazos del pastel
  
![](https://github.com/Grande1996/PC2-Trabajodevisualizaci-n-Grupo3-/blob/main/Figure_4.png)
