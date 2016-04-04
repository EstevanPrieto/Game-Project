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
start = Room('Camp Center',
'Everything around you is in ruins. Nobody to be seen. Wonderful sight, eh? Oh yeah. To the north is an exit to a bridge. To the east is the laboratory. To the south is another exit to a bridge. Finally, to the west is the storage room.', 
'n_exit', 'lab', 's_exit', 'storage')
s_exit = Room('South Exit', 'Ready for a chilly adventure? Cause I\'m not. To the south lies the Empty Highlands, a mountain range as empty as my soul. Or we could head back north to the start and just hang out there for the rest of our lives. Just saying, it sounds like a pretty good idea.', 
'start', None, 'mount', None)
lab = Room('Laboratory', 'Yikes. What a mess. Careful where you step, since you can step on some explosive chemical or some rad thing like that. Explain to me. What happened here? Wait, what? You forgot? HOW? Does this mean I have to guide your lost soul through this wasteland? Ughhhh. To the east, lies a third bridge, the armory is south of here, and the starting area is west.',
None, 'e_exit', 'arm', 'start')
arm = Room('Armory', 'Ooh guns. Too bad they are all rusted. Is that a vault south of here??? WHAT\'S INSIDE???? North of here is the laboratory.', 
'lab', None, 'final', None) 
e_exit = Room('East Exit', 'Feeling exotic and adventurous? Head east to the Wicked Forest of the East. Or you can be a boring human being and stay behind a counter in your slick laboratory in the west. And if you can remember anything, cook up a cure that does not exist.', 
None, 'forest', None, 'lab')
n_exit = Room('North Exit', 'Oh so you\'re feeling royal now, huh? You\'re one those stuck up people, right? Thinks they are better than everyone? That is the kind of mindset that plunges the world into this garbage. Cross the bridge if you want to head to the Rust Palace, or head back south to the start.', 
'gates', None, 'start', None)
farm = Room('Farm', 'Why is this place called a farm? ALL THE PLANTS ARE DEAD, LIKE THIS ENTIRE LAND. GONE. Absolutely NO resources. South of here is-- what?? A pantry? Maybe there some resources in there that we can actually use.',
None, None, 'storage', None) 
w_exit = Room('West Exit', 'Suicidal? If you are admired by the sights of nothing, head west into the Quiet Steppes. Or, go back east into the pantry, that holds absolutely nothing.',
None, 'storage', None, 'one')
storage = Room('Pantry', 'Will you look at that. That\'s right. Nothing. There is nothing here. Now that we explored all the possibile rooms here. We should probably go into one of the four main land zones and look for help. Yeah, this is one of the few times i will be helping you. I suggest going to the east first. North of here is the farm, the starting area is north, and the west bridge is to the west.',
'farm', 'start', None, 'w_exit')
mount = Room('Mountain Base', 'That is a really tall mountain. Do you really want to climb this? I think this is taller than what those Earthlings call Mount Everest. We could head back north to the camp, but I guess if you really want to, head south to start climbing.',
's_exit', None, 'slope', None)
slope = Room('Slopes', 'Remind me again why we are climbing a stupid mountain? Are you even wearing the proper attire? Back north is the base, where should head, in my opinion, Or we could finish climbing the mountain to see what you are desperately looking for. Or you can admire the wasteland by watching it from the cliff to the east.',
'mount', 'cliff', 'peak', None)
cliff = Room('Cliff', 'I TAKE BACK WHAT I SAID ABOUT THE CLIFF. PLEASE GO BACK. GETTING MAULED TO DEATH BY A YETI IS NOT ON MY LIST. DAMN, I THINK It SAW US! PLEASE. LET\'S GO BACK.',
None, None, None, 'slope')
peak = Room('Peak', 'Wait, what are we looking for again?', 'slope', 'e_peak', None, 'w_peak')
e_peak = Room('East Peak', 'Can we go back home, please? I don\'t know, maybe we still have the required resources to make hot chocolat???', None, None, None, 'peak')
w_peak = Room('West Peak', 'Oh, is that what we are looking for? It looks really odd to be a key.', None, 'peak', None, None)
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
three_n = Room('Area Three - North', 'I am not even going to.', None, 'two_n', 'three', None)
three_s = Room('Area Three - South', 'Nope.', 'three', 'two_s', None, None)
four = Room('Area Four', 'Just no.', None, 'three', None, None)
gates = Room('Gates', 'Welcome to the Rust Palace. Fun fact, did you know this place was originally just pure glass? How it went from glass to rust is beyond me. I am not scientist, but you are. Care to explain? Can\'t remember? That\'s fine.',
None, 'e_tower', 'n_exit', 'w_tower')
e_tower = Room('East Tower', 'Hey is that a key over there? North of here is the corridor and back west are the gates.', 'corridor', None, None, 'gates')
w_tower = Room('West Tower', 'Is that another key over there? If I recall, there should be only four of them. North is the hallway and east is the gates.', 'hallway', 'gates', None, None)
corridor = Room('Corridor', 'Why are there keys everywhere? Did we choose the right one back there? We should keep investigating.', 'dining', None, 'e_tower', None)
hallway = Room('Hallway', 'Keys. Keys. Keys. Keys. I count at least 5.', 'dorms', None, 'w_tower', None)
dining = Room('Dining Room', 'Too many keys. Should we back and investigate? Or should we head west into the main hall and look for other potenial keys?', None, None, 'corridor', 'main')
dorms = Room('Dorms', 'This place makes me sleepy. Weirdly enough, there are no keys here. I\'d say we should keep investigating.', None, 'main', 'hallway', None)
main = Room('Main Hall', 'Out of all these keys, the right one is going to be either the abnormally big key, the abnormally small key, the rusted one, or the polished one. Which one it is, I do not know. I am confused as you are, and that is saying something considering how clueless you can be.', 
None, 'dining', 'courtyard', 'dorms')
courtyard = Room('Courtyard', 'HOLY. WHY ARE THERE SO MANY KEYS??? I COUNT AT LEAST 60 OF THEM. You can back north into the hall or into the gates tby heading south.', 
'main', None, 'gates', None)
forest = Room('Forest', 'Hey, this place does not look half bad. Yo, that chick looks like she could help. Go ask her for some aid. Maybe she can tell us what happened here. Or you can go east, follow the south path, or head back to the camp.', 
None, 'boulder', 'path', 'e_exit')
boulder = Room('Boulder', 'That is a nice boulder.', 'hut', 'ruins', None, 'forest')
path = Room('Muddy Path', 'This path is leading us nowhere, dude. Please, listen to me for once. Let\'s go back.', 'forest', 'gear', None, None)
hut = Room('Abandoned Hut', 'It does not surprise me that there is nothing useful here. Actually, it is compeltely empty. Did they manage to evacuate before the Incident? Maybe we might run across them? Or maybe they died off.', 
None, None, 'boulder', None)
ruins = Room('Village Ruins', 'Dude, this looks an awful lot like our village back home. Can we go back? This place gives me the creeps. I do not want to find out if there are living skeletons waiting to seek us out.', 
None, None, None, 'boulder')
gear = Room('The Gear', 'That is a huge piece of gear, I wonder what it belon-- oh nevermind. Actually that makes a lot of sense. You should go ask that fellow robot over there. Then again, he seems pretty dangerous. I say we go back. You could either go south or west. Your choice.',
None, None, 'trees', 'path')
trees = Room('Fallen Trees', 'Um, I expected this forest to be a lot nicer. Now this is just scaring me. If we go back, I promise to be nicer to you. Or you can go east into the ring, which looks a lot more unsettling.', 'gear', 'ring', None, None)
ring = Room('Ring of Trees', 'Hey that is not a key. That is, actually I do not know what that is. It looks more like a card or something. Does the vault have some sort credit card slot?', 
None, None, None, 'trees')
final = Room('The Secret Room',
'Finally. I\'m surprised someone as pathetic as you could manage to even unlock this poop hole. Are you proud of yourself? DON\'T BE. From what I can tell you, there is literally nothing here except some other person. I do not even want to know how they managed to survive here for so long without any resources. Eww, I can\'t imagine his hygiene issues. Talk about nasty. I\'ll let you talk to him.', 
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
        
character_one = Character('Regina the Queen')
character_two = Character('David the Mechanical Beast')
character_three = Character('Emma the Dragon')
character_four = Character('Cora the Yeti')
character_five = Character('Kyle')

class Dialogue:
    def __init__(self, convo, response_one, response_two):
        self.convo = convo
        self.response_one = response_one
        self.response_two = response_two
    
    def say(self, person):
        print person.name+':"'+self.convo+'"'

#Regina's Dialogue 
node = None

intro = Dialogue('Hello, my name is Regina. I was the formal Queen of the Castle of the North before the incident. Before, I had so much power, but now, not so much.', 'What happened here?', 'Where am I?')
happen = Dialogue('I do not know. All I remember was that I was enjoying my time in my palace. Everything was normal. Then, I found myself here. How could such hell break loose on a once beautiful land? Speaking of which, where are you from?', 
'I am from the Center Camp across the bridge.', 
'I don\'t know. I just woke up in ruins and I followed this path.')
location = Dialogue('You don\'t remember anything? That sounds awful. The only memories I lost are what happened between during my black out. Anyway, you are in the ruins of the once beautiful Seaborath. Those waters you saw while crossing the bridge? That used to be the best purified water you could get in the realm. Now, it is simply a lake of acid.', 
'That is awful. However, I have this notebook with writings I can not decipher. Could you translate it for me?', 
'Is there something else you can tell me?') 
pity = Dialogue('Oh that is horrible! I saw the ruins on my journey over here. Is there something I can help you with?', 
'I have this notebook with writings I can not decipher. Could you translate it for me?', 
'That is kind of you, but I do not need any help at the moment. Thank you so much though!')
oh_ruins = Dialogue('Ruins? OH, I know now! You are from the Center Camp. I had to go through there in order to get to these forests. That must have been awful for you to go through such tragedy. Can I help you with anything?', 
'I have this notebook with writings I can not decipher. Could you translate it for me?', 
'That is kind of you, but I do not need any help at the moment. Thank you so much though!')
notebook = Dialogue('Of course! The writing is a bit smudged, but I can still read it. It says that the cure to this epidemic crisis is found the vault locked in the armory at the camp. To unlock it, you need four keys in which they are all found throughout Seaborath. They can each be found in the Wicked Forest (where we are right now), The Rust Palace of the North, The Quiet Steppes of the West, and the Empty Highlands. Now that I have given this information to you, you should hurry along. Your actions can save the future of Seaborath.', None, None)
prompt = Dialogue('From what I can think of, that is all I can tell you. Is there something you need?', 
'I have this notebook with writings I can not decipher. Could you translate it for me?', 
'That is kind of you, but I do not need any help at the moment. Thank you so much though!') 
decline = Dialogue('Ok then. You better be on your way then on your empty journey. Be careful.', None, None)

node = intro

print intro.say(character_one)
user_response = raw_input('> ')

if user_response == intro.response_one:
    node = happen
    print happen.convo

if user_response == intro.response_two:
    node = location
    print location.convo

if user_response == happen.response_two:
    node = oh_ruins
    print oh_ruins.convo

if user_response == happen.response_one:
    node = pity
    print pity.convo

if user_response == location.response_one:
    node = notebook
    print notebook.convo

if user_response == location.response_two:
    node = prompt
    print prompt.convo

if user_response == pity.response_one:
    node = notebook
    print notebook.convo
    
if user_response == pity.response_two:
    node = decline
    print decline.convo

if user_response == oh_ruins.response_one:
    node = notebook
    print notebook.convo

if user_response == oh_ruins.response_two:
    node = decline
    print decline.convo

if user_response == prompt.response_one:
    node = notebook
    print notebook.convo

if user_response == prompt.response_two:
    node = decline
    print decline.convo

#David's Dialogue

node = None

david_intro = Dialogue('Please don\'t hurt me! I\'m just a completely harmless, dismantled mechanical beast. Please, I beg you!', 'What happened?', 'Don\'t worry, I\'m harmless too.')
harmless = Dialogue('Thank you so much! My name is David by the way. I thought humans like you were dead by now. I saw what happened at the camp from a distance. Sadly I could not help due to my current state. It was truly a tragic sight. Can I help you with something?', 
'I was looking for an object. To be more specific, a key. With all the keys I need, I can fix everything that happened here. Do you think you can help?', 
'Nothing that concerns you. After all, I don\'t think you would be of much help given your current state.')
what_happened = Dialogue('I think that is pretty obvious. The blast of the Incident wiped out the beauty of this land along with the life with it. As you can see, the blast of it dismantled me and sent my parts flying everywhere. Now, I am a robot beyond repair.', 
'The Incident? What is that? Can you please explain because I lost my memory.', 
'I am so sorry, David. I\'m going through something similar like you. I have lost my memory and I am trying to regain them, but so far it has been really hard.')
incident = Dialogue('No no no. I can\'t. I just can\'t. It\'s too much. I don\'t want to talk about it.', 
'Oh ok then. I guess I better get going then. Good luck out here, David.', 
'Don\'t worry, David. I can fix this. I just need to gather the four keys so I can unlock the vault in my camp that is holding the cure. Do you know anything that can help?')
apology = Dialogue('Oh no, it\'s ok. Don\'t worry about it. I can relax here and admire the view, even if it is horrendous and disturbing. I hope you do regain your memories. Good luck.', 
'Thank you. I better get going then. Good luck out here, David.', 
'Don\'t worry, David. I can fix this. I just need to gather the four keys so I can unlock the vault in my camp that is holding the cure. Do you know anything that can help?')
bye = Dialogue('Be careful out there, David. I am sorry for not being of much help. Farewell.', None, None)
key_one_location = Dialogue('If you travel past me, at some point there is a place where a shiny object can be found. Occassionally I can see its shine from here, but I can\'t go investigate since I am dismantled. You should go check it out. Just be careful out there.', None, None)
something = Dialogue('You should keep travelling. Who knows? You might just come across something in this wasteland. Just watch out.', None, None)
rude_end = Dialogue('Oh ok. I understand, it isn\'t my business to intervene what is your pivacy. Forgive me for that. You should be on your way.', None, None)

node = david_intro

print david_intro.say(character_two)

if user_response == david_intro.response_one:
    node = what_happened
    print what_happened.convo

if user_response == david_intro.response_two:
    node = harmless
    print harmless.convo

if user_response == what_happened.response_one:
    node = incident
    print incident.convo

if user_response == what_happened.response_two:
    node = apology
    print apology.convo

if user_response == harmless.response_one:
    node = something
    print something.convo

if user_response == harmless.response_two:
    node = rude_end
    print rude_end.convo

if user_response == incident.response_one:
    node = bye
    print bye.convo

if user_response == incident.response_two:
    node = key_one_location
    print key_one_location.convo

if user_response == apology.response_one:
    node = bye
    print bye.convo

if user_response == apology.response_two:
    node = key_one_location
    print key_one_location.convo
    


#Emma's Dialogue

#Cora's Dialogue

#Kyle's Dialogue



















