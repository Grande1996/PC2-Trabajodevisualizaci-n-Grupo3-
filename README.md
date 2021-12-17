# PC2-visualización de datos(Grupo3)
## Visualización de datos.
En el presente Proyecto  usaremos la visualización de datos para poder representar de manera gráfica la información de los pokemon de la region kanto.
## integrantes
* Alexander Josue Grande Romero
* Marcelo Jaramillo Alfaro
* Alessandro Zevallos Espinoza
*
*
## instrucciones del proyecto
### lectura del archivo json como un diccionario:
```py
import json

f = open('<filename>.json')
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
plt.bar(<keys>, <values>)
plt.show()
```

![](https://github.com/Grande1996/PC2-Trabajodevisualizaci-n-Grupo3-/blob/main/Figura1.png)

## Scatterplot 

```py
plt.scatter(<valores x>, <valores y>)
plt.show()
```
![](https://github.com/Grande1996/PC2-Trabajodevisualizaci-n-Grupo3-/blob/main/figura2.png)

## Grafico en el mapa de Kanto

```py
im = plt.imread('kanto.png')
implot = plt.imshow(im)
```
```py
plt.plot()
plt.show()
```


![](https://github.com/Grande1996/PC2-Trabajodevisualizaci-n-Grupo3-/blob/main/figura3.png)

## Grafico Pastel
```py
plt.pie(x=valores, labels=etiquetas, colors = colores)
plt.show()
```

![](https://github.com/Grande1996/PC2-Trabajodevisualizaci-n-Grupo3-/blob/main/figura4.png)
