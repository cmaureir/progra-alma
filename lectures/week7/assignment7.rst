Assignment 7
============

Minesweeper
------------

  The minesweeper game is based on a rectangular grid which represents a minefield.
  Some elements of the grid has a mine, and other do not.
  The game is to discover all the boxes which does not has mines.
  
  In a program, we can represent a minefield as an array in which the boxes with
  mines are marked with the **-1** value,
  and the rest of them with the 0 value:: 
  
      >>> from numpy import *
      >>> minefield = array([[ 0,  0, -1,  0,  0,  0,  0,  0],
                             [-1,  0,  0,  0, -1,  0,  0,  0],
                             [ 0,  0,  0,  0, -1,  0,  0, -1],
                             [ 0,  0, -1,  0,  0,  0,  0,  0],
                             [ 0,  0,  0,  0,  0,  0, -1,  0],
                             [ 0, -1,  0,  0, -1,  0,  0,  0],
                             [ 0,  0, -1,  0,  0,  0,  0,  0],
                             [ 0,  0,  0,  0,  0,  0,  0,  0]])
  
  #. Write a function called ``create_minefield(pattern, n)``,
     ``pattern`` is a ``(rows, columns)`` tuple,
     which return a new random minefield with the given pattern
     with ``n`` mines.
  
     Perform the following steps:
  
     a. Build a vector of ``rows * columns`` size
        which has ``n`` times the -1 value, and the rest of them, only zeros.
     b. Import the ``shuffle`` function from the ``numpy.random`` module.
        This function disorder (or «shuffle») the array elements.
     c. Shuffle the vector elements that you created.
     d. Change the vector pattern.
  
     ::
  
        >>> create_minefield((4, 4), 5)
        array([[-1,  0,  0,  0],
               [ 0,  0,  0,  0],
               [ 0, -1, -1,  0],
               [ 0, -1, -1,  0]])
        >>> create_minefield((4, 4), 5)
        array([[ 0,  0, -1,  0],
               [ 0,  0,  0, -1],
               [-1,  0,  0,  0],
               [ 0,  0, -1, -1]])
        >>> create_minefield((4, 4), 5)
        array([[ 0,  0,  0, -1],
               [ 0,  0, -1, -1],
               [-1,  0,  0,  0],
               [ 0,  0, -1,  0]])
  
  #. When a box without a mine is discover, it appears a number,
     which indicates the amount of mines which are present in their
     eight neighboring boxes.
  
     Write a function called ``discover(minefield)``
     which modify the minefield putting en each zero box
     the amount of neighboring boxes with mines::
  
         >>> c = create_minefield((4, 4), 5)
         >>> c
         array([[ 0,  0, -1, -1],
                [ 0,  0, -1,  0],
                [ 0,  0,  0, -1],
                [ 0,  0,  0, -1]])
         >>> discover(c)
         >>> c
         array([[ 0,  2, -1, -1],
                [ 0,  2, -1,  4],
                [ 0,  1,  3, -1],
                [ 0,  0,  2, -1]])

  #. With this two function, you are now able to play minesweeper,
     so, write a function called ``play_minesweeper(level)`` which provide
     the possibility of play this game, turn by turn.
 
     To develop this function you must have in mind the following points:
   
     * The ``level`` parameter is an integer between 1 and 3.
     * Inside the function, you need to define the ``level`` as a tuple,
       with information ``(rows, columns, mines number)``.

      * *Level 1:* ``(5,5,6)``
      * *Level 2:* ``(7,7,12)``
      * *Level 3:* ``(10,10,30)``

     * The game behavior is a loop, which verify each turn if the game
       is over (**win** or **lose**), in both cases, you need to display a message to the user.
     * You must represent the undiscovered field with **#** symbols, for example
       a 5 x 5 field.:

       ::

           # # # # #
           # # # # #
           # # # # #
           # # # # #
           # # # # #

      * The user must enter a box ``(x,y)`` each turn, to undiscovered it.
      
       * If the box is a mine, the game is over.
       * If the box is not a mine, you change the **#** symbol by corresponding field number,
         for example, if we have this initial field:

         ::

             1  -1  1
             2   2  1
             -1  1  0

         We need to show it, like this:

         ::

             # # #
             # # #
             # # #

         The positions are:

         ::

             (0,2) (1,2) (2,2)
             (0,1) (1,1) (2,1)
             (0,0) (1,0) (2,0)

         So, the first choice of the user, can be, for example: ``(2,1)``

         ::

             # # #
             # # 1
             # # #

         The next choice, can be, for example: ``(0,1)``

         ::

             # # #
             2 # 1
             # # #


         An the third choice, can be, for example: ``(0,0)``

         ::

             #  # #
             2  # 1
             -1 # #

         So, the game is over!
