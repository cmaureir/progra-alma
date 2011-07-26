from time import sleep

antenna_models = {0:'ESO',1:'NAOJ',2:'NRAO'}
transporter_models = {0:'Otto',1:'Lore'}
antenna_state = {0:'READY',1:'FAILED',2:'OBSERVING'}
transporter_state = {0:'READY',1:'MOVING'}

transporters = []
antennas = []
pads = set([i for i in range(0,11)])

class Antenna():
    def __init__(self, id_number, model, state):
        self.id_number = id_number
        self.model = model
        self.state = state
        self.azimuth = 0 # 0 to 360 degrees
        self.elevation = 0 # 0 to 90 degrees
        self.pad = 0
        self.data = []

    def get_position(self):
        print 'not implemented'

    def set_position(self,x,y,z):
        print 'not implemented'

    def get_pad(self):
        print 'not implemented'

    def get_state(self):
        print 'not implemented'

class Transporter():
    def __init__(self, id_number, name, state):
        self.id_number = id_number
        self.name = name
        self.state = state

    def move(self, antenna, orig_pad, dest_pad):
        print 'not implemented'
        # change status
        # display message of moving (from initial pad, to final pad)
        sleep(0.5) # intentional delay to note the mechanism

# Add functions parameters if is needed

def create_transporters():
    pass
def create_antennas():
    pass
def move_antenna():
    pass
def set_antenna_position():
    pass
def set_antenna_state():
    pass
def start_observation():
    pass
def get_observation_data():
    pass
def get_problems():
    pass

if __name__ == '__main__':
   print 'Here will be the assignment process'
   # Add the assignment behaviour
