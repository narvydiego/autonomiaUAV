# autonomia UAV

Este proyecto está diseñado para analizar y predecir la autonomía de los vehículos aéreos no tripulados (UAV), enfocándose específicamente en el dron DJI Tello. Utilizando técnicas avanzadas de programación en Python, hemos desarrollado un sistema que permite un control total sobre el dron, facilitando la recopilación de datos críticos sobre su rendimiento en vuelo y el consumo de batería.

El objetivo principal es desarrollar un modelo predictivo que pueda estimar con precisión la duración de la batería del dron bajo diversas condiciones operativas. Este modelo ayudará a optimizar las operaciones de vuelo y garantizar una gestión eficiente de la energía, lo cual es crucial para maximizar la utilidad del UAV en aplicaciones comerciales y de investigación.

## Estructura del Proyecto

1. **Control:** 
    Código que permite controlar cada movimiento del dron mediante teclado. Se utilizan las librerías Tellopy y Pygame para manejar las acciones de las teclas W, S, A, D, flechas, J y K.
2. **Datos:**
    Base de datos utilizada para entrenar el modelo en formato XLSX.
3. **Escenarios:**
    Scripts con el Path Planning de cada uno de los escenarios, utilizando Tellopy y Time. Entre los escenarios contemplamos:
    - **Movimiento Vertical:** El dron se eleva a alturas de 2, 4 y 6 metros.
    - **Movimiento Horizontal:** El dron se desplaza por 2, 4 y 6 metros.
    - **Estado Estático:** El dron se eleva a 4 metros de altura y se mantiene en el aire por 5 minutos.
    - **Ruta Marcada:** El dron se eleva a 1 metro de altura, después realiza un recorrido en forma de cuadrado donde en cada uno de sus lados recorre 5 metros.
4. **Modelos de Predicción:**
    Contiene los modelos de predicción Regresión Lineal y Árbol de Decisión, así como la interfaz para que el usuario pueda obtener un valor de predicción sobre el consumo de batería en función del desplazamiento que se planifique realizar. 
5. **Prototipos:**
    Contiene los dos prototipos utilizados para realizar las pruebas con diferentes pesos, además de un diseño de propellers para el dron. Cabe resaltar que el filamento utilizado para imprimir cada uno de estos diseños es PLA. En los propellers se recomienda utilizar una impresora con alto grado de precisión.

## Requerimientos

- Python
    - Tellopy
    - Time
    - Pandas
    - Pyexcel-xls
- Toolkit de Machine Learning de Matlab
- Fusion 360
- Cura for Robo R2

## Instalación

Para instalar y configurar el proyecto, sigue estos pasos:

```bash
# Clona el repositorio
git clone https://github.com/usuario/autonomiaUAV.git

# Entra al directorio del proyecto
cd autonomiaUAV

# Instala las dependencias de Python
pip install tellopy time pandas pyexcel-xls
