Class 2
=======

Script creation
---------------

PENDING

Control sentences
-----------------

A program is a **sentence** succession
being executed sequentially.

For example, the following program has four sentences::

    n = int(raw_input('Enter n: '))
    m = int(raw_input('Enter m: '))
    sum = n + m
    print 'The sum of n and m is:', sum

The first three lines are assignments,
and the last one is a function call.
Running the program,
each of these sentences is executed,
one after the other, once.

.. index:: control sentence

Besides the simple sentences,
which are sequentially executed,
there are the **control sentences**
allowing modify the program flow
introducing cycles and conditionals.

.. index:: conditional

A **conditional** is a sentence set
which can or can not execute,
depending of a condition result.

.. index:: cycle

A **cycle** is a sentence set
which are executed several times,
until one of the end condition was satisfied.

.. index:: indentation

The conditionals and the cycles
contains other sentences.
To indicate this relation
python use the **identation**:
the contained sentences
are not writed in the same column
that the control sentence,
but more to the right::

    n = int(raw_input())
    m = int(raw_input())
    if m < n:
        t = m
        m = n
        n = t
    print m, n

In this example, the three asignations are
contained inside the ``if`` control sentence.
The ``print m, n`` is not indented,
so is not a part of the ``if`` sentence.

This program has four sentences,
of which the third one is a control sentence,
that contain the other three sentences.

To indent,
we will use four spaces always.

if conditional
~~~~~~~~~~~~~~
.. index:: if

The **if** sentence
execute the instrutions
only if a condition is satisfied.
Si la condición es falsa,
no se hace nada:

.. image:: ../diagrams/if.png
   :alt: (if flow diagram)

The syntax is as follows::

    if condition:
        sentences

For example,
the following program congratulates someone
thats approved the course::

    nota = int(raw_input('Enter your grade: '))
    if grade >= 55:
        print 'Congratulations!'

Execute this program,
testing it several times with different values.

if-else conditional
~~~~~~~~~~~~~~~~~~~
.. index:: if-else

The **if-else** sentence
decide what instructions execute
depending if a condition is true or false:

.. image:: ../diagrams/if-else.png
   :alt: (if-else flow diagram)

The syntax is as follows::

    if condición:
        qué hacer cuando la condición es verdadera
    else
        qué hacer cuando la condición es falsa

For example,
the following program indicates if someone is an adult (in Chile)::

    edad = int(raw_input('How old are you? '))
    if edad < 18:
        print 'You are a minor'
    else:
        print 'You are an adult'

The next program do different actions
depending if the input number is even or odd::

    n = int(raw_input('Enter a number: '))
    if n % 2 == 0:
        print 'The number is even'
        print 'The halfnumber is', n / 2
    else:
        print 'The number is odd'
        print 'The next number is', n + 1
    print 'Ready'

The last sentence is not indented,
so it is not a part of the conditional,
and will be always executed.

if-else-elif conditional
~~~~~~~~~~~~~~~~~~~~~~~~
.. index:: if-elif-else

The **if-elif-else** sentence
depends on two or more conditions,
which are evaluated in order.
The first which is true
determines what instructions will be executed:

.. image:: ../diagrams/if-elif-else.png
   :alt: (if-elif-else flow diagram)

The syntax is as follow::

    if condition1:
        what to do if condition1 is true
    elif condition2:
        what to do if condition2 is true
    ...
    else:
        what to do if none of the above conditions is true

The last ``else`` is optional.

For example,
the rate of tax payable by a person according to his salary
can be given by the next table:

====================== ====================
**salary**             **tax rate**
---------------------- --------------------
less than 1000                           0%
1000 ≤ sueldo < 2000                     5%
2000 ≤ sueldo < 4000                    10%
4000 or higher                          12%
====================== ====================

So, the program that compute the tax to pay
is as follow::

    salary = int(raw_input('Enter salary: '))
    if salary < 1000:
        rate = 0.00
    elif salary < 2000:
        rate = 0.05
    elif salary < 4000:
        rate = 0.10
    else:
        rate = 0.12
    print 'You must pay', rate * salary, 'of taxes'

Always only one of the alternatives will be executed.
If one of the conditions, in order, is true,
the below conditions are not being evaluated.

