Assignment 6
============

.. Software engineering book
.. Figures

Considering the ALMA project,
we can think in an small approach focused
only in the interaction between an antenna and
a transporter.

The main idea will be to 
move the antennas from one path to another.
This is performed by a transporter,
so you can easily deduce some restrictions.
For example, a transporter cannot has more
than one antenna, or each path cannot
has more than antenna neither, etc.

This assignment will only be related with the previus idea.

Lets consider the following two incomplete
classes:

::

    from time import sleep
    
    class Antenna():
        def __init__(self, id_number, model, state):
            self.id_number = id_number
            self.model = model
            self.state = state
            self.x = 0
            self.y = 0
            self.z = 0
            self.path = 0
            self.data = []
    
        def get_position(self):
            print 'not implemented'
    
        def set_position(self,x,y,z):
            print 'not implemented'
    
        def get_path(self):
            print 'not implemented'
    
        def get_state(self):
            print 'not implemented'
    
    class Transporter():
        def __init__(self, id_number, name, state):
            self.id_number = id_number
            self.name = name
            self.state = state
            self.fuel = 100
    
        def move(self, antenna, orig_path, dest_path):
            print 'not implemented'
            # change status
            # display message of moving (from initial path, to final path)
            sleep(0.5) # intentional delay to note the mechanism
    
        def get_fuel_status(self):
            print 'not implemented'
            
        def add_fuel(self):
            print 'not implemented'


You need to write the content
of the previous incomplete methods,
and also, you need to perform the following task
in separated functions (not methods!).

* **Create 2 transporters**, instructions:

  * Function name ``create_transporters(...)``.
  * Create two instance of the ``Transporter`` class.
  * Display a message warning the creation.
* **Create 10 antennas**, instructions:

  * Function name ``create_antennas(...)``.
  * Create two instance of the ``Antenna`` class.
  * Display a message warning the creation.
* **Move the antennas**, instructions:

  * Function name ``move_antenna(...)``
  * Call the ``move`` method of the transporter.
  * The main idea is to move all the antennas to the paths randomly,
    it means, which is not necessary to place the antenna 1 in the path 1.
  * Change the transporter status (*MOVING*).
  * Change the antenna status (random, between *OBSERVING* and *FAIL*).
  * Change the path status (Remove path from set).
  * Display a message warning the movement.
* **Set antennas positions**, instructions:

  * Function name ``set_antenna_position(...)``.
  * For each path, change the dice position to a random ``(x,y,z)`` position.
  * Display a message warning the movement.
* **Set antennas status**, instructions:

  * Function name ``set_antenna_state(...)``.
  * For each antenna in a path, change the state randomly-
  * Change antenna state.
  * Display a message warning the state change.
* **Start antenna observation**, instructions:

  * Function name ``start_observation(...)``
  * For each antenna in a path, with a *READY* state, start the observation
    and generate a list of ten data numbers randomly.
  * Change antenna state.
  * Display a message warning the observation process.

* **Getting the observation data**, instructions:

  * Function name ``get_observation_data(..)``.
  * Display all the data per antenna.
  * Show the most repeated value in the observation data.

* **Problems report**, instructions:

  * Function name ``get_problems(..)``.
  * Display all the antennas ``id_number`` with a **FAILED** status.

Also, this global list and dictionaries will be very useful,
to manipulate the states, models, etc:

::

    antenna_models = {0:'ESO',1:'NAOJ',2:'NRAO'}
    transporter_models = {0:'Otto',1:'Lore'}
    antenna_state = {0:'READY',1:'FAILED',2:'OBSERVING'}
    transporter_state = {0:'READY',1:'MOVING'}
    
    transporters = []
    antennas = []
    paths = set([i for i in range(0,10)])    

General considerations:

* All the transporters and antennas start in a zero point.
* When a transporter move an antenna to a certain path,
  the transporter stay in that path, until the next movement.
* Will be very useful to add in some code sections a ``sleep(0.5)``
  statement, to see all the process not so quickly.
* Remember the mechanism to generate a random number:

  ::
  
    from random import randint
    x =  randint(0,3)

  This will produce a random integer, between 0 and 2 (the 3 is not included)

To avoid confusion, you can download a template file from `here`_.

Is this the best way to work with Antennas and Transporters? Why? (Justify).

.. _`here`: ../../_static/programs/login-a6.py
