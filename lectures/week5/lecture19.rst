Lecture 19 - Iterators
----------------------

..  * Iterators
..      * iterators (itertools)
..         * chain, count, no necsito lista
..      * for
..         *       zip, map, sorted, enumerated, reversed

Iterators from `itertools`
~~~~~~~~~~~~~~~~~~~~~~~~~~
.. 

* Chain

.. 
.. itertools.chain(*iterables)¶
.. Make an iterator that returns elements from the first iterable until it is exhausted, then proceeds to the next iterable, until all of the iterables are exhausted. Used for treating consecutive sequences as a single sequence. Equivalent to:
.. 
.. def chain(*iterables):
..     # chain('ABC', 'DEF') --> A B C D E F
..     for it in iterables:
..         for element in it:
..             yield element
.. 
.. 

* Count

.. 
.. 
.. itertools.count(start=0, step=1)¶
.. Make an iterator that returns evenly spaced values starting with n. Often used as an argument to imap() to generate consecutive data points. Also, used with izip() to add sequence numbers. Equivalent to:
.. 
.. def count(start=0, step=1):
..     # count(10) --> 10 11 12 13 14 ...
..     # count(2.5, 0.5) -> 2.5 3.0 3.5 ...
..     n = start
..     while True:
..         yield n
..         n += step
.. When counting with floating point numbers, better accuracy can sometimes be achieved by substituting multiplicative code such as: (start + step * i for i in count()).
.. 

* Cycle

.. 
.. itertools.cycle(iterable)¶
.. Make an iterator returning elements from the iterable and saving a copy of each. When the iterable is exhausted, return elements from the saved copy. Repeats indefinitely. Equivalent to:
.. 
.. def cycle(iterable):
..     # cycle('ABCD') --> A B C D A B C D A B C D ...
..     saved = []
..     for element in iterable:
..         yield element
..         saved.append(element)
..     while saved:
..         for element in saved:
..               yield element
.. Note, this member of the toolkit may require significant auxiliary storage (depending on the length of the iterable).
.. 
.. 

* Repeat

.. 
.. 
.. itertools.repeat(object[, times])¶
.. Make an iterator that returns object over and over again. Runs indefinitely unless the times argument is specified. Used as argument to imap() for invariant function parameters. Also used with izip() to create constant fields in a tuple record. Equivalent to:
.. 
.. def repeat(object, times=None):
..     # repeat(10, 3) --> 10 10 10
..     if times is None:
..         while True:
..             yield object
..     else:
..         for i in xrange(times):
..             yield object
.. 
.. 
.. * Without list!
.. 

`for` iterators
~~~~~~~~~~~~~~~

* Zip

.. 
.. zip([iterable, ...])¶
.. This function returns a list of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. The returned list is truncated in length to the length of the shortest argument sequence. When there are multiple arguments which are all of the same length, zip() is similar to map() with an initial argument of None. With a single sequence argument, it returns a list of 1-tuples. With no arguments, it returns an empty list.
.. 
.. The left-to-right evaluation order of the iterables is guaranteed. This makes possible an idiom for clustering a data series into n-length groups using zip(*[iter(s)]*n).
.. 
.. zip() in conjunction with the * operator can be used to unzip a list:
.. 
.. >>> x = [1, 2, 3]
.. >>> y = [4, 5, 6]
.. >>> zipped = zip(x, y)
.. >>> zipped
.. [(1, 4), (2, 5), (3, 6)]
.. >>> x2, y2 = zip(*zipped)
.. >>> x == list(x2) and y == list(y2)
.. True
.. 
.. 

* Map

.. 
.. map(function, iterable, ...)
.. Apply function to every item of iterable and return a list of the results. If additional iterable arguments are passed, function must take that many arguments and is applied to the items from all iterables in parallel. If one iterable is shorter than another it is assumed to be extended with None items. If function is None, the identity function is assumed; if there are multiple arguments, map() returns a list consisting of tuples containing the corresponding items from all iterables (a kind of transpose operation). The iterable arguments may be a sequence or any iterable object; the result is always a list.
.. 
.. 

* Sorted

.. 
.. sorted(iterable[, cmp[, key[, reverse]]])
.. Return a new sorted list from the items in iterable.
.. 
.. The optional arguments cmp, key, and reverse have the same meaning as those for the list.sort() method (described in section Mutable Sequence Types).
.. 
.. cmp specifies a custom comparison function of two arguments (iterable elements) which should return a negative, zero or positive number depending on whether the first argument is considered smaller than, equal to, or larger than the second argument: cmp=lambda x,y: cmp(x.lower(), y.lower()). The default value is None.
.. 
.. key specifies a function of one argument that is used to extract a comparison key from each list element: key=str.lower. The default value is None (compare the elements directly).
.. 
.. reverse is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed.
.. 
.. In general, the key and reverse conversion processes are much faster than specifying an equivalent cmp function. This is because cmp is called multiple times for each list element while key and reverse touch each element only once. Use functools.cmp_to_key() to convert an old-style cmp function to a key function.
.. 
.. For sorting examples and a brief sorting tutorial, see Sorting HowTo.
.. 