Another way to write the same program
using only the ``if`` sentece is as follow::


    salary = int(raw_input('Enter salary: '))
    if salary < 1000:
        rate = 0.00
    if 1000 <= sueldo < 2000:
        rate = 0.05
    if 2000 <= sueldo < 4000:
        rate = 0.10
    if 4000 < sueldo:
        rate = 0.12
    print 'You must pay', rate * salary, 'of taxes'

This way is less clear,
because is not obvious at first look that
only one of the conditions will be true.

Cyclic flow
-----------

while cycle
~~~~~~~~~~~

.. index:: while

El ciclo **while**
(«mientras»)
ejecuta una secuencia de instrucciones
mientras una condición sea verdadera:

.. image:: ../diagrams/while.png
   :alt: (while flow diagram)

.. index:: iteración

Cada una de las veces que el cuerpo del ciclo es ejecutado
se llama **iteración**.

La condición es evaluada antes de cada iteración.
Si la condición es inicialmente falsa,
el ciclo no se ejecutará ninguna vez.

La sintaxis es la siguiente::

    while condición:
        sentencias

Por ejemplo,
el siguiente programa
multiplica dos números enteros
sin usar el operador ``*``::

    m = int(raw_input())
    n = int(raw_input())
    p = 0
    while m > 0:
        m = m - 1
        p = p + n
    print 'El producto de m y n es', p

Para ver cómo funciona este programa,
hagamos un ruteo con la entrada ``m`` = 4
y ``n`` = 7:

   +-------+-------+-------+
   | ``p`` | ``m`` | ``n`` |
   +=======+=======+=======+
   |       |     4 |       |
   +-------+-------+-------+
   |       |       |     7 |
   +-------+-------+-------+
   |     0 |       |       |
   +-------+-------+-------+
   |       |     3 |       |
   +-------+-------+-------+
   |     7 |       |       |
   +-------+-------+-------+
   |       |     2 |       |
   +-------+-------+-------+
   |    14 |       |       |
   +-------+-------+-------+
   |       |     1 |       |
   +-------+-------+-------+
   |    21 |       |       |
   +-------+-------+-------+
   |       |     0 |       |
   +-------+-------+-------+
   |    28 |       |       |
   +-------+-------+-------+

En cada iteración,
el valor de ``m`` decrece en 1.
Cuando llega a 0,
la condición del ``while`` deja de ser verdadera
por lo que el ciclo termina.
De este modo,
se consigue que el resultado sea
sumar ``m`` veces el valor de ``n``.

Note que el ciclo no termina apenas el valor de ``m`` pasa a ser cero.
La condición es evaluada una vez que la iteración completa ha terminado.

En general,
el ciclo ``while`` se utiliza cuando no es posible saber de antemano
cuántas veces será ejecutado el ciclo,
pero sí qué es lo que tiene que ocurrir
para que se termine.



for cycle with counter
~~~~~~~~~~~~~~~~~~~~~~

.. index:: for, variable de control

El ciclo **for con rango**
ejecuta una secuencia de sentencias
una cantidad fija de veces.

Para llevar la cuenta,
utiliza una **variable de control**
que toma valores distintos en cada iteración.

Una de las sintaxis para usar un ``for``
con rango es la siguiente::

    for variable in range(fin):
        qué hacer para cada valor de la variable de control

En la primera iteración,
la variable de control toma el valor 0.
Al final de cada iteración,
el valor de la variable aumenta automáticamente.
El ciclo termina justo antes que la variable
tome el valor ``fin``.

Por ejemplo,
el siguiente programa muestra los cubos
de los números del 0 al 20::

    for i in range(21):
        print i, i ** 3

.. index:: range, rango

Un **rango** es una sucesión de números enteros equiespaciados.
Incluyendo la presentada más arriba,
hay tres maneras de definir un rango::

    range(final)
    range(inicial, final)
    range(inicial, final, incremento)

El valor inicial siempre es parte del rango.
El valor final nunca es parte del rango.
El incremento indica la diferencia
entre dos valores consecutivos del rango.

Si el valor inicial es omitido, se supone que es 0.
Si el incremento es omitido, se supone que es 1.

