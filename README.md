# 👥 PyLicenciasPersonal 👥
Sistema de gestión de licencias para un departamento de personal, en donde se lleva registro y control de licencias de empleados, en el podrás:

* Crear y borrar empleados basados en un identificador denominado "número de legajo".
* Crear y borrar dias correspondientes por año.
* Crear Licencias.
* Llevar registro de licencias y días correspondientes de empleados.
* Generar Excel con informe

## Diagrama de Clases
Se decidió realizar el proyecto en base al paradigmas orientado a objetos, por lo tanto, se adjunta el diagrama de clases asociado a la resolución del escenario, esto también afectó la manera de organización de los módulos y clases del proyecto [(Véase la carpeta raíz del código)](https://github.com/damianstetson17/PyLicenciasPersonal/tree/main/src)

![diagrama_de_clases](https://github.com/damianstetson17/PyLicenciasPersonal/blob/main/img/classes.jpeg)

## ⚠️ Estado del proyecto ⚠️

El proyecto aún se encuentra **en desarrollo**.

### Hecho ✅:
* Modelo completo.
* Logger en consola de los llamados a los módulos y mensajes de errores.
** ![errors and msj](https://github.com/damianstetson17/PyLicenciasPersonal/blob/main/img/msj_errors.png)

### En desarrollo 🛠️:
* No contabilizar *días feriados* ni *fines de semana* a la hora de contabilizar los días de licencia
* Caducidad de días correspondientes no utilizados en *X* cantidad de tiempo en desarrollo.
* Graphic user interface.
* Generación de Excels.


## 🚀 ¿Cómo ejecutar? 🚀

_Para ejecutar correctamente simplemente ejecutar el archivo [main.py](https://github.com/damianstetson17/PyLicenciasPersonal/blob/main/src/main.py) este contiene la instanciación de dos empleados ("Namis" y "Angy") quienes poseen sus números de legajo ("Namis" posee el número de legajo "1", "Angy" el número de legajo "2") seguido a estos se instanciarán dos días correspondientes al empleado "Namis", le corresponderán 10 días del año 2021 y 25 días del año 2009. Se solicitará generar dos Licencia, una de 15 días (desde 1/03/21 al 16/03/21) y otra de 5 días (desde 1/05/21 al 6/05/21).
Además se agrega una licencia solicitada luego de estas que pide 16 días al empleado "Namis", el cual no posee (Ya que utilizó todos sus días disponibles en las dos licencias anteriores) para generar situación de error y poner el sistema a pruebas, el cual no generará dicha licencia. Ídem de esto es la generación de una licencia en el mísmo día de inicio que una de las ya generadas (esto generar una situación de error, por lo que el sistema tampoco la generará)_

EL mensaje mostrado por consola, de esto será:

![msj_lic](https://github.com/damianstetson17/PyLicenciasPersonal/blob/main/img/msj_gen_lic.png)
