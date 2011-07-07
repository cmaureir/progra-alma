Lecture 26 - NumPy arrays (part II)
-----------------------------------

Productos entre arreglos
========================

Recordemos que **vector** es sinónimo de arreglo de una dimensión,
y **matriz** es sinónimo de arreglo de dos dimensiones.


Producto interno (vector-vector)
--------------------------------
El **producto interno** entre dos vectores
es la suma de los productos entre elementos correspondientes:

.. image:: ../diagramas/producto-interno.png
   :align: center

El producto interno entre dos vectores
se obtiene usando la función ``dot``
provista por NumPy::

    >>> a = array([-2.8 , -0.88,  2.76,  1.3 ,  4.43])
    >>> b = array([ 0.25, -1.58,  1.32, -0.34, -4.22])
    >>> dot(a, b)
    -14.803

El producto interno es una operación muy común.
Por ejemplo, suele usarse para calcular totales::

    >>> precios = array([200, 100, 500, 400, 400, 150])
    >>> cantidades = array([1, 0, 0, 2, 1, 0])
    >>> total_a_pagar = dot(precios, cantidades)
    >>> total_a_pagar
    1400

También se usa para calcular promedios ponderados::

    >>> notas = array([45, 98, 32])
    >>> ponderaciones = array([30, 30, 40]) / 100.
    >>> nota_final = dot(notas, ponderaciones)
    >>> nota_final
    55.7

Producto matriz-vector
----------------------
El **producto matriz-vector**
es el vector de los productos internos
El producto matriz-vector puede ser visto
simplemente como varios productos internos
calculados de una sola vez.

Esta operación también es obtenida
usando la función ``dot``
entre las filas de la matriz y el vector:

.. image:: ../diagramas/matriz-vector.png
   :align: center

El producto matriz-vector puede ser visto
simplemente como varios productos internos
calculados de una sola vez.

Esta operación también es obtenida
usando la función ``dot``::

    >>> a = array([[-0.6,  4.8, -1.2],
                   [-2. , -3.6, -2.1],
                   [ 1.7,  4.9,  0. ]])
    >>> x = array([-0.6, -2. ,  1.7])
    >>> dot(a, x)
    array([-11.28,   4.83, -10.82])

Producto matriz-matriz
----------------------
El **producto matriz-matriz**
es la matriz de los productos internos
entre las filas de la primera matriz
y las columnas de la segunda:

.. image:: ../diagramas/matriz-matriz.png
   :align: center

Esta operación también es obtenida
usando la función ``dot``::

    >>> a = array([[ 2,  8],
                   [-3,  7],
                   [-8, -5]])
    >>> b array([[-3, -5, -6, -3],
                 [-9, -2,  3, -3]])
    >>> dot(a, b)
    array([[-78, -26,  12, -30],
           [-54,   1,  39, -12],
           [ 69,  50,  33,  39]])

La multiplicación de matrices
puede ser vista como varios productos matriz-vector
(usando como vectores todas las filas de la segunda matriz),
calculados de una sola vez.

En resumen,
al usar la función ``dot``,
la estructura del resultado
depende de cuáles son los parámetros pasados::

    dot(vector, vector) → número
    dot(matriz, vector) → vector
    dot(matriz, matriz) → matriz

Resolución de sistemas lineales
===============================

Repasemos el producto matriz-vector:

.. image:: ../diagramas/dieta-1.png
   :align: center

Esta operación tiene dos operandos:
una matriz y un vector.
El resultado es un vector.
A los operandos los denominaremos respectivamente ``A`` y ``x``,
y al resultado, ``b``.

Un problema recurrente en Ingeniería
consiste en obtener cuál es el vector ``x``
cuando ``A`` y ``b`` son dados:

.. image:: ../diagramas/dieta-2.png
   :align: center

La ecuación matricial `Ax = b` es una manera abreviada
de expresar un `sistema de ecuaciones lineales`_.
Por ejemplo,
la ecuación del diagrama
es equivalente al siguiente sistema de tres ecuaciones
que tiene las tres incógnitas `w`, `y` y `z`:

.. math::

    \begin{align}
      36w + 51y + 13z &= 3 \\
      52w + 34y + 74z &= 45 \\
             7y + 1.1z &= 33 \\
    \end{align}

.. _sistema de ecuaciones lineales: http://es.wikipedia.org/wiki/Sistema_de_ecuaciones_lineales

En matemáticas,
este sistema se representa matricialmente así:

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

La teoría detrás de la resolución de problemas de este tipo
usted la aprenderá en sus ramos de matemáticas.
Sin embargo,
como este tipo de problemas aparece a menudo en la práctica,
aprenderemos cómo obtener rápidamente la solución
usando Python.

Dentro de los varios módulos incluídos en NumPy
(por ejemplo, ya vimos ``numpy.random``),
está el módulo ``numpy.linalg``,
que provee algunas funciones que implementan algoritmos de álgebra lineal,
que es la rama de las matemáticas que estudia los problemas de este tipo.
En este módulo está la función ``solve``,
que entrega la solución ``x`` de un sistema
a partir de la matriz ``A`` y el vector ``b``::

    >>> a = array([[ 36. ,  51. ,  13. ],
    ...            [ 52. ,  34. ,  74. ],
    ...            [  0. ,   7. ,   1.1]])
    >>> b = array([  3.,  45.,  33.])
    >>> x = solve(a, b)
    >>> x
    array([-7.10829222,  4.13213834,  3.70457422])

Podemos ver que el vector ``x`` en efecto
satisface la ecuación ``Ax = b``::

    >>> dot(a, x)
    array([  3.,  45.,  33.])
    >>> b
    array([  3.,  45.,  33.])

Sin embargo, es importante tener en cuenta que
los valores de tipo real
casi nunca están representados de manera exacta en el computador,
y que el resultado de un algoritmo que involucra muchas operaciones
puede sufrir de algunos errores de redondeo.
Por esto mismo,
puede ocurrir que aunque los resultados se vean iguales en la consola,
los datos obtenidos son sólo aproximaciones
y no exactamente los mismos valores::

    >>> (dot(a, x) == b).all()
    False

.. 
.. Exercises
.. ---------
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
