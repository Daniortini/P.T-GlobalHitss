# ¿En que consistió el desarrollo de la prueba?

Para la prueba indicada se usó Python y Selenium para la integración del programa a ejecutar mediante la automatización y se utilizo visual studio code como editor de código fuente.

# Configuración del entorno

Se deben ejecutar los siguientes comandos en el mismo orden:

version de pythhon: **v3.13.5**

```
1. Para acceder al Github: git clone https://github.com/Daniortini/P.T-GlobalHitss.git

2. Para crear la carpeta en local y visualizar el final de la ejecución: cd P.T-GlobalHitss

3. Para crear el ambiente virtual: python -m venv venv

-Si estas en linux o Unix debes ejecutar: source venv/bin/activate

-Si estas en windows: .\venv\Scripts\activate.bat

4. Se debe ejecutar la instalacion de los paquetes: pip install -r requirements.txt 

5. Una vez instalados los paquetes se procede a la ejecución: python . -m 

```

# Ejecución de reporte 

```
En la consola se visualiza el paso a paso de la ejecución , cumpliendo asi 
con las especificaciones propuestas en la prueba
1. Ingresar al sitio web: https://www.mercadolibre.com/
2. Seleccionar México como país
3. En la barra buscador buscar "playstation 5"
4. Usar los filtros dispuestos en la parte izquierda de la pantalla "Nuevos"
5. Usar el filtro de ubicación, en este punto se tiene como consideración que dentro 
del filtro no se encuentra la ubicacion "CDMX" por lo que se toma el filtro 
**Distrito Federal**"
6. Se da clic sobre la flecha de ordenar por y se debe visualizar el despliegue 
de las opciones 
7. Al visualizarse las opciones se elige "Mayor precio"
8. Un vez seleccionado este filtro se muestran los productos de mayor a menor, en la 
ejecución se podra visualizar en la consola los 5 primeros productos con nombre y precio 
distinguidos con tres asteriscos "***" al inicio 
9. Se da por finalizado la prueba y se podrá visualizar en la carpeta "screenshots" las imágenes tomadas del paso a paso anteriormente descrito.

```