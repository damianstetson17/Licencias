# 👥 PyLicenciasPersonal 👥
Base para un sistema de gestión de licencias para un departamento de personal, en donde se lleva registro y control de licencias de empleados, en el podrás:

* Crear y borrar empleados basados en un identificador denominado "número de legajo".
* Crear y borrar dias correspondientes por año.
* Crear Licencias con controles de fines de semana y/o feriados.
* Llevar registro de licencias y días correspondientes de empleados.

## Diagrama de Clases
Se decidió realizar el proyecto en base al paradigmas orientado a objetos, por lo tanto, se adjunta el diagrama de clases asociado a la resolución del escenario, esto también afectó la manera de organización de los módulos y clases del proyecto [(Véase carpeta raíz.)](https://github.com/damianstetson17/PyLicenciasPersonal/tree/main/src).

![diagrama_de_clases](https://github.com/damianstetson17/PyLicenciasPersonal/blob/main/img/classes.png.png)

## ⚠️ Estado del proyecto ⚠️

### Hecho ✅:
* Modelo completo.
* No contabilizar **días feriados** _(Estos cargables por el usuario)_ ni **fines de semana** a la hora de contabilizar los días de licencia
* Caducidad de días correspondientes no utilizados en *X* cantidad de tiempo.
* "Logger" en consola de los llamados a los módulos y mensajes de errores.
![errors and msj](https://github.com/damianstetson17/PyLicenciasPersonal/blob/main/img/msj_errors.png)

### No implementado ❌:
* Conexión con BD.
* Graphic user interface.

## 🔧 Construido con:
* [Lucidchart](www.lucidchart.com)
* [Python 3.8.7](https://www.python.org/downloads/release/python-387/)
* [PyCharm](https://www.jetbrains.com/es-es/pycharm/)

## 🚀 ¿Cómo ejecutar? 🚀

Para ejecutar correctamente simplemente compilar el archivo [main.py](https://github.com/damianstetson17/PyLicenciasPersonal/blob/main/src/main.py).
* Tener [Python](https://www.python.org/) instalado.
* Abrir un Terminal _(En windows apretar **Win + r** y tipear **"cmd"**)_.
* Posicionarse mediante el comando **"cd"** sobre la [carpeta raíz del código](https://github.com/damianstetson17/PyLicenciasPersonal/tree/main/src).
* Ejecutar la sentencia "```python main.py```".

### ¿Que me encontraré al compilar el archivo [main.py](https://github.com/damianstetson17/PyLicenciasPersonal/blob/main/src/main.py)?
Que no te pierda la cantidad de contenido dentro del fichero [main.py](https://github.com/damianstetson17/PyLicenciasPersonal/blob/main/src/main.py), simplemente
crea instancias de los objetos del modelo, comprueba objetos duplicados, vencimientos de días correspondientes, licencias repetidas, licencias no posibles de tomar, entre otros, encima de cada llamado a funciones se encuentra documentado la finalidad del mísmo. Anímate a trastear con el código, sirve como base para proyectos más grandes [(Véase una implementación del mísmo en Java)](https://github.com/damianstetson17/LicenciasJava).

Una fracción del mensaje mostrado por consola _(De la generación de licencias)_, al compilarse será:

![msj_lic](https://github.com/damianstetson17/PyLicenciasPersonal/blob/main/img/msj_gen_lic.png)

## 🦚 Aclaraciones 🦚

Este proyecto se ha desarrollado con el fin de aprendizaje del lenguaje Python, como así generar una base sólida para el desarrollo de sistemas de gestiones de Licencias de organizaciones.
Por otra parte, se han desarrollado métodos _"getters & setters"_ basados en la filosofía de un fuerte encapsulamiento  esto no tendrá nunca la mísma filosofía planteada en **Java**. Existe un concepto que describe bien la diferencias en este: La idea del _"Programador Malvado"_ _(Por favor no malinterpretar esto, es simplemente una metáfora)_, en Java hay un encapsulamiento muy fuerte en los objetos, ciertas propiedades las podemos acceder solo mediante los métodos apropiados, la idea es que en **Java** se cuida a los objetos de este hipotético _"Programador Malvado"_, en **Python** esa idea se la reemplaza por un: _"somos todos adultos"_, es decir cada uno sabe lo que está haciendo, si quieres modificar un atributo interno de un objeto, perfecto, se supone que sabes lo que estás haciendo. Por lo que se han generado métodos hipotéticos que incluso algunos no se utilizan dentro del projecto. 

_Todas estas imágenes y documentación se encuentran sujetas a cambios, que serán publicados en tiempo y forma._
