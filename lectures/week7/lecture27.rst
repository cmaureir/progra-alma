Lecture 27 - NumPy arrays (part III)
-------------------------------------

Products between arrays
========================

Remember that a **vector** is a one dimension array synonymous,
and a **matrix** is a synonymous of a bi-dimensional array.

Inner product (vector-vector)
=============================

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
======================

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
======================

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
=========================

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

.. 
.. 
.. Rotar matrices
.. ==============
.. 
.. #. Escriba la función ``rotar90(a)``
..    que retorne el arreglo ``a``
..    rotado 90 grados en el sentido contrario
..    a las agujas del reloj::
.. 
..       >>> a = arange(12).reshape((3, 4))
..       >>> a
..       array([[ 0,  1,  2,  3],
..              [ 4,  5,  6,  7],
..              [ 8,  9, 10, 11]])
..       >>> rotar90(a)
..       array([[ 3,  7, 11],
..              [ 2,  6, 10],
..              [ 1,  5,  9],
..              [ 0,  4,  8]])
.. 
..    Hay dos maneras de hacerlo:
..    la larga (usando ciclos anidados)
..    y la corta (usando operaciones de arreglos).
..    Trate de hacerlo de las dos maneras.
.. 
.. #. Escriba las funciones ``rotar180(a)`` y ``rotar270(a)``::
.. 
..       >>> rotar180(a)
..       array([[11, 10,  9,  8],
..              [ 7,  6,  5,  4],
..              [ 3,  2,  1,  0]])
..       >>> rotar270(a)
..       array([[ 8,  4,  0],
..              [ 9,  5,  1],
..              [10,  6,  2],
..              [11,  7,  3]])
.. 
..    Hay tres maneras de hacerlo:
..    la larga (usando ciclos anidados),
..    la corta (usando operaciones de arreglos)
..    y la astuta.
..    Trate de hacerlo de las tres maneras.
.. 
.. #. Escriba el  módulo ``rotar.py``
..    que contenga estas tres funciones.
..    Le será útil más adelante::
.. 
..       >>> from rotar import rotar90
..       >>> a = array([[6, 3, 8],
..       ...            [9, 2, 0]])
..       >>> rotar90(a)
..       array([[8, 0],
..              [3, 2],
..              [6, 9]])
.. 
.. Sudoku
.. ======
.. 
.. El sudoku es un puzzle que consiste en llenar una grilla de 9 × 9
.. con los dígitos del 1 al 9, de modo que no haya ningún valor repetido
.. en cada fila, en cada columna y en cada uno de las regiones de 3 × 3
.. marcadas por las líneas más gruesas.
.. 
.. El sudoku sin resolver tiene algunos de los dígitos puestos de antemano en la grilla.
.. Cuando el puzzle ha sido resuelto, todas las casillas tienen un dígito,
.. y entre todos satisfacen las condiciones señaladas.
.. 
.. .. image:: ../../diagramas/sudoku.png
.. 
.. En un programa,
.. un sudoku resuelto puede ser guardado en un arreglo de 9 × 9::
.. 
..     from numpy import array
..     sr = array([[4, 2, 6, 5, 7, 1, 3, 9, 8],
..                 [8, 5, 7, 2, 9, 3, 1, 4, 6],
..                 [1, 3, 9, 4, 6, 8, 2, 7, 5],
..                 [9, 7, 1, 3, 8, 5, 6, 2, 4],
..                 [5, 4, 3, 7, 2, 6, 8, 1, 9],
..                 [6, 8, 2, 1, 4, 9, 7, 5, 3],
..                 [7, 9, 4, 6, 3, 2, 5, 8, 1],
..                 [2, 6, 5, 8, 1, 4, 9, 3, 7],
..                 [3, 1, 8, 9, 5, 7, 4, 6, 2]])
.. 
.. Escriba la función ``solucion_es_correcta(sudoku)``
.. que reciba como parámetro un arreglo de 9 × 9
.. representando un sudoku resuelto,
.. y que indique si la solución es correcta
.. (es decir, si no hay elementos repetidos
.. en filas, columnas y regiones)::
.. 
..     >>> solucion_es_correcta(s)
..     True
..     >>> s[0, 0] = 9
..     >>> solucion_es_correcta(s)
..     False
.. 
.. .. 2. (¡Difícil!).
.. ..    Un sudoku sin resolver puede ser representado como un arreglo
.. ..    donde las casillas vacías se marcan con el número cero::
.. .. 
.. ..     s = array([[0, 2, 0, 5, 0, 1, 0, 9, 0],
.. ..                [8, 0, 0, 2, 0, 3, 0, 0, 6],
.. ..                [0, 3, 0, 0, 6, 0, 0, 7, 0],
.. ..                [0, 0, 1, 0, 0, 0, 6, 0, 0],
.. ..                [5, 4, 0, 0, 0, 0, 0, 1, 9],
.. ..                [0, 0, 2, 0, 0, 0, 7, 0, 0],
.. ..                [0, 9, 0, 0, 3, 0, 0, 8, 0],
.. ..                [2, 0, 0, 8, 0, 4, 0, 0, 7],
.. ..                [0, 1, 0, 9, 0, 7, 0, 6, 0]])
.. .. 
.. ..    Escriba una función ``resolver(sudoku)``
.. ..    que reciba un sudoku sin resolver
.. ..    y retorne el sudoku resuelto::
.. .. 
.. ..     >>> resolver(s)
.. ..     array([[4, 2, 6, 5, 7, 1, 3, 9, 8],
.. ..            [8, 5, 7, 2, 9, 3, 1, 4, 6],
.. ..            [1, 3, 9, 4, 6, 8, 2, 7, 5],
.. ..            [9, 7, 1, 3, 8, 5, 6, 2, 4],
.. ..            [5, 4, 3, 7, 2, 6, 8, 1, 9],
.. ..            [6, 8, 2, 1, 4, 9, 7, 5, 3],
.. ..            [7, 9, 4, 6, 3, 2, 5, 8, 1],
.. ..            [2, 6, 5, 8, 1, 4, 9, 3, 7],
.. ..            [3, 1, 8, 9, 5, 7, 4, 6, 2]])
.. .. 
.. ..    Sugerencia: en vez de intentar resolver el sudoku completo,
.. ..    intente resolver sólo algunas de las casillas
.. ..    (las más sencillas).
.. Matrices especiales
.. ===================
.. 
.. #. Una matriz ``a`` es **simétrica**
..    si para todo par de índices ``i`` y ``j``
..    se cumple que ``a[i, j] == a[j, i]``.
.. 
..    Escriba la función ``es_simetrica(a)``
..    que indique si la matriz ``a``
..    es simétrica o no.
.. 
..    Cree algunas matrices simétricas
..    y otras que no lo sean
..    para probar su función.
.. 
.. #. Una matriz ``a`` es **antisimétrica**
..    si para todo par de índices ``i`` y ``j``
..    se cumple que ``a[i, j] == -a[j, i]``
..    (note el signo menos).
.. 
..    Escriba la función ``es_antisimetrica(a)``
..    que indique si la matriz ``a``
..    es antisimétrica o no.
.. 
..    Cree algunas matrices antisimétricas
..    y otras que no lo sean
..    para probar su función.
.. 
.. #. Una matriz ``a`` es **diagonal**
..    si todos sus elementos que no están en la diagonal principal
..    tienen el valor cero.
..    Por ejemplo,
..    la siguiente matriz es diagonal:
.. 
..    .. math:: 
.. 
..      \begin{bmatrix}
..        9 & 0 & 0 & 0 \\
..        0 & 2 & 0 & 0 \\
..        0 & 0 & 0 & 0 \\
..        0 & 0 & 0 & -1 \\
..      \end{bmatrix}
.. 
..    Escriba la función ``es_diagonal(a)``
..    que indique si la matriz ``a``
..    es diagonal o no.
.. 
.. #. Una matriz ``a`` es **triangular superior**
..    si todos sus elementos que están bajo la diagonal principal
..    tienen el valor cero.
..    Por ejemplo,
..    la siguiente matriz es triangular superior:
.. 
..    .. math:: 
.. 
..      \begin{bmatrix}
..        9 & 1 & 0 & 4 \\
..        0 & 2 & 8 & -3 \\
..        0 & 0 & 0 & 7 \\
..        0 & 0 & 0 & -1 \\
..      \end{bmatrix}
.. 
..    Escriba la función ``es_triangular_superior(a)``
..    que indique si la matriz ``a``
..    es trangular superior o no.
.. 
.. #. No es dificil adivinar
..    qué es lo que es
..    una matriz **triangular inferior**.
..    Escriba la función ``es_triangular_inferior(a)``.
..    Para ahorrarse trabajo,
..    llame a ``es_triangular_superior`` desde dentro de la función.
.. 
.. #. Una matriz es **idempotente**
..    si el resultado del producto matricial consigo misma
..    es la misma matriz.
..    Por ejemplo:
.. 
..    .. math::
.. 
..         \begin{bmatrix}
..            2 & -2 & -4 \\
..           -1 &  3 &  4 \\
..            1 & -2 & -3 \\
..         \end{bmatrix}
..         \begin{bmatrix}
..            2 & -2 & -4 \\
..           -1 &  3 &  4 \\
..            1 & -2 & -3 \\
..         \end{bmatrix}
..         =
..         \begin{bmatrix}
..            2 & -2 & -4 \\
..           -1 &  3 &  4 \\
..            1 & -2 & -3 \\
..         \end{bmatrix}
.. 
..    Escriba la función ``es_idempotente(a)``
..    que indique si la matriz ``a``
..    es idempotente o no.
.. 
.. #. Se dice que dos matrices *A* y *B* **conmutan**
..    si los productos matriciales entre *A* y *B*
..    y entre *B* y *A* son iguales.
.. 
..    Por ejemplo, estas dos matrices sí conmutan:
.. 
..    .. math::
.. 
..        \begin{bmatrix}
..          1 & 3 \\ 3 & 2 \\
..        \end{bmatrix}
..        \begin{bmatrix}
..          -1 & 3 \\ 3 & 0 \\
..        \end{bmatrix} =
..        \begin{bmatrix}
..          -1 & 3 \\ 3 & 0 \\
..        \end{bmatrix}
..        \begin{bmatrix}
..          1 & 3 \\ 3 & 2 \\
..        \end{bmatrix} =
..        \begin{bmatrix}
..          8 & 3 \\ 3 & 9 \\
..        \end{bmatrix}
.. 
..    Escriba la función ``conmutan``
..    que indique si dos matrices conmutan o no.
..    Pruebe su función con estos ejemplos::
.. 
..        >>> a = array([[ 1, 3], [3, 2]])
..        >>> b = array([[-1, 3], [3, 0]])
..        >>> conmutan(a, b)
..        True
.. 
..        >>> a = array([[3, 1, 2], [9, 2, 4]])
..        >>> b = array([[1, 7], [2, 9]])
..        >>> conmutan(a, b)
..        False
.. 
.. Buscaminas
.. ==========
.. 
.. El juego del buscaminas
.. se basa en una grilla rectangular
.. que representa un campo minado.
.. Algunas de las casillas de la grilla
.. tienen una mina, y otras no.
.. El juego consiste en descubrir
.. todas las casillas que no tienen minas.
.. 
.. En un programa,
.. podemos representar un campo de buscaminas
.. como un arreglo en el que las casillas minadas
.. están marcadas con el valor −1,
.. y las demás casillas con el valor 0::
.. 
..     >>> from numpy import *
..     >>> campo = array([[ 0,  0, -1,  0,  0,  0,  0,  0],
..                        [-1,  0,  0,  0, -1,  0,  0,  0],
..                        [ 0,  0,  0,  0, -1,  0,  0, -1],
..                        [ 0,  0, -1,  0,  0,  0,  0,  0],
..                        [ 0,  0,  0,  0,  0,  0, -1,  0],
..                        [ 0, -1,  0,  0, -1,  0,  0,  0],
..                        [ 0,  0, -1,  0,  0,  0,  0,  0],
..                        [ 0,  0,  0,  0,  0,  0,  0,  0]])
.. 
.. 
.. 
.. #. Escriba la función ``crear_campo(forma, n)``,
..    ``forma`` es una tupla ``(filas, columnas)``,
..    que retorne un nuevo campo aleatorio con la forma indicada
..    que tenga ``n`` minas.
.. 
..    Hágalo en los siguientes pasos:
.. 
..    a. Construya un vector de tamaño ``filas * columnas``
..       que tenga ``n`` veces el valor −1, y a continuación sólo ceros.
..    b. Importe la función ``shuffle`` desde el módulo ``numpy.random``.
..       Esta función desordena (o «baraja») los elementos de un arreglo.
..    c. Desordene los elementos del vector que creó.
..    d. Cambie la forma del vector.
.. 
..    ::
.. 
..       >>> crear_campo((4, 4), 5)
..       array([[-1,  0,  0,  0],
..              [ 0,  0,  0,  0],
..              [ 0, -1, -1,  0],
..              [ 0, -1, -1,  0]])
..       >>> crear_campo((4, 4), 5)
..       array([[ 0,  0, -1,  0],
..              [ 0,  0,  0, -1],
..              [-1,  0,  0,  0],
..              [ 0,  0, -1, -1]])
..       >>> crear_campo((4, 4), 5)
..       array([[ 0,  0,  0, -1],
..              [ 0,  0, -1, -1],
..              [-1,  0,  0,  0],
..              [ 0,  0, -1,  0]])
.. 
.. #. Al descubrir una casilla no minada,
..    en ella aparece un número,
..    que indica la cantidad de minas
..    que hay en sus ocho casillas vecinas.
.. 
..    Escriba la función ``descubrir(campo)``
..    que modifique el campo
..    poniendo en cada casilla
..    la cantidad de minas vecinas::
.. 
..        >>> c = crear_campo((4, 4), 5)
..        >>> c
..        array([[ 0,  0, -1, -1],
..               [ 0,  0, -1,  0],
..               [ 0,  0,  0, -1],
..               [ 0,  0,  0, -1]])
..        >>> descubrir(c)
..        >>> c
..        array([[ 0,  2, -1, -1],
..               [ 0,  2, -1,  4],
..               [ 0,  1,  3, -1],
..               [ 0,  0,  2, -1]])
.. 
.. Barman
.. ------
.. .. Propuesto por Mabel Bielenberg
.. 
.. Para preparar aperitivos,
.. un barman almacena en tres baldes
.. distintas medidas de vino, ginebra y jugo de limón,
.. según la siguiente tabla:
.. 
.. ======= ============= ============= =============
.. Balde   Vino          Ginebra       Jugo de limón
.. ======= ============= ============= =============
.. A                  20            30            50
.. B                  30            20            60
.. C                  30            30            32
.. ======= ============= ============= =============
.. 
.. Por otro lado,
.. se tiene la información de los precios por litro
.. de cada líquido:
.. 
.. ============= ========
.. Líquido       Precio
.. ============= ========
.. Vino                 5
.. Ginebra             45
.. Jugo de limón       10
.. ============= ========
.. 
.. #. Escriba un programa que muestre
..    cuál es el precio de cada uno de los baldes.
.. 
.. #. Escriba un programa
..    que muestre el precio total de
..    10 baldes A, 4 baldes B y 5 baldes C.
.. 
.. Producción de autos
.. ===================
.. .. Propuesto por Mabel Bielenberg
.. 
.. Una fábrica de autos produce tres modelos:
.. sedán, camioneta y económico.
.. Cada auto necesita para su producción
.. materiales, personal, impuestos y transporte.
.. Los costos en unidades por cada concepto
.. son los siguientes:
.. 
.. ========== ========== ========== ==========
.. (Costos)   Sedán      Camioneta  Económico
.. ========== ========== ========== ==========
.. Material            7          8          5
.. Personal           10          9          7
.. Impuestos           5          3          2
.. Transporte          2          3          1
.. ========== ========== ========== ==========
.. 
.. Semanalmente, se producen
.. 60 sedanes, 40 camionetas y 90 económicos.
.. 
.. Los costos de una unidad de
.. material, personal, impuestos y transporte
.. son respectivamente 5, 15, 7 y 2.
.. 
.. Escriba un programa que muestre:
.. 
.. * las unidades semanales necesarias de
..   material, personal, impuestos y transporte,
.. * el costo total de un auto de cada modelo,
.. * el costo total de la producción semanal.
.. 
.. Informe de producción de gas
.. ============================
.. .. Propuesto por Mabel Bielenberg
.. 
.. En un informe anual de SansanoGas S.A.,
.. el presidente informa a sus accionistas
.. la cantidad anual de producción de barriles
.. de 50 litros de lubricantes
.. normal, extra y súper,
.. en sus dos refinerías:
.. 
.. ========= ======== ======== ========
.. Refinería Normal   Extra    Súper
.. ========= ======== ======== ========
.. A             3000     7000     2000
.. B             4000      500      600
.. ========= ======== ======== ========
.. 
.. Además, informa que en cada barril de 50 litros de lubricante
.. existe la siguiente composición en litros de
.. aceites finos, alquitrán y grasas residuales:
.. 
.. ================= ======== ======== ========
.. Componente        Normal   Extra    Súper
.. ================= ======== ======== ========
.. Aceites finos           10        5       35
.. Alquitrán               15        4       31
.. Grasas residuales       18        2       30
.. ================= ======== ======== ========
.. 
.. #. Escriba la función ``totales_anuales(a, b)``
..    que reciba como parámetros ambas matrices
..    y retorne un arreglo con los totales
..    de aceites finos, alquitrán y grasas residuales
..    presentes en la producción anual.
.. 
.. #. Escriba la función ``maximo_alquitran(a, b)``
..    que reciba como parámetros ambas matrices
..    y retorne el máximo de litros de alquitrán
..    consumidos por ambas refinerías.
.. 
.. #. Determine cuál es la matriz
..    que entrega el consumo de todos los elementos
..    que forman parte de un lubricante,
..    en cada refinería.
.. 
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
