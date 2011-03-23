Lecture 14 - Creación de módulos
--------------------------------
.. index:: módulo (creación)

Un módulo sencillo es simplemente un archivo con código en Python.
El nombre del archivo indica cuál es el nombre del módulo.

Por ejemplo, podemos crear un archivo llamado ``pares.py``
que tenga funciones relacionadas con los números pares::

 def es_par(n):
 return n % 2 == 0

 def es_impar(n):
 return not es_par(n)

 def pares_hasta(n):
 return range(0, n, 2)

En este caso, el nombre del módulo es ``pares``.
Para poder usar estas funciones desde otro programa,
el archivo ``pares.py`` debe estar en la misma carpeta
que el programa.

Por ejemplo,
el programa ``mostrar_pares.py``
puede ser escrito así::

 from pares import pares_hasta

 n = int(raw_input('Ingrese un entero: '))
 print 'Los numeros pares hasta', n, 'son:'
 for i in pares_hasta(n):
 print i

Y el programa ``ver_si_es_par.py``
puede ser escrito así::

 import pares

 n = int(raw_input('Ingrese un entero: '))
 if pares.es_par(n):
 print n, 'es par'
 else:
 print n, 'no es par'

Como se puede ver,
ambos programas pueden usar los objetos definidos en el módulo
simplemente importándolos.

Usar módulos como programas
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Un archivo con extensión ``.py`` puede ser un módulo o un programa.
Si es un módulo,
contiene definiciones que pueden ser importadas desde un programa o desde otro módulo.
Si es un programa,
contiene código para ser ejecutado.

A veces, un programa también contiene definiciones
(por ejemplo, funciones y variables)
que también pueden ser útiles desde otro programa.
Sin embargo, no pueden ser importadas,
ya que al usar la sentencia ``import``
el programa completo sería ejecutado.
Lo que ocurriría en este caso es que,
al ejecutar el segundo programa,
también se ejecutaría el primero.

Existe un truco para evitar este problema:
siempre que hay código siendo ejecutado,
existe una variable llamada ``__name__``.
Cuando se trata de un programa,
el valor de esta variable es ``'__main__'``,
mientras que en un módulo,
es el nombre del módulo.

Por lo tanto,
se puede usar el valor de esta variable
para marcar la parte del programa
que debe ser ejecutada al ejecutar el archivo,
pero no al importarlo.

Por ejemplo,
el siguiente programa convierte
unidades de medidas de longitud:

.. literalinclude:: ../../_static/programs/unit_conversion.py

Este programa es útil por sí solo,
pero además sus cuatro funciones
y las constantes ``km_por_milla`` y ``cm_por_pulgada``
podrían ser útiles para ser usadas en otro programa.

Al poner el cuerpo del programa
dentro del ``if __name__ == '__main__'``,
el archivo puede ser usado como un módulo.
Si no hiciéramos esto,
cada vez que otro programa importe una función
se ejecutaría el programa completo.

Haga la prueba: `descargue el programa`_ y ejecútelo.
Luego, escriba otro programa que importe alguna de las funciones.
A continuación, haga lo mismo,
pero eliminando el ``if``.

.. _descargue el programa: ../_static/programas/conversion_unidades.py