Con algunos ejemplos quedará más claro:

==================== ===================================
``range(9)``         0, 1, 2, 3, 4, 5, 6, 7, 8
``range(3, 13)``     3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
``range(3, 13, 2)``  3, 5, 7, 9, 11
``range(11, 4)``     ningún valor
``range(11, 4, -1)`` 11, 10, 9, 8, 7, 6, 5
==================== ===================================

Usando un incremento negativo,
es posible hacer ciclos que van hacia atrás::

    for i in range(10, 0, -1):
        print i
    print 'Feliz anno nuevo!'

En general,
el ciclo ``for`` con rango
se usa cuando el número de iteraciones
es conocido antes de entrar al ciclo.


Functions
---------
.. index:: function

Supongamos que necesitamos escribir un programa
que calcule el `número combinatorio`_ `C(m, n)`,
definido como:

.. math::

    C(m, n) = \frac{m!}{(m - n)! n!},

donde `n!` (el factorial_ de `n`)
es el producto de los números enteros desde 1 hasta `n`:

.. math::

    n! = 1\cdot 2\cdot\cdots\cdot(n - 1)\cdot n = \prod_{i=1}^n i

.. _número combinatorio: http://es.wikipedia.org/wiki/Número_combinatorio
.. _factorial: http://es.wikipedia.org/wiki/Factorial

El código para calcular el factorial de un número entero `n`
es sencillo::

    f = 1
    for i in range(1, n + 1):
        f *= i

Sin embargo,
para calcular el número combinatorio,
hay que hacer lo mismo tres veces::

    comb = 1

    # multiplicar por m!
    f = 1
    for i in range(1, m + 1):
        f = f * i
    comb = comb * f

    # dividir por (m - n)!
    f = 1
    for i in range(1, m - n + 1):
        f = f * i
    comb = comb / f

    # dividir por n!
    f = 1
    for i in range(1, n + 1):
        f = f * i
    comb = comb / f

La única diferencia entre los tres cálculos de factoriales
es el valor de término de cada ciclo ``for``
(``m``, ``m - n`` y ``n``, respectivamente).

Escribir el mismo código varias veces es tedioso y propenso a errores.
Además, el código resultante es mucho más dificil de entender,
pues no es evidente a simple vista qué es lo que hace.

Lo ideal sería que existiera una función llamada ``factorial``
que hiciera el trabajo sucio, y que podamos usar de la siguiente manera::


    factorial(m) / (factorial(m - n) * factorial(n))

Ya vimos anteriormente que Python ofrece «de fábrica»
algunas funciones, como ``int``, ``min`` y ``abs``.
Ahora veremos cómo crear nuestras propias funciones.

Function details
~~~~~~~~~~~~~~~~
.. index:: function details

En programación,
una **función** es una sección de un programa
que calcula un valor
de manera independiente al resto del programa.

.. index:: parámetro (de una función), resultado (de una función), valor de retorno

Una función tiene tres componentes importantes:

* los **parámetros**,
  que son los valores que recibe la función como entrada;
* el **código de la función**,
  que son las operaciones que hace la función; y
* el **resultado** (o **valor de retorno**),
  que es el valor final que entrega la función.

En escencia, una función es un mini programa.
Sus tres componentes son análogos a
la entrada, el proceso y la salida de un programa.

En el ejemplo del factorial,
el parámetro es el entero al que queremos calcularle el factorial,
el código es el ciclo que hace las multiplicaciones,
y el resultado es el valor calculado.

Function definition
~~~~~~~~~~~~~~~~~~~
Las funciones en Python son creadas mediante la sentencia ``def``::

    def nombre(parámetros):
        # código de la función

Los parámetros son variables
en las que quedan almacenados los valores de entrada.

La función contiene código igual al de cualquier programa.
La diferencia es que, al terminar,
debe entregar su resultado
usando la sentencia ``return``.

Por ejemplo,
la función para calcular el factorial
puede ser definida de la siguiente manera::

    def factorial(n):
        f = 1
        for i in range(1, n + 1):
            f *= i
        return f

En este ejemplo,
el resultado que entrega una llamada a la función
es el valor que tiene la variable ``f``
al llegar a la última línea de la función.

