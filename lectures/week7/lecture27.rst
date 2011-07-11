Lecture 27 - NumPy arrays (part III)
-------------------------------------

Products between arrays
========================

Remember that a **vector** is a one dimension array synonymous,
and a **matrix** is a synonymous of a bi-dimensional array.

Inner product (vector-vector)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The **inner product** between two vectors
is the product sum between corresponding elements:

.. image:: ../../diagrams/inner-product.png

The inner product between two vectors
is obtained using the ``dot`` function 
provided by NumPy::

    >>> a = array([-2.8 , -0.88,  2.76,  1.3 ,  4.43])
    >>> b = array([ 0.25, -1.58,  1.32, -0.34, -4.22])
    >>> dot(a, b)
    -14.803

The inner product is a very common operation.
For example, is often used to calculate totals::

    >>> prices = array([200, 100, 500, 400, 400, 150])
    >>> quantities = array([1, 0, 0, 2, 1, 0])
    >>> total_to_pay = dot(prices, quantities)
    >>> total_to_pay
    1400

It is also used to calculate weighted averages::

    >>> grades = array([45, 98, 32])
    >>> weights = array([30, 30, 40]) / 100.
    >>> final_grade = dot(grades, weights)
    >>> final_grade
    55.7

Matrix-Vector Product
~~~~~~~~~~~~~~~~~~~~~~

The **matrix-vector product**
is the vector of the inner products.
The matrix-vector product can be viewed
simply as several inner products
calculated at once.

This operation is also obtained
using the ``dot`` function
between the rows of matrix and vector:

.. image:: ../../diagrams/matrix-vector.png
   :align: center

An example using the ``dot`` function::

    >>> a = array([[-0.6,  4.8, -1.2],
                   [-2. , -3.6, -2.1],
                   [ 1.7,  4.9,  0. ]])
    >>> x = array([-0.6, -2. ,  1.7])
    >>> dot(a, x)
    array([-11.28,   4.83, -10.82])

Matrix-Matrix Product
~~~~~~~~~~~~~~~~~~~~~~

The **matrix-matrix product**
is the matrix of inner products
between the first matrix rows
and columns of the second matrix:

.. image:: ../../diagrams/matrix-matrix.png
   :align: center

This operation is also obtained
using the ``dot`` function::

    >>> a = array([[ 2,  8],
                   [-3,  7],
                   [-8, -5]])
    >>> b array([[-3, -5, -6, -3],
                 [-9, -2,  3, -3]])
    >>> dot(a, b)
    array([[-78, -26,  12, -30],
           [-54,   1,  39, -12],
           [ 69,  50,  33,  39]])

Matrix multiplication
can be viewed as several matrix-vector products
(using all second matrix rows as vectors),
calculated at once.

In summary,
when using the ``dot`` function,
the result structure
depends on which parameters are passed::

    dot(vector, vector) → number
    dot(matrix, vector) → vector
    dot(matrix, matrix) → matrix

Lineal Systems Resolution
==========================

Let's review the matrix-vector product:

.. image:: ../../diagrams/diet-1.png
   :align: center

This operation has two operands:
a matrix and a vector.
The result is a vector.
The operands will call them respectively ``A`` and ``x``,
and the result, ``b``.

A recurring problem in engineering
is to obtain which is the ``x`` vector
when ``A`` and ``b`` are given:

.. image:: ../../diagrams/diet-2.png
   :align: center

The matrix equation `Ax = b` is a shorthand way
of expressing a `system of linear equations`_.
For example,
the equation of the diagram
is equivalent to the following system of three equations
which has three unknowns variables `w`, `y` and `z`:

.. math::

    \begin{align}
      36w + 51y + 13z &= 3 \\
      52w + 34y + 74z &= 45 \\
             7y + 1.1z &= 33 \\
    \end{align}

.. _system of linear equations: http://en.wikipedia.org/wiki/System_of_linear_equations

In mathematics,
this system is represented in matrix, as follows:

.. math::

    \begin{bmatrix}
      36 & 51 & 13 \\
      52 & 34 & 74 \\
         &  7 & 1.1 \\
    \end{bmatrix}
    \begin{bmatrix}
       w \\ y \\ z \\
    \end{bmatrix}
    =
    \begin{bmatrix}
       3 \\ 45 \\ 33 \\
    \end{bmatrix}


