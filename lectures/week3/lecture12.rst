Lecture 12 - Tuples
-------------------

.. index:: tuple

A **tuple** is a sequence of grouped values.

A tuple is used to group several related values as a single value.

The data type that represents the tuple is called ``tuple``.
The ``tuple`` type is immutable: a tuple cannot be modified once created.

.. index:: tuple literal

A tuple can be created
setting comma separated values and in round brackets.
For example,
we can create a tuple with the first-name and last-name of a person::

    >>> person = ('John', 'Smith')
    >>> person
    ('John', 'Smith')

Unpacking tuples
~~~~~~~~~~~~~~~~

.. index:: unpacking

The tuple values can be recovered assigning the tuple to the corresponding variables.
This is called **unpacking tuples**::

    >>> person = ('John', 'Smith')
    >>> name, surname = person
    >>> name
    'John'

If you try to unpack the wrong number of values,
a value error occurs::

    >>> a, b, c = person
    Traceback (most recent call last):
File "<stdin>", line 1, in <module>
    ValueError: need more than 2 values to unpack

Also, it is possible to extract the values using their index::

    >>> person[1]
    'Smith'

``tuple`` comparison
~~~~~~~~~~~~~~~~~~~~~~

Two tuples are the same
when they have the same size
and each of their items have the same value::

    >>> (1, 2) == (3 // 2, 1 + 1)
    True
    >>> (6, 1) == (6, 2)
    False
    >>> (6, 1) == (6, 1, 0)
    False

.. index:: lexicographic order

To determine if a tuple is smaller than other,
the rule called **lexicographic order** is used.
If the items in the first position from both tuples are different,
comparing them determines the order of the tuples::

    >>> (1, 4, 7) < (2, 0, 0, 1)
    True
    >>> (1, 9, 10) < (0, 5)
    False

The first comparison is  ``True`` because ``1 < 2``.
The second comparison is ``False`` because ``1 > 0``.
No matter the value of the following values
or if a tuple has more elements than the other.

If the first position items are the same,
then the same comparison is used with the next value::

    >>> (6, 1, 8) < (6, 2, 8)
    True
    >>> (6, 1, 8) < (6, 0)
    False

The first comparison is  ``True`` because ``6 == 6`` and ``1 < 2``.
The second comparison is ``False`` because ``6 == 6`` and ``1 > 0``.

If the respective items continue being the same,
we continue comparing with the next values.
If a tuple runs out of items to compare before the other,
then it is immediately smaller than the other::

    >>> (1, 2) < (1, 2 ,4)
    True
    >>> (1, 3) < (1, 2, 4)
    False

The first comparison is ``True`` because ``1 == 1``, ``2 == 2``
and, at this point, all the elements from the first tuple have been compared.
The second comparison is ``False`` because ``1 == 1`` and ``3 < 2``;
in this case, it does reach the outcome before any of the tuples run out of elements.

This comparison method is the same used to sort words in alphabetic order.
(for example, in directories and dictionaries)::

    >>> 'car' < 'carousel'
    True
    >>> 'car' < 'cars'
    True
    >>> 'mon' < 'month' < 'monthly''
    True

Exercises
~~~~~~~~~

#. In the card games, a card has two attributes:
   a value (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q o K) and
   a suit (♥, ♠, ♦ o ♣).     
     
   In a program, a card can be represented as a tuple
   of two elements: the value and the suit.
   The value is a number from 1 to 13, and the suit is a string ('H', 'C', 'S' or 'D').
     
   A hand can be represented as a set of cards.
   For example, we can represented the hand 5♣ 2♥ 1♠ Q♥ K♣ as the next way:
     
   ::   
     
       hand = {(5, 'C'), (2, 'H'), (1, 'S'), (12, 'H'), (13, 'C')}  
     
   In the `Carioca`_ a straight is a hand with four cards which have the same suit and have consecutives values.
     
   .. _Carioca: http://en.wikipedia.org/wiki/Carioca_(card_game)

   For example:     
     
   * 3♥ 6♥ 5♥ 4♥ is a straight, because all the card have the suit ♥ and their consecutives values
     are from 3 to 6.
   * 3♣ 6♦ 5♦ 4♥ is not a straight, because the cards have different suits.  
   * 3♣ A♣ J♣ 5♣ is not a straight, because the values are not consecutives.
   * 3♠ 4♠ 5♠ is not a straight, because the hand does not have four cards.
     
     
   Write a function called *is_straight(hand)* which indicates if the hand is or not a straight.
  
   ::   
   
        >>> is_straight({(3,'C'), (6, 'C'), (5, 'C'), (4, 'C')})  
        True    
        >>> is_straight({(3,'T'), (6, 'D'), (5, 'D'), (4, 'C')})  
        False   
        >>> is_straight({(3,'T'), (1, 'T'), (11, 'T'), (5, 'T'))  
        False   
        >>> is_straight({(3,'C'), (4, 'C'), (5, 'C')})
        False    

#. En los juegos de naipes,
   una carta tiene dos atributos:
   un valor (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K)     
   y una pinta (♥, ♦, ♣, ♠).     
   
   En un programa,   
   el valor puede ser representado como un número  
   del 1 al 13,
   y la pinta como un string:    
   ♥ → ``'H'``,
   ♦ → ``'D'``,
   ♣ → ``'C'`` and     
   ♠ → ``'S'``.
   
   Una carta puede ser representada    
   como una tupla de dos elementos:    
   el valor y la pinta::   
   
 carta1 = (5, 'T')   
 carta2 = (10, 'D')  
   
   Para simplificar, 
   se puede representar el as como un 1,     
   y los «monos» J, Q y K como 11, 12 y 13:: 
   
 # as de picas y reina de corazones    
 carta3 = (1, 'P')   
 carta4 = (12, 'C')  
   
   En el juego de póker,   
   una mano tiene cinco cartas,  
   lo que en un programa vendría a ser 
   un conjunto de cinco tuplas:: 
   
 mano = {(1, 'P'), (1, 'C'), (1, 'T'), (13, 'D'), (12, 'P')}   
   
   #. Un *full* es una mano en que tres cartas tienen un valor común,
y las otras dos tienen otro valor común.     
Escriba una función que indique si la mano es un full::  
   
 >>> mano_1 = {(1, 'P'), (1, 'C'), (6, 'T'), (1, 'D'), (6, 'D')}     
 >>> mano_2 = {(2, 'T'), (1, 'C'), (12, 'C'), (1, 'D'), (6, 'D')}    
 >>> es_full(mano_1) 
 True     
 >>> es_full(mano_2) 
 False   
   
   #. Un *color* es una mano en que todas las cartas tienen la misma pinta.
Escriba una función que indique si la mano es un color:: 
   
 >>> mano_1 = {(8, 'P'), (13, 'P'), (4, 'P'), (9, 'P'), (2, 'P')}    
 >>> mano_2 = {(12, 'T'), (1, 'C'), (5, 'C'), (2, 'C'), (2, 'D')}    
 >>> es_color(mano_1)
 True    
 >>> es_color(mano_2)
 False   
   
   #. Una *escalera* es una mano en que las cartas tienen valores consecutivos   
(por ejemplo: 5, 6, 7, 8 y 9).   
Escriba una función que indique si la mano es una escalera::   
   
 >>> mano_1 = {(4, 'P'), (7, 'C'), (3, 'C'), (6, 'T'), (5, 'T')}     
 >>> mano_2 = {(12, 'T'), (7, 'C'), (3, 'C'), (12, 'C'), (5, 'T')}   
 >>> es_escalera(mano_1)   
 True    
 >>> es_escalera(mano_2)   
 False   
   
   #. Escriba el resto de las funciones
para identificar `el resto de las manos`_ del póker.     
   
.. _el resto de las manos: http://www.poquer.com.es/ranking.html 

#. Un partido de fútbol entre dos equipos    
   puede ser representado como una tupla de dos equipos::
   
 >>> partido = ('Chile', 'España')     
   
   El resultado del partido
   puede ser representado como una tupla con los goles   
   marcados por cada equipo::    
   
 >>> resultado = (4, 1)    
   
   Todos los partidos de un campeonato 
   pueden ser representados como un diccionario    
   que asocia a cada partido un resultado::  
   
 >>> campeonato = {  
 ...     ('Honduras', 'Chile'):    (1, 4),   
 ...     ('España',   'Suiza'):    (1, 1),   
 ...     ('Chile',    'Suiza'):    (2, 0),   
 ...     ('España',   'Honduras'): (1, 0),   
 ...     ('Chile',    'España'):   (5, 5),   
 ...     ('Suiza',    'Honduras'): (1, 2);   
 ... }   
   
   #. Escriba una función ``equipos(campeonato)``  
que entregue el conjunto de los equipos
que participaron del campeonato::
   
 >>> equipos(campeonato)   
 {'Chile', 'Honduras', 'Suiza', 'España'}    
   
   #. Escriba una función ``nro_empates(campeonato)``    
que cuente cuántos partidos del campeonato   
terminaron en empate::     
   
 >>> nro_empates(campeonato)     
 2   
   #. Cuando un equipo gana un partido, recibe 3 puntos; 
cuando empata, recibe 1 punto, y cuando pierde, no recibe ninguno.   
Escriba una función ``puntos(equipo, campeonato)`` 
que entregue cuántos puntos obtuvo el equipo 
en el campeonato::   
   
 >>> puntos('Chile', campeonato) 
 7 
 >>> puntos('Honduras', campeonato)    
 3 
   
   #. La diferencia de goles de un equipo    
es la suma de los goles que hizo 
menos la suma de los goles que le hicieron.  
Escriba una función ``dg(equipo, campeonato)``     
que entregue la diferencia de goles    
del equipo en el campeonato::    
   
 >>> dg('Chile', campeonato)     
 5 
 >>> dg('Honduras', campeonato)  
 -3
   
   #. Escriba una función ``mejor_partido(campeonato)``  
que entregue cuál fue el partido con más goles::   
   
 >>> mejor_partido(campeonato)   
 ('Chile', 'España')   
   
   #. Escriba una función ``tabla_de_posiciones(campeonato)``  
que retorne una lista de tuplas  
``(equipo, puntaje, diferencia_de_goles)``   
ordenada por puntaje de mayor a menor. 
Los equipos con el mismo puntaje 
deben estar ordenados por diferencia de goles
de mayor a menor::   
   
 >>> tabla_de_posiciones(campeonato)   
 [('España', 6, 2), ('Chile', 6, 1), ('Suiza', 4, 0), ('Honduras', 1, -3)] 

    
#. Las fechas pueden ser representadas 
   como tuplas ``(año, mes, dia)``.    
   
   Para asociar a cada persona su fecha de nacimiento,   
   se puede usar un diccionario::
   
 >>> n = {     
 ...     'Pepito': (1990, 10, 20),     
 ...     'Yayita': (1992, 3, 3), 
 ...     'Panchito': (1989, 10, 20),   
 ...     'Perica': (1989, 12, 8),
 ...     'Fulanita': (1991, 2, 14),    
 ... }   
   
   **Ejercicio 1:**  
   escriba una función ``mismo_dia(fecha1, fecha2)``     
   que indique si las dos fechas ocurren el mismo día del año  
   (aunque sea en años diferentes)::   
   
 >>> mismo_dia((2010, 6, 11), (1990, 6, 11)) 
 True    
 >>> mismo_dia((1981, 8, 12), (1981, 5, 12)) 
 False   
   
   **Ejercicio 2:**  
   escriba una función ``mas_viejo(n)``
   que indique quién es la persona más vieja 
   según las fechas de nacimiento del diccionario ``n``::
   
 >>> mas_viejo(n)    
 'Panchito'    
   
   **Ejercicio 3:**  
   escriba una función ``primer_cumple(n)``  
   que indique quién es la persona     
   que tiene el primer cumpleaños del año::  
   
 >>> primer_cumple(n)
 'Fulanita'    

#. Una recta en el plano está descrita por la ecuación:  
   
   .. math::   
   
 y = mx + b,   
   
   donde `m` es la *pendiente*   
   y `b` es el *intercepto*.     
   Todos los puntos de la recta  
   satisfacen esta ecuación.     
   
   En un programa,   
   una recta puede ser representada    
   como una tupla ``(m, b)``.    
   
   Los algoritmos para resolver los siguientes ejercicios
   seguramente usted los aprendió en el colegio.   
   Si no los recuerda,     
   puede buscarlos en su libro de matemáticas favorito   
   o en internet.    
   
   #. Escriba una función ``punto_en_recta(p, r)`` 
que indique si el punto ``p`` está en la recta ``r``::   
   
 >>> recta = (2, -1) 
 >>> punto_en_recta((2, 3), recta)     
 True    
 >>> punto_en_recta((0, -1), recta)    
 True    
 >>> punto_en_recta((1, 2), recta)     
 False   
   
   #. Escriba una función ``son_paralelas(r1, r2)``
que indique si las rectas ``r1`` y ``r2`` son paralelas, 
es decir, no se intersectan en ningún punto. 
   
   #. Escriba una función ``recta_que_pasa_por(p1, p2)`` 
que entregue la recta que pasa por los puntos ``p1`` y ``p2``::
   
 >>> recta_que_pasa_por((-2, 4), (4, 1))     
 (-0.5, 3.0)   
   
Puede comprobar que la función está correcta 
verificando que ambos puntos están en la recta obtenida:: 
   
 >>> p1 = (-2, 4)    
 >>> p2 = (4, 1)     
 >>> r = recta_que_pasa_por(p1, p2)    
 >>> punto_en_recta(p1, r) 
 True    
 >>> punto_en_recta(p2, r) 
 True    
   
   #. Escriba una función ``punto_de_interseccion(r1, r2)``    
que entregue el punto donde las dos rectas se `intersectan`_:: 
   
 >>> r1 = (2, 1)     
 >>> r2 = (-1, 4)    
 >>> punto_de_interseccion(r1, r2)     
 (1.0, 3.0)    
   
Si las rectas son paralelas,     
la función debe retornar ``None``.     
   
   .. _intersectan: http://www.mieres.uniovi.es/egi/dao/apuntes/planos_y_coordenadas.html

#. Para este problema,
   consideraremos las siguientes características de una persona:     
   
   * nombre,   
   * género (masculino o femenino),    
   * edad,     
   * música favorita, y    
   * signo zodiacal. 
   
   En el programa a realizar,    
   una persona será representada como una tupla::  
   
     persona_1 = ('Pepito', 'M', 27, 'rock', 'leo')
     persona_2 = ('Yayita', 'F', 23, 'cumbia', 'virgo')  
   
   Dos personas son compatibles  
   si:   
   
   * son de géneros opuestos (un hombre y una mujer),    
   * tienen menos de diez años de diferencia,
   * les gusta la misma música, y
   * sus signos zodiacales son compatibles.  
   
   Para saber los signos compatibles,  
   existe un conjunto ``signos_compatibles`` 
   que tiene tuplas ``(signo_mujer, signo_hombre)``,     
   que `usted puede descargar aquí`_.  
   Si una tupla está en el conjunto,   
   significa que los signos son compatibles::
   
       >>> ('aries', 'tauro') in signos_compatibles
       True    
   
       # Significa que mujer aries     
       # es compatible con hombre tauro.     
   
       >>> ('capricornio', 'libra') in signos_compatibles
       False   
   
       # Significa que mujer capricornio     
       # no es compatible con hombre libra.
   
   Escriba una función ``compatibles(p1, p2)``     
   que indique si dos personas son compatibles o no.     
   
   .. _usted puede descargar aquí: ../../_static/signos.py 
