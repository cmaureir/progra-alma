Lecture 18 - Higher-order functions
------------------------------------

..  map, reduce, filter,
..        * funciones como parametros (ver diapo 11)
..        * decorators
..           * memoize
..           * metodo statico

List comprehensions
~~~~~~~~~~~~~~~~~~~
.. 
.. List comprehensions provide a concise way to create lists without resorting to use of map(), filter() and/or lambda. The resulting list definition tends often to be clearer than lists built using those constructs. Each list comprehension consists of an expression followed by a for clause, then zero or more for or if clauses. The result will be a list resulting from evaluating the expression in the context of the for and if clauses which follow it. If the expression would evaluate to a tuple, it must be parenthesized.
.. 
.. >>> freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
.. >>> [weapon.strip() for weapon in freshfruit]
.. ['banana', 'loganberry', 'passion fruit']
.. >>> vec = [2, 4, 6]
.. >>> [3*x for x in vec]
.. [6, 12, 18]
.. >>> [3*x for x in vec if x > 3]
.. [12, 18]
.. >>> [3*x for x in vec if x < 2]
.. []
.. >>> [[x,x**2] for x in vec]
.. [[2, 4], [4, 16], [6, 36]]
.. >>> [x, x**2 for x in vec]  # error - parens required for tuples
..   File "<stdin>", line 1, in ?
..     [x, x**2 for x in vec]
..                ^
.. SyntaxError: invalid syntax
.. >>> [(x, x**2) for x in vec]
.. [(2, 4), (4, 16), (6, 36)]
.. >>> vec1 = [2, 4, 6]
.. >>> vec2 = [4, 3, -9]
.. >>> [x*y for x in vec1 for y in vec2]
.. [8, 6, -18, 16, 12, -36, 24, 18, -54]
.. >>> [x+y for x in vec1 for y in vec2]
.. [6, 5, -7, 8, 7, -5, 10, 9, -3]
.. >>> [vec1[i]*vec2[i] for i in range(len(vec1))]
.. [8, 12, -54]
.. List comprehensions are much more flexible than map() and can be applied to complex expressions and nested functions:
.. 
.. >>> [str(round(355/113.0, i)) for i in range(1,6)]
.. ['3.1', '3.14', '3.142', '3.1416', '3.14159']
.. 
.. 
.. 
.. When to Use List Comprehension
.. We typically should use simple for loops when getting started with Python, and map. Use comprehension where they are easy to apply. However, there is a substantial performance advantage to use list comprehension. The map calls are roughly twice as fast as equivalent for loops. List comprehensions are usually slightly faster than map calls. This speed difference is largely due to the fact that map and list comprehensions run at C language speed inside the interpreter. It is much faster that stepping through Python for loop code within the Python Virtual Machine (PVM).
.. 
.. However, for loops make logic more explicit, we may want to use them on the grounds of simplicity. On the other hand, map and list comprehensions are worth knowing and using for simpler kinds of iterations if the speed of application is an important factor.




Function as parameters
~~~~~~~~~~~~~~~~~~~~~~

..   En Python las funciones son valores como cualquier otro.
..   Por ejemplo, se les puede crear un nuevo nombre
..   con una simple asignación: \li!f = factorial!.
..   Una de las ventajas que tiene esto
..   es que es posible crear funciones que reciben a otras funciones como parámetro.
.. 
..   En el ejemplo de la diapositiva,
..   se define una función \li!sumar!
..   que entrega la suma de todos los valores menores que \li!n!,
..   pero antes aplicándoles una función,
..   la que será referida con el nombre \li!f!.
.. 
..   El programa llama a la función \li!sumar! tres veces,
..   y en cada una de ellas pasa una función distinta como parámetro.
..   De esta forma, se puede usar una única función
..   para calcular la suma de los valores hasta 1000,
..   la suma de los cuadrados hasta 1000
..   y la suma de los cubos hasta 1000.
.. 
.. 
.. 
.. 
.. def sumar(n, f):
.. 	s = 0
.. 	for i in range(n):
.. 		s = s + f(i)
.. 	return s
.. 
.. def identidad(x):
.. 	return x
.. 
.. def cuadrado(x):
.. 	return x ** 2
.. 
.. def cubo(x):
.. 	return x ** 3
.. 
.. print sumar(1000, identidad)
.. print sumar(1000, cuadrado)
.. print sumar(1000, cubo)






