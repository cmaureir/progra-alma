Assignment 5
============

Sticker Album
-------------

One of the most common hobbies of the children
is to buy an sticker album, from any interesting
topic, like dinosaurs, football, cars, cartoon, etc,
maybe you had one where you are a little boy!

First of all, please note that you can generate random numbers,
using the python ``random`` module, which provide several
functions to obtain random numbers in different ways.

For example, the ``randrange(n, m)`` function,
return a random number between ``n`` and ``m``::

    >>> from random import randrange
    >>> randrange(5, 15)
    14
    >>> randrange(5, 15)
    6
    >>> randrange(5, 15)
    14
    >>> randrange(5, 15)
    5
    >>> randrange(5, 15)
    12
    >>> randrange(5, 15)
    9

(Remember that the ranges include the first value but not the last one,
so the maximum previous value will be 14).

#. Lets think that a boy want to collect an sticker album.
   The stickers are enumerated from 1 to 640,
   and the boy can buy some sticker packets,
   which contain 5 stickers, but by error
   in some packets are only 4 stickers.

   Write a function called ``new_packet()``
   which return a list with the new stickers
   and a status, which is *correct* or *wrong*
   in cases which the stickers are 4 or 5::

    >>> new_packet()
    [27, 31, 207, 455, 529], correct
    >>> new_packet(), wrong
    [66, 577, 481, 171]
    >>> new_packet()
    [275, 493, 167, 25], wrong
    >>> new_packet()
    [113, 35, 592, 560, 244], correct


   **Hint:** Returning more than one value.

#. The boy has a sticker register of all their albums,
   but in this time, he is only looking for finish the
   **Python album**.

   The register is a simple list, called ``album_stickers``-

   Each day, the boy go to the store and buy some stickers
   and obviously, add them to the register.

   Write a function called ``add_stickers()``,
   which receive a parameter of the number of stickers,
   which can be *one* or *n* stickers,
   because in some days, the boy buy a lot of packets
   and he want to add them all::

    >>> album_stickers = []
    >>> add_stickers(1)
    >>> album_stickers
    [1]
    >>> add_stickers(2,500,156)
    >>> album_stickers
    [1,2,500,156]

   Also, the boy can add new entire packets,
   without know the content::

    >>> add_stickers(new_packets=2, 14)
    [1,2,500,156,4,75,23,8,324,36,244,234]

   Please note that the function does not return anything,
   only modify the ``album_stickers`` list.

   **Hint:** Default parameter and special parameters.

#. Write a function called ``missing(stickers)``
   which return the missing sticker set to complete the album::

    >>> album_stickers = []
    >>> add_stickers(new_packets=128)
    >>> missing(album_stickers)
    {514, 3, 5, 7, 10, 523, 12, 525, 14, 16, 529, ...}

   Please note that the boy buy 128 packets,
   that in total are the same number of the album stickers
   in approximation (because the bad packets), but because
   some stickers are more than once, or another stickers
   which does not are present in the packets is not
   enough to complete the album.

   **Hint:** List comprehensions.

#. Write a function called ``count_stickers(stickers)``
   which return a dictionary associating each sticker
   to the number of times which is in the stickers list::

    >>> album_stickers = [4, 6, 9, 12, 9, 9, 6, 12, 2]
    >>> count_stickers(album_stickers)
    {9: 3, 2: 1, 4: 1, 6: 2, 12: 2}

  **Hint:** *sorted()* function.

#. If the boy wants to exchange stickers with a friend,
   he need to know what stickers does not have and
   what of their stickers has the friend.

   The friend of the boy will exchange only the repeated
   stickers.

   Write a function called ``needed_stickers(wanted_stickers,friend_stickers)``
   which return the set of the stickers that can be exchanged,
   which are the intersection between the ``wanted_stickers`` (missing stickers)
   and the repeated stickers from his friend ``friend_stickers``::

    >>> album_stickers = [4, 6, 9, 12, 9, 9, 6, 12, 2]
    >>> friend_stickers = [4, 9, 7, 7, 4, 4, 8]
    >>> needed_stickers(album_stickers, friend_stickers)
    [7]
    >>> needed_stickers(friend_stickers, album_stickers)
    [12, 6]

   This means, the boy wants the sticker number 7, which
   his friend has repeated.
   Also he wants the sticker number 8, but she does not
   has it repeated, so, there is no exchange.
   His friend have repeated the stickers number 4,
   but the boy already have it, so, there is no exchange.

   **Hint:** *filter()* function.

#. Each packet have the possibility to contain an holographic sticker,
   which are multiples of ten.

   The boy want to sell to their friends the repeated stickers,
   a simple stickers cost 0.25 USD and the holographic stickers
   cost 0.50 USD.

   Write a function called ``sticker_cost()``
   which first obtain the sticker cost
   and later calculate the total cost of the repeated stickers::
   
     >>> album_stickers = [1,3,62,10,323,120,34]
     >>> sticker_cost(album_stickers)
     2.25 USD

   **Hint:** *map()* and *reduce()* function.
