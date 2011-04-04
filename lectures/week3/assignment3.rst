Assignment 3
============

#. A football game between two teams
   can be represented as a tuple of two teams::
   
       >>> game = ('Chile', 'Spain')     
   
   The game result
   can be represented as a tuple with the goals   
   performed by each team::
       
       >>> result = (4, 1)    
   
   All the tournament games
   cab be represented as a dictionary
   associated to each result game::
   
       >>> tournament = {  
       ...     ('Honduras',    'Chile'):       (1, 4),   
       ...     ('Spain',       'Switzerland'): (1, 1),   
       ...     ('Chile',       'Switzerland'):(2, 0),   
       ...     ('Spain',       'Honduras'):    (1, 0),   
       ...     ('Chile',       'Spain'):       (5, 5),   
       ...     ('Switzerland', 'Honduras'):    (1, 2);   
       ... }   
   
   #. Write a function called ``teams(tournament)``  
      that return the set of teams which participated in the tournament::
         
          >>> teams(tournament)   
          {'Chile', 'Honduras', 'Switzerland', 'Spain'}    
   
   #. Write a function called ``draws(tournament)``    
      which count how many games of the tournament finish in a draw::   
         
       >>> draws(tournament)     

   #. When a team win a game, receives 3 points; 
      when draws, receive 1 point, and when lose, does not receive any point.
      Write a function called ``points(team, tournament)`` 
      which return how many points obtained a team in a tournament::

          >>> points('Chile', tournament) 
          7 
          >>> points('Honduras', tournament)    
          3 
   
   #. The difference of the goals of a team    
      is the sum of all the goals made 
      minus the sum of the goals against.  
      Write a function ``gf(team, tournament)``     
      which returns the goal differences    
      of a team in a tournament::    
         
          >>> gd('Chile', tournament)     
          5 
          >>> gd('Honduras', tournament)  
          -3
         
   #. Write a function called ``best_game(tournament)``  
      which return the game with more goals::
         
          >>> best_game(tournament)   
          ('Chile', 'Spain')   
   
   #. Write a function called ``position_table(tournament)``  
      which return a tuple lists
      ``(team, points, goal differences)``   
      order by the points from highest to lowest.
      The teams with the same points, must be ordered by goal differences
      from highest to lowest::
         
          >>> position_table(tournament)   
          [('Spain', 6, 2), ('Chile', 6, 1), ('Switzerland', 4, 0), ('Honduras', 1, -3)] 