`map()` function
~~~~~~~~~~~~~~~~
.. 
.. map(function, iterable, ...)
.. Apply function to every item of iterable and return a list of the results. If additional iterable arguments are passed, function must take that many arguments and is applied to the items from all iterables in parallel. If one iterable is shorter than another it is assumed to be extended with None items. If function is None, the identity function is assumed; if there are multiple arguments, map() returns a list consisting of tuples containing the corresponding items from all iterables (a kind of transpose operation). The iterable arguments may be a sequence or any iterable object; the result is always a list.
.. 
.. 
.. 
.. map(function, sequence) calls function(item) for each of the sequence’s items and returns a list of the return values. For example, to compute some cubes:
.. 
.. >>> def cube(x): return x*x*x
.. ...
.. >>> map(cube, range(1, 11))
.. [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
.. 
.. More than one sequence may be passed; the function must then have as many arguments as there are sequences and is called with the corresponding item from each sequence (or None if some sequence is shorter than another). For example:
.. 
.. >>> seq = range(8)
.. >>> def add(x, y): return x+y
.. ...
.. >>> map(add, seq, seq)
.. [0, 2, 4, 6, 8, 10, 12, 14]
.. 
.. 
.. 
.. One of the common things we do with list and other sequences is applying an operation to each item and collect the result. For example, updating all the items in a list can be done easily with a for loop:
.. 
.. >>> items = [1, 2, 3, 4, 5]
.. >>> squared = []
.. >>> for x in items:
.. 	squared.append(x ** 2)
.. 
.. 	
.. >>> squared
.. [1, 4, 9, 16, 25]
.. >>> 
.. Since this is such a common operation. We have a built-in feature that does most of the work for us. The map(aFunction, aSequence) function applies a passed-in function to each item in an iterable object and returns a list containing all the function call results.
.. 
.. >>> items = [1, 2, 3, 4, 5]
.. >>> 
.. >>> def sqr(x): return x ** 2
.. 
.. >>> list(map(sqr, items))
.. [1, 4, 9, 16, 25]
.. >>> 
.. We passed in a user-defined function applied to each item in the list. map calls sqr on each list item and collects all the return values into a new list.
.. 
.. Because map expects a function to be passed in, it also happens to be one of the places where lambda routinely appears:
.. 
.. >>> list(map((lambda x: x **2), items))
.. [1, 4, 9, 16, 25]
.. >>> 
.. In the short example above, the lambda function squares each item in the items list.
.. 
.. Because such uses of map are equivalent to for loops, with an extra code we can always write a general mapping utility:
.. 
.. >>> def mymap(aFunc, aSeq):
.. 	result = []
.. 	for x in aSeq: result.append(aFunc(x))
.. 	return result
.. 
.. >>> list(map(sqr, [1, 2, 3]))
.. [1, 4, 9]
.. >>> mymap(sqr, [1, 2, 3])
.. [1, 4, 9]
.. >>> 
.. Since it's a built-in, map is always available and always works the same way. It also has some performance benefit because it is usually faster than a manually coded for loop. On top of those, map can be used in more advance way. For example, given multiple sequence arguments, it sends items taken form sequences in parallel as distinct arguments to the function:
.. 
.. >>> pow(3,5)
.. 243
.. >>> pow(2,10)
.. 1024
.. >>> pow(3,11)
.. 177147
.. >>> pow(4,12)
.. 16777216
.. >>> 
.. >>> list(map(pow,[2, 3, 4], [10, 11, 12]))
.. [1024, 177147, 16777216]
.. >>> 
.. As in the example above, with multiple sequences, map expects an N-argument function for N sequences. In the example, pow function takes two arguments on each call.
.. 
.. The map call is similar to the list comprehension expression. But map applies a function call to each item instead of an arbitrary expression. Because of this limitation, it is somewhat less general tool. In some cases, however, map may be faster to run than a list comprehension such as when mapping a built-in function. And map requires less coding.
.. 
.. 
.. 
.. 
.. 

`reduce()` function
~~~~~~~~~~~~~~~~~~~~

.. 
.. 
.. reduce(function, iterable[, initializer])
.. Apply function of two arguments cumulatively to the items of iterable, from left to right, so as to reduce the iterable to a single value. For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5). The left argument, x, is the accumulated value and the right argument, y, is the update value from the iterable. If the optional initializer is present, it is placed before the items of the iterable in the calculation, and serves as a default when the iterable is empty. If initializer is not given and iterable contains only one item, the first item is returned.
.. 
.. reduce(function, sequence) returns a single value constructed by calling the binary function function on the first two items of the sequence, then on the result and the next item, and so on. For example, to compute the sum of the numbers 1 through 10:
.. 
.. >>> def add(x,y): return x+y
.. ...
.. >>> reduce(add, range(1, 11))
.. 55
.. If there’s only one item in the sequence, its value is returned; if the sequence is empty, an exception is raised.
.. 
.. A third argument can be passed to indicate the starting value. In this case the starting value is returned for an empty sequence, and the function is first applied to the starting value and the first sequence item, then to the result and the next item, and so on. For example,
.. 
.. >>> def sum(seq):
.. ...     def add(x,y): return x+y
.. ...     return reduce(add, seq, 0)
.. ...
.. >>> sum(range(1, 11))
.. 55
.. >>> sum([])
.. 0
.. Don’t use this example’s definition of sum(): since summing numbers is such a common need, a built-in function sum(sequence) is already provided, and works exactly like this.
.. 
.. 
.. 
.. 
.. 
.. The reduce is in the functools in Python 3.0. It is more complex. It accepts an iterator to process, but it's not an iterator itself. It returns a single result:
.. 
.. >>> 
.. >>> from functools import reduce
.. >>> reduce( (lambda x, y: x * y), [1, 2, 3, 4] )
.. 24
.. >>> reduce( (lambda x, y: x / y), [1, 2, 3, 4] )
.. 0.041666666666666664
.. >>> 
.. At each step, reduce passes the current product or division, along with the next item from the list, to the passed-in lambda function. By default, the first item in the sequence initialized the starting value. Here's the for loop version of the first of these calls, with the multiplication hardcoded inside the loop:
.. 
.. >>> L = [1, 2, 3, 4]
.. >>> result = L[0]
.. >>> for x in L[1:]:
.. 	result = result * x
.. 
.. 	
.. >>> result
.. 24
.. >>> 
.. Let's make our own version of reduce.
.. 
.. >>> def myreduce(fnc, seq):
.. 	tally = seq[0]
.. 	for next in seq[1:]:
.. 		tally = fnc(tally, next)
.. 	return tally
.. 
.. >>> myreduce( (lambda x, y: x * y), [1, 2, 3, 4])
.. 24
.. >>> myreduce( (lambda x, y: x / y), [1, 2, 3, 4])
.. 0.041666666666666664
.. >>> 
.. The built-in reduce also allows an optional third argument placed before the items in the sequence to serve as a default result when the sequence is empty.
.. 
.. 
.. 
.. 
.. 

