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
arm = Room('Armory', 'TBA', 'lab', None, 'final', None)
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
one = Room('Area One', 
'You have crossed the bridge from your settlement into the vast desert of the Unknown. Be careful, you can easily get lost here, and we don\'t want that to happen. After all, you have to beat the game to find what is lurking in that stupid secret room.\
 I mean, COME ON. How can you be that idiotic to forget what was in it? YOU MADE THAT ROOM. You know what? Whatever. Your own fault you lost your memory. Back to describing this room.\
 Finding what you are looking for can be quite tricky in this area. ', 'one_n', 'w_exit', 'one_s', 'two')
one_n = Room('Area One - North', 'There is nothing to be seen in either direction.', None, None, 'one', 'two_n')
one_s = Room('Area One - South', 'There is nothing to be seen in either direction.', 'one', None, None, 'two_s')
two = Room('Area Two', 'Are you even listening to what I just told you?', 'two_n', 'one', 'two_s', 'three')
two_n = Room('Area Two - North', 'I told you there is nothing in either direction. At least listen for once in your life.', None, 'one_n', 'two', 'three_n')
two_s = Room('Area Two - South', 'OK I AM TIRED OF YOUR-- wait. Is that something glistening in the ground? Well guess what, Deadbrain? You lucked out. Again. ', 'two', 'one_s', None, 'three_s')
three = Room('Area Three', 'I SAID THERE IS NOTHING HERE. STOP TRYING TO DIE OUT HERE. BE SMART.', 
'three_n', 'two', 'three_s', 'four')
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
final = Room('The Secret Room', 'Finally. I\'m surprised someone as pathetic as you could manage to even unlock this poop hole. Are you proud of yourself? DON\'T BE. From what I can tell you, there is literally nothing here except some other person. I do not even want to know how they managed to survive here for so long without any resources. Eww, I can\'t imagine his hygiene issues. Talk about nasty. I\'ll let you talk to him.', 
'arm', None, None, None)

final = False

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
character_one = Character('Regina')
character_two = Character('Emma')
character_three = Character('David')
character_four = Character('Cora')
character_five = Character('Henry')

class Dialogue:
    def __init__(self, convo, response_one, response_two):
        self.convo = convo
        self.response_one = response_one
        self.response_two = response_two
    
    def say(self, person):
        print person.name+':"'+self.convo+'"'

user_response = raw_input('> ')
node = None
intro = Dialogue('Hello, my name is Regina. I was the formal Queen of the Castle of the North before the incident. Before, I had so much power, but now I don\'t.')


'''node = intro
if user_reponse == response_one:
    node = intro_pt2
    print intro_pt2.convo'''




#--------------------------------------------------------------
#ITEMS
























