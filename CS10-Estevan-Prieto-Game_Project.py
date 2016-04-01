import sys 
#Sets up aspects of the rooms

node = None

class Room:
    def __init__(self, name, description, n_path, e_path, s_path, w_path):
        '''Enter in the room name, room description, and rooms you can access from directions as follows: north, east, south, west
        '''
        self.name = name
        self.description = description
        self.north = n_path
        self.east = e_path
        self.south = s_path
        self.west = w_path

#Makes you able to move to each room       
    def move (self, direction):
        while True:
            global node
            node = globals()[getattr(self,direction)]
            break

#Rooms in the game
start = Room('Camp Center', 'TBA', 'n_exit', 'lab', 's_exit', 'storage')
s_exit = Room('South Exit', 'TBA', 'start', None, 'mount', None)
lab = Room('Laboratory', 'TBA', None, 'e_exit', 'arm', 'start')
arm = Room('Armory', 'TBA', 'lab', None, None, None)
e_exit = Room('East Exit', 'TBA', None, 'forest', None, 'lab')
n_exit = Room('North Exit', 'TBA', 'gates', None, 'start', None)
farm = Room('Farm', 'TBA', None, None, 'storage', None) 
w_exit = Room('West Exit', 'TBA', None, 'storage', None, 'one')
storage = Room('Pantry', 'TBA', 'farm', 'start', None, 'w_exit')
mount = Room('Mountain Base', 'TBA', 's_exit', None, 'slope', None)
slope = Room('Slopes', 'TBA', 'mount', 'cliff', 'peak', None)
cliff = Room('Cliff', 'TBA', None, None, None, 'slope')
peak = Room('Peak', 'TBA', 'slope', 'e_peak', None, 'w_peak')
e_peak = Room('East Peak', 'TBA', None, None, None, 'peak')
w_peak = Room('West Peak', 'TBA', None, 'peak', None, None)
one = Room('Area One', 'TBA', 'one_n', 'w_exit', 'one_s', 'two')
one_n = Room('Area One - North', 'TBA', None, None, 'one', 'two_n')
one_s = Room('Area One - South', 'TBA', 'one', None, None, 'two_s')
two = Room('Area Two', 'TBA', 'two_n', 'one', 'two_s', 'three')
two_n = Room('Area Two - North', 'TBA', None, 'one_n', 'two', 'three_n')
two_s = Room('Area Two - South', 'TBA', 'two', 'one_s', None, 'three_s')
three = Room('Area Three', 'TBA', 'three_n', 'two', 'three_s', 'four')
three_n = Room('Area Three - North', 'TBA', None, 'two_n', 'three', None)
three_s = Room('Area Three - South', 'TBA', 'three', 'two_s', None, None)
four = Room('Area Four', 'TBA', None, 'three', None, None)
gates = Room('Gates', 'TBA', None, 'e_tower', 'n_exit', 'w_tower')
e_tower = Room('East Tower', 'TBA', 'corridor', None, None, 'gates')
w_tower = Room('West Tower', 'TBA', 'hallway', 'gates', None, None)
corridor = Room('Corridor', 'TBA', 'dining', None, 'e_tower', None)
hallway = Room('Hallway', 'TBA', 'dorms', None, 'w_tower', None)
dining = Room('Dining Room', 'TBA', None, None, 'corridor', 'main')
dorms = Room('Dorms', 'TBA', None, 'main', 'hallway', None)
main = Room('Main Hall', 'TBA', None, 'dining', 'courtyard', 'dorms')
courtyard = Room('Courtyard', 'TBA', 'main', None, 'gates', None)
forest = Room('Forest', 'TBA', None, 'boulder', 'path', 'e_exit')
boulder = Room('Boulder', 'TBA', 'hut', 'ruins', None, 'forest')
path = Room('Muddy Path', 'TBA', 'forest', 'gear', None, None)
hut = Room('Abandoned Hut', 'TBA', None, None, 'boulder', None)
ruins = Room('Village Ruins', 'TBA', None, None, None, 'boulder')
gear = Room('The Gear', 'TBA', None, None, 'trees', 'path')
trees = Room('Fallen Trees', 'TBA', 'gear', 'ring', None, None)
ring = Room('Ring of Trees', 'TBA', None, None, None, 'trees')

#sets your location to the starting room in the game
node = start 

#prints where you are and checks if you can move that way; prompts you for where to go or if you want to quit
while True:    
    print node.name
    print node.description
    command = raw_input('> ')
    if command in ['north','south','east','west']:
        try:
            node.move(command)
        except:
            print 'You can\'t go that way.'
    if command in ['q', 'quit', 'exit']:
        sys.exit(0)
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#DIALOGUE
class Character:
    def __init__(self, name):
        self. name = name
character_one = Character('Laurel')
character_two = Character('Gaby')
character_three = Character('Eric')
character_four = Character('Carol')
character_five = Character('Gaby')

class Dialogue:
    def __init__(self, convo):
        self.convo = convo
    
    def say(self, person):
        print person.name+':"'+self.convo+'"'






