`filter()` function
~~~~~~~~~~~~~~~~~~~~
.. 
.. filter(function, iterable)
.. Construct a list from those elements of iterable for which function returns true. iterable may be either a sequence, a container which supports iteration, or an iterator. If iterable is a string or a tuple, the result also has that type; otherwise it is always a list. If function is None, the identity function is assumed, that is, all elements of iterable that are false are removed.
.. 
.. Note that filter(function, iterable) is equivalent to [item for item in iterable if function(item)] if function is not None and [item for item in iterable if item] if function is None.
.. 
.. See itertools.ifilter() and itertools.ifilterfalse() for iterator versions of this function, including a variation that filters for elements where the function returns false.
.. 
.. 
.. 
.. 
.. filter(function, sequence) returns a sequence consisting of those items from the sequence for which function(item) is true. If sequence is a string or tuple, the result will be of the same type; otherwise, it is always a list. For example, to compute primes up to 25:
.. 
.. >>> def f(x): return x % 2 != 0 and x % 3 != 0
.. ...
.. >>> filter(f, range(2, 25))
.. [5, 7, 11, 13, 17, 19, 23]
.. 
.. 
.. 
.. 
.. As an example, the following filter call picks out items in a sequence that are less than zero:
.. 
.. >>> list(range(-5,5))
.. [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
.. >>>
.. >>> list( filter((lambda x: x < 0), range(-5,5)))
.. [-5, -4, -3, -2, -1]
.. >>> 
.. Items in the sequence or iterable for which the function returns a true, the result are added to the result list. Like map, this function is roughly equivalent to a for loop, but it is built-in and fast:
.. 
.. >>> 
.. >>> result = []
.. >>> for x in range(-5, 5):
.. 	if x < 0:
.. 		result.append(x)
.. 
.. 		
.. >>> result
.. [-5, -4, -3, -2, -1]
.. >>> 
.. 
.. 
.. .. Decorators
.. .. ~~~~~~~~~~
.. .. 
.. .. * Memoize
.. .. 
.. .. * Static methods