The theory behind solving problems like this
you learned in your math classes.
However,
as this type of problem occurs often in practice,
we learn how to quickly get the solution
using Python.

Among the modules included in NumPy
(for example, we saw ``numpy.random``),
is the ``numpy.linalg`` module,
which provides some functions that implement linear algebra algorithms,
which is the mathematics branch that studies this type of problems.
In this module is the ``solve`` function,
which gives the ``x`` system solution
from the ``A`` matrix and the ``b`` vector::

    >>> a = array([[ 36. ,  51. ,  13. ],
    ...            [ 52. ,  34. ,  74. ],
    ...            [  0. ,   7. ,   1.1]])
    >>> b = array([  3.,  45.,  33.])
    >>> x = solve(a, b)
    >>> x
    array([-7.10829222,  4.13213834,  3.70457422])


We can see that indeed the ``x`` vector
satisfies the ``Ax = b`` equation::

    >>> dot(a, x)
    array([  3.,  45.,  33.])
    >>> b
    array([  3.,  45.,  33.])

However, it is important to note that
the real types values
are rarely represented accurately on the computer,
and the algorithm result that involves many operations
may suffer from some rounding errors.
For this reason,
it may happen that although the results look the same on the console,
the obtained data are only approximations
and not exactly the same values::

    >>> (dot(a, x) == b).all()
    False

 
Exercises
=========

* *Bartender*

  To prepare an appetizer, a  bartender stores in three pails
  different wine, gin and lemon juice measures,
  following the next table:
  
  ======= ============= ============= =============
  Pail    Wine          Gin           Lemon juice
  ======= ============= ============= =============
  A                  20            30            50
  B                  30            20            60
  C                  30            30            32
  ======= ============= ============= =============
  
  On the other hand,
  we have the information related to the prices by liter
  of each liquid:
  
  ============= ========
  Liquid        Price
  ============= ========
  Wine                 5
  Gin                 45
  Lemon Juice         10
  ============= ========
  
  #. Write a program which show the price of
     each one of the pails.
  
  #. Write a program which show the total price of
     10 A pails, 4 B pails and 5 C pails.

* *Car production*

  A car factory produce three models:
  sedan, van and economic.
  Each car production needs materials, manpower, taxes and transport.
  The cost in units per each concept are the following:
  
  ========== ======= ===== ==========
  (Cost)     Sedan   Van   Economic
  ========== ======= ===== ==========
  Material         7     8          5
  Manpower        10     9          7
  Taxes            5     3          2
  Transport        2     3          1
  ========== ======= ===== ==========
  
  Weekly, the production amount is of
  60 sedan, 40 van and 90 economic.
  
  The cost of a unit of material, manpower, taxes and transport
  are 5, 15, 7 y 2 respectively.
  
  Write a program which show:
  
  * the weekly needed units of material, manpower, taxes and transport,
  * the total cost of a car of each model,
  * the total cost of the weekly production.

* *Gas production report*

  In the annual report of a gas enterprise,
  the president reports to their shareholders
  the annual amount of the barrel production
  of 50 liter of normal, extra and super lubricant
  in two refineries:
  
  ========= ======== ======== ========
  Refinery  Normal   Extra    Super
  ========= ======== ======== ========
  A             3000     7000     2000
  B             4000      500      600
  ========= ======== ======== ========
  
  Also, reports that in each 50 liter lubricant barrel
  exist the following composition in liter of
  fine oils, tar and residual fat:
  
  ============== ======== ======== ========
  Component      Normal   Extra    Super
  ============== ======== ======== ========
  Fine oils            10        5       35
  Tar                  15        4       31
  Residual fat         18        2       30
  ============== ======== ======== ========
  
  #. Write a function called ``annual_totals(a, b)``
     which receive as parameter both matrix
     and return an array with the totals of
     fine oils, tar and residual fats present in the annual production.
  
  #. Write a function called ``maximum_tar(a, b)``
     which receive as parameter both matrix
     and return the maximum of tar liters
     consumed by both refineries.
  
  #. Determine which is the matrix that return
     the total consumption of the elements that
     are part of the lubricant, in each refinery.