* enumerated

.. 
.. enumerate(sequence[, start=0])¶
.. Return an enumerate object. sequence must be a sequence, an iterator, or some other object which supports iteration. The next() method of the iterator returned by enumerate() returns a tuple containing a count (from start which defaults to 0) and the corresponding value obtained from iterating over iterable. enumerate() is useful for obtaining an indexed series: (0, seq[0]), (1, seq[1]), (2, seq[2]), .... For example:
.. 
.. >>> for i, season in enumerate(['Spring', 'Summer', 'Fall', 'Winter']):
.. ...     print i, season
.. 0 Spring
.. 1 Summer
.. 2 Fall
.. 3 Winter
.. 
.. 

* reversed

.. 
.. reversed(seq)¶
.. Return a reverse iterator. seq must be an object which has a __reversed__() method or supports the sequence protocol (the __len__() method and the __getitem__() method with integer arguments starting at 0).
.. 
.. 
.. 
.. 
.. 

frozenset([iterable])

.. Return a frozenset object, optionally with elements taken from iterable. The frozenset type is described in Set Types — set, frozenset.
.. 
.. For other containers see the built in dict, list, and tuple classes, and the collections module.
.. 
.. class frozenset([iterable])
.. Return a new set or frozenset object whose elements are taken from iterable. The elements of a set must be hashable. To represent sets of sets, the inner sets must be frozenset objects. If iterable is not specified, a new empty set is returned.
.. 
.. Instances of set and frozenset provide the following operations:
.. 
.. len(s)
.. Return the cardinality of set s.
.. x in s
.. Test x for membership in s.
.. x not in s
.. Test x for non-membership in s.
.. isdisjoint(other)
.. Return True if the set has no elements in common with other. Sets are disjoint if and only if their intersection is the empty set.
.. 
.. New in version 2.6.
.. 
.. issubset(other)
.. set <= other
.. Test whether every element in the set is in other.
.. set < other
.. Test whether the set is a true subset of other, that is, set <= other and set != other.
.. issuperset(other)
.. set >= other
.. Test whether every element in other is in the set.
.. set > other
.. Test whether the set is a true superset of other, that is, set >= other and set != other.
.. union(other, ...)
.. set | other | ...
.. Return a new set with elements from the set and all others.
.. 
.. Changed in version 2.6: Accepts multiple input iterables.
.. 
.. intersection(other, ...)
.. set & other & ...
.. Return a new set with elements common to the set and all others.
.. 
.. Changed in version 2.6: Accepts multiple input iterables.
.. 
.. difference(other, ...)
.. set - other - ...
.. Return a new set with elements in the set that are not in the others.
.. 
.. Changed in version 2.6: Accepts multiple input iterables.
.. 
.. symmetric_difference(other)
.. set ^ other
.. Return a new set with elements in either the set or other but not both.
.. copy()
.. Return a new set with a shallow copy of s.
.. Note, the non-operator versions of union(), intersection(), difference(), and symmetric_difference(), issubset(), and issuperset() methods will accept any iterable as an argument. In contrast, their operator based counterparts require their arguments to be sets. This precludes error-prone constructions like set('abc') & 'cbs' in favor of the more readable set('abc').intersection('cbs').
.. 
.. Both set and frozenset support set to set comparisons. Two sets are equal if and only if every element of each set is contained in the other (each is a subset of the other). A set is less than another set if and only if the first set is a proper subset of the second set (is a subset, but is not equal). A set is greater than another set if and only if the first set is a proper superset of the second set (is a superset, but is not equal).
.. 
.. Instances of set are compared to instances of frozenset based on their members. For example, set('abc') == frozenset('abc') returns True and so does set('abc') in set([frozenset('abc')]).
.. 
.. The subset and equality comparisons do not generalize to a complete ordering function. For example, any two disjoint sets are not equal and are not subsets of each other, so all of the following return False: a<b, a==b, or a>b. Accordingly, sets do not implement the __cmp__() method.
.. 
.. Since sets only define partial ordering (subset relationships), the output of the list.sort() method is undefined for lists of sets.
.. 
.. Set elements, like dictionary keys, must be hashable.
.. 
.. Binary operations that mix set instances with frozenset return the type of the first operand. For example: frozenset('ab') | set('bc') returns an instance of frozenset.
.. 
.. 
.. 
.. A frozenset is basically the same as a set, except that it is immutable - once it is created, its members cannot be changed. Since they are immutable, they are also hashable, which means that frozensets can be used as members in other sets and as dictionary keys. frozensets have the same functions as normal sets, except none of the functions that change the contents (update, remove, pop, etc.) are available.
.. >>> fs = frozenset([2, 3, 4])
.. >>> s1 = set([fs, 4, 5, 6])
.. >>> s1
.. set([4, frozenset([2, 3, 4]), 6, 5])
.. >>> fs.intersection(s1)
.. frozenset([4])
.. >>> fs.add(6)
.. Traceback (most recent call last):
..   File "<stdin>", line 1, in <module>
.. AttributeError: 'frozenset' object has no attribute 'add'
.. 
.. 
