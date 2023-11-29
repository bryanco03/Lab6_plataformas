# Laboratorio 6. Programacion bajo plataformas abiertas 

### Bryan Cortés Espínola C22422
---
# Callbacks en Python
---


En el primer enunciado del laboratorio se utilizó las clases *EventManager* y *RealTimeDataManager* de los archivos `eventmanager.py` y `datamanager.py` en los cuales EventManager es un atributo de RealTimeManager, por lo cual se implementó el método *notify()* de EventManager, en método *start_real_time_updates()*, asimismo en el archivo `main_problema1.py` se define la función *imprimir_datos()* , la cual imprime los valores de los datos registrados  y se crea una instancia de *RealTimeDataManager* y se suscribe el evento "datos", con la función *imprimir_datos()*, la cual la función de callback del evento, luego se va estar generando información en segundo plano y va estar mostrando la informacion cada segundo.

---
# Funciones lambda en Python 

---

En esta parte del laboratorio se utiliza el archivo `calc.py`, el cual se extendio la funcion *ejecutar_operacion()* utilizando callbacks para invocar las operaciones que se deseen realizar, aparte en el *main()*, se definio la siguiente biblioteca:

```
operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y if y != 0 else "No es posible dividir por cero."   
            }
```
En la cual se definen por medio de funciones lambdas, todas las operaciones aritméticas que se desean realizar en el programa, lo cual al correr el programa las operaciones se ejecutan con exito.
