Lecture 1 - Algorithm elements
------------------------------

Expressions
~~~~~~~~~~~

.. index:: expression

Una **expresión** es una combinación de valores y operaciones
que son evaluados durante la ejecución del algoritmo
para obtener un valor.
Por ejemplo, :math:`2 + 3` es una expresión
que, al ser evaluada, siempre entrega el valor :math:`5`.

En el ejemplo, :math:`b^2 - 4ac` es una expresión,
cuyo valor depende de qué valores tienen
:math:`a`, :math:`b` y :math:`c`
al momento de la evaluación.

Asignations
~~~~~~~~~~~

.. index:: assignation, variable, identificator

Cuando un algoritmo calcula valores,
se necesita ponerles un nombre para poder referirse a ellos
en pasos posteriores.
Es lo que hacemos en el paso 2 de nuestro algoritmo,
cuando calculamos el discriminante y lo llamamos :math:`Δ`.
Esto se llama una **asignación**,
y se representa así::

    nombre = expresión

Al nombre usado en una expresión se le denomina
**variable** o **identificador**.

La asignación del ejemplo sería::

    Δ = b² − 4 * a * c

Una asignación debe interpretarse así:

1. primero la expresión a la derecha del ``=`` es evaluada,
   utilizando los valores que tienen las variables en ese momento;
2. una vez obtenido el resultado,
   el valor de la variable a la izquierda del ``=``
   es reemplazado por ese resultado.

Bajo esta interpretación,
es perfectamente posible una asignación como ésta::

    i = i + 1

Primero la expresión es evaluada,
y su resultado es el sucesor del valor actual de ``i``.
Por ejemplo, si ``i`` tiene el valor 15,
después de la asignación tendrá el valor 16.
Esto *no* significa que 15 = 16.

Condicionales
~~~~~~~~~~~~~

.. index:: condicional

A veces un algoritmo debe realizar pasos diferentes
bajo condiciones distintas.
Es lo que hacemos en el paso 3 del ejemplo:
decidimos que la ecuación no tiene soluciones
solamente cuando se cumple que :math:`Δ < 0`.
Esto se llama un **condicional**.

La condición que determina qué ejecutar
es una expresión, cuyo valor debe ser
verdadero o falso.

Ciclos
~~~~~~

.. index:: ciclo, condición de término

Un **ciclo** ocurre cuando
un algoritmo ejecuta una serie de instrucciones
varias veces.

Como un algoritmo no puede quedarse pegado,
un ciclo debe tener además una condición de término,
cuyo valor indica si el ciclo debe continuar o terminar.

El ejemplo no tiene ciclos.

Entrada
~~~~~~~

.. index:: entrada, lectura

Cuando un algoritmo necesita recibir un dato,
se representa así::

    variable = input()

(``input`` significa «ingresar» en inglés).
Durante la ejecución,
esto significa que el dato
queda guardado en la variable.

En el ejemplo, la entrada ocurre en el paso 1,
y puede ser representada así::

    a = input()
    b = input()
    c = input()

Salida
~~~~~~

.. index:: salida, escritura

Una vez que el algoritmo ha resuelto el problema
para el que fue diseñado,
debe entregar sus resultados como un mensaje.
La salida se representa así::

    print(mensaje)

(``print`` significa «imprimir» en inglés).
Si el mensaje es un texto literal,
va entre comillas.
Si es una variable,
va sólo el nombre de la variable.

En el ejemplo, cuando no existen soluciones,
la salida puede ser representada así::

    print('No hay soluciones')

Cuando existe una única solución,
se puede incluirla en el mensaje::

    print 'La solución única es', x