Una vez creada,
la función puede ser usada como cualquier otra,
todas las veces que sea necesario::

    >>> factorial(0)
    1
    >>> factorial(12) + factorial(10)
    482630400
    >>> factorial(factorial(3))
    720
    >>> n = 3
    >>> factorial(n ** 2)
    362880

.. index:: variable local

Las variables que son creadas dentro de la función
(incluyendo los parámetros y el resultado)
se llaman **variables locales**,
y sólo son visibles dentro de la función,
no desde el resto del programa.

.. index:: variable global

Por otra parte,
las variables creadas fuera de alguna función
se llaman **variables globales**,
y son visibles desde cualquier parte del programa.
Sin embargo, su valor no puede ser modificado,
ya que una asignación crearía una variable local
del mismo nombre.

En el ejemplo, las variables locales son ``n``, ``f`` e ``i``.
Una vez que la llamada a la función termina,
estas variables dejan de existir::

    >>> factorial(5)
    120
    >>> f
    Traceback (most recent call last):
      File "<console>", line 1, in <module>
    NameError: name 'f' is not defined

Después de definir la función ``factorial``,
podemos crear otra función llamada ``comb``
para calcular números combinatorios::

    def comb(m, n):
        fact_m = factorial(m)
        fact_n = factorial(n)
        fact_m_n = factorial(m - n)
        c = fact_m / (fact_n * fact_m_n)
        return c

Esta función llama a ``factorial`` tres veces,
y luego usa los resultados para calcular su resultado.
La misma función puede ser escrita también de forma más sucinta::

    def comb(m, n):
        return factorial(m) / (factorial(n) * factorial(m - n))

El programa completo es el siguiente:

.. literalinclude:: ../_static/programs/combinatorios.py

(Puede descargarlo aquí_).

.. _aquí: ../_static/programs/combinatorios.py

Note que, gracias al uso de las funciones,
la parte principal del programa ahora tiene sólo cuatro líneas,
y es mucho más fácil de entender.

Multiple return values
~~~~~~~~~~~~~~~~~~~~~~
En Python, una función puede retornar más de un valor.

Por ejemplo,
la siguiente función
recibe una cantidad de segundos,
y retorna el equivalente
en horas, minutos y segundos::

    def convertir_segundos(segundos):
        horas = segundos / (60 * 60)
        minutos = (segundos / 60) % 60
        segundos = segundos % 60
        return horas, minutos, segundos

Al llamar la función,
se puede asignar un nombre a cada uno de los valores retornados::

    >>> h, m, s = convertir_segundos(9814)
    >>> h
    2
    >>> m
    43
    >>> s
    34

Técnicamente, la función está retornando una **tupla** de valores,
un tipo de datos que veremos más adelante::

    >>> convertir_segundos(9814)
    (2, 43, 34)

Functions returning anything
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Una función puede realizar acciones
sin entregar necesariamente un resultado.

Por ejemplo,
si un programa necesita imprimir cierta información muchas veces,
conviene encapsular esta acción en una función que haga los ``print`` ::

    def imprimir_datos(nombre, apellido, rol, dia, mes, anno):
        print 'Nombre completo:', nombre, apellido
        print 'Rol:', rol
        print 'Fecha de nacimiento:', dia, '/', mes, '/', anno

    imprimir_datos('Perico', 'Los Palotes', '201101001-1',  3, 1, 1993)
    imprimir_datos('Yayita', 'Vinagre',     '201101002-2', 10, 9, 1992)
    imprimir_datos('Fulano', 'De Tal',      '201101003-3', 14, 5, 1990)

En este caso,
cada llamada a la función ``imprimir_datos``
muestra los datos en la pantalla, pero no entrega un resultado.
Este tipo de funciones es conocido en programación
como **procedimientos** o **subrutinas**,
pero en Python son funciones como cualquier otra.

Técnicamente, todas las funciones retornan valores.
En el caso de las funciones que no tienen una sentencia ``return``,
el valor de retorno siempre es ``None``.
Pero como la llamada a la función no aparece en una asignación,
el valor se pierde, y no tiene ningún efecto en el programa.

Assignment 2
------------

PENDING