.. Migración de poblaciones
.. ========================
.. 
..     *Ejercicio sacado de* [Lay97]_.
.. 
.. Estudios demográficos muestran que, cada año,
.. el 5% de la población de una ciudad
.. se muda a los suburbios (y el 95% se queda),
.. mientras que el 3% de la población de los suburbios
.. se muda a la ciudad (y el 97% se muda).
.. 
.. Estos datos pueden ser representados
.. en una **matriz de migración**:
.. 
.. .. math::
.. 
..     M =
..     \frac{1}{100}
..     \begin{bmatrix}
..       95 &  3 \\
..        5 & 97 \\
..     \end{bmatrix}
.. 
.. #. Escriba un programa que pregunte al usuario
..    cuáles son las poblaciones de la ciudad y los suburbios
..    en el año 2011,
..    y entregue una tabla con las poblaciones proyectadas
..    para los siguientes 10 años:
.. 
..    .. testcase::
.. 
..        Poblacion ciudad: `600`
..        Poblacion suburbios: `400`
.. 
..        Anno    Ciudad     Suburbios
..        ----------------------------
..        2012    582.000    418.000
..        2013    565.440    434.560
..        2014    550.205    449.795
..        2015    536.188    463.812
..        2016    523.293    476.707
..        2017    511.430    488.570
..        2018    500.515    499.485
..        2019    490.474    509.526
..        2020    481.236    518.764
..        2021    472.737    527.263
.. 
.. #. Considere ahora la siguiente variación.
..    Suponga que
..    todos los años
..    hay 14000 personas que se mudan a la ciudad
..    desde fuera de la región
..    (no desde los suburbios)
..    y 9000 personas abandonan la región;
..    además,
..    hay 13000 personas que se mudan anualmente
..    a los suburbios desde fuera de la ciudad.
.. 
..    Modifique el programa anterior
..    para resolver este problema.
.. 
.. 
.. 
.. .. [Lay97] David C. Lay.
..            *Linear Algebra and Its Applications*.
..            Addison-Wesley, 1997.


.. Construcción de una dieta
.. =========================
.. 
..     *Ejercicio sacado de* [Lay97]_.
.. 
.. La dieta Cambridge es una dieta que fue popular en la década de los 80,
.. y fue el resultado de más de ocho años de trabajo clínico e investigación
.. de un equipo de científicos liderados por el doctor Alan H. Howard
.. en la Universidad de Cambridge.
.. 
.. La dieta combina un balance preciso de carbohidratos,
.. proteínas de alta calidad y grasa,
.. junto con vitaminas, minerales, oligoelementos y electrolitos.
.. Millones de personas han usado la dieta en años recientes
.. para bajar rápidamente de peso.
.. 
.. Para alcanzar las proporciones de nutrientes deseadas,
.. el doctor Howard debió incorporar una gran variedad de comidas
.. en la dieta. Cada comida provee varios de los nutrientes,
.. pero no en las proporciones correctas.
.. Por ejemplo, la leche descremada es una buena fuente de proteínas,
.. pero contiene mucho calcio.
.. Por esto, se usó harina de soya (que tiene poco calcio)
.. para proveer las proteínas; sin embargo,
.. tiene proporcionalmente mucha grasa,
.. por lo que se agregó suero de leche a la dieta,
.. que desafortunadamente contiene muchos carbohidratos...
.. como se hace evidente,
.. el delicado problema de balancear los nutrientes es complejo.
.. 
.. La siguiente tabla muestra el aporte en nutrientes
.. por cada 100 gramos de cada uno de los tres ingredientes
.. (leche descremada, harina de soya y suero de leche):
.. 
.. ============== ==== ==== ====
.. Nutrientes       LD   HS   SL
.. ============== ==== ==== ====
.. Proteínas        36   51   13
.. Carbohidratos    52   34   74
.. Grasas            0    7  1.1
.. ============== ==== ==== ====
.. 
.. La dieta de Cambridge debe proveer 33 gramos de proteínas,
.. 45 gramos de carbohidratos y 3 gramos de grasa.
.. 
.. Escriba un programa que muestre qué cantidades de ingredientes
.. se debe usar para satisfacer los requerimientos
.. de la dieta de Cambridge.
.. 
.. .. [Lay97] David C. Lay.
..            *Linear Algebra and Its Applications*.
..            Addison-Wesley, 1997.
