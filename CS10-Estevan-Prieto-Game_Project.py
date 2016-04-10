#THINGS TO CLEAN UP
    #Choppy Dialogue System
    #Develop dialogue with characters - add more background to it
    #More rooms?
    #Change keys to something more appealing?
    #Fix you win function
    #Set the final room to tell you you cant go there while you dont have the keys.
    #probable case - change code to dictionaries so the code can flow more easily

global inventory
import sys 
#Sets up aspects of the rooms

class Inventory:
    def __init__(self):
        self.inventory = []
my_inventory = Inventory()        

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def pick_up(self, storage):
        storage.inventory.append(self.name)
        print "You have picked up the %s." % self.name

cookie = Item('Galleta', 'The source of your problems.')
first_key = Item('First Key', 'First key to unlock the room.')
second_key = Item('Second Key', 'Second key to unlock the room.')
third_key = Item('Third Key', 'Third key to unlock the room.')
fourth_key = Item('Fourth Key', 'Fourth key to unlock the room.')

node = None

class Room:
    def __init__(self, name, description, n_path, e_path, s_path, w_path, key, key_two, key_three, key_four):
        '''Enter in the room name, room description, and rooms you can access from directions as follows: north, east, south, west
        '''
        self.name = name
        self.description = description
        self.north = n_path
        self.east = e_path
        self.south = s_path
        self.west = w_path
        self.key = key
        self.key_two = key_two
        self.key_three = key_three
        self.key_four = key_four

#Makes you able to move to each room       
    def move (self, direction):
        while True:
            global node
            node = globals()[getattr(self,direction)]
            break

#Rooms in the game
#Rooms in the game
start = Room('Camp Center','Everything around you is in ruins. Nobody to be seen. Wonderful sight, eh? There is a notebook in your pocket that is in a language you can\'t read, so you should go look for someone to decipher it for you. Oh yeah. To the north is an exit to a bridge. To the east is the laboratory. To the south is another exit to a bridge. Finally, to the west is the storage room. You should explore this settlement before going beyond. Look for the storages to see if we can find something we can use.',
'n_exit', 'lab', 's_exit', 'storage', None, None, None, None,)
s_exit = Room('South Exit', 'Ready for a chilly adventure? Cause I\'m not. To the south lies the Empty Highlands, a mountain range as empty as my soul. Or we could head back north to the start and just hang out there for the rest of our lives. Just saying, it sounds like a pretty good idea.',
'start', None, 'mount', None, None, None, None, None)
lab = Room('Laboratory', 'Yikes. What a mess. Careful where you step, since you can step on some explosive chemical or some rad thing like that. Explain to me. What happened here? Wait, what? You forgot? HOW? Does this mean I have to guide your lost soul through this wasteland? Ughhhh. To the east, lies a third bridge, the armory is south of here, and the starting area is west.',
None, 'e_exit', 'arm', 'start', None, None, None, None)
arm = Room('Armory', 'Ooh guns. Too bad they are all rusted. North of here is the laboratory.', 'lab', None, 'final', None, None, None, None, None) 
e_exit = Room('East Exit', 'Feeling exotic and adventurous? Head east to the Wicked Forest of the East. Or you can be a boring human being and stay behind a counter in your slick laboratory in the west. And if you can remember anything, cook up a cure that does not exist.', None, 'forest', None, 'lab', None, None, None, None)
n_exit = Room('North Exit', 'Oh so you\'re feeling royal now, huh? You\'re one those stuck up people, right? Thinks they are better than everyone? That is the kind of mindset that plunges the world into this garbage. Head north to cross the bridge if you want to head to the Rust Palace, or head back south to the start.', 
'gates', None, 'start', None, None, None, None, None)
farm = Room('Farm', 'Why is this place called a farm? ALL THE PLANTS ARE DEAD, LIKE THIS ENTIRE LAND. GONE. Absolutely NO resources. Well now that we have explored most of the parts of this camp, we should explore the main land of this wasteland. I recommend going to the east.',
None, None, 'storage', None, None, None, None, None) 
w_exit = Room('West Exit', 'Suicidal? If you are admired by the sights of nothing, head west into the Quiet Steppes. Or, go back east into the pantry, that holds absolutely nothing.',
None, 'storage', None, 'one', None, None, None, None)
storage = Room('Pantry', 'Will you look at that. Nothing. Absolutely nothing. Norht of here is the farm, the start is to the east, and the west exit is to the west.',
'farm', 'start', None, 'w_exit', None, None, None, None)
mount = Room('Mountain Base', 'That is a really tall mountain. Do you really want to climb this? I think this is taller than what those Earthlings call Mount Everest. We could head back north to the camp, but I guess if you really want to, head south to start climbing.',
's_exit', None, 'slope', None, None, None, None, None)
slope = Room('Slopes', 'Remind me again why we are climbing a stupid mountain? Are you even wearing the proper attire? Back north is the base, where should head, in my opinion, Or we could head south to finish climbing the mountain to see what you are desperately looking for. Or you can admire the wasteland by watching it from the cliff to the east.',
'mount', 'cliff', 'peak', None, None, None, None, None)
cliff = Room('Cliff', 'I TAKE BACK WHAT I SAID ABOUT THE CLIFF. PLEASE GO BACK. GETTING MAULED TO DEATH BY A YETI IS NOT ON MY LIST. DAMN, I THINK It SAW US! PLEASE. LET\'S GO BACK WEST. Wait, does it talk?? ',
None, None, None, 'slope', None, None, None, None)
peak = Room('Peak', 'Wait, what are we looking for again? We can also explore the east and west sides of the peak.', 'slope', 'e_peak', None, 'w_peak', None, None, None, None)
e_peak = Room('East Peak', 'Can we go back home, please? I don\'t know, maybe we still have the required resources to make hot chocolate??? West of here is the peak.', None, None, None, 'peak', None, None, None, None)
w_peak = Room('West Peak', 'Oh, is that what we are looking for? It looks really odd to be a key. East of here is the peak. When we get back, we should head west to look for the third key.', None, 'peak', None, None, None, second_key, None, None)
one = Room('Area One', 
'You have crossed the bridge from your settlement into the vast desert of the Unknown. Be careful, you can easily get lost here, and we don\'t want that to happen. After all, you have to beat the game to find what is lurking in that stupid secret room.\
 I mean, COME ON. How can you be that idiotic to forget what was in it? YOU MADE THAT ROOM. You know what? Whatever. Your own fault you lost your memory. Back to describing this room.\
 Finding what you are looking for can be quite tricky in this area. ', 'one_n', 'w_exit', 'one_s', 'two', None, None, None, None)
one_n = Room('Area One - North', 'There is nothing to be seen in either direction. A huge sand storm is preventing us from traveling north. The dead acid sea prevents us form going to the east.', None, None, 'one', 'two_n', None, None, None, None)
one_s = Room('Area One - South', 'There is nothing to be seen in either direction. South of here is a huge wall preventing us to travel there.', 'one', None, None, 'two_s', None, None, None, None)
two = Room('Area Two', 'Are you even listening to what I just told you?', 'two_n', 'one', 'two_s', 'three', None, None, None, None)
two_n = Room('Area Two - North', 'I told you there is nothing in either direction. At least listen for once in your life.', None, 'one_n', 'two', 'three_n', None, None, None, None)
two_s = Room('Area Two - South', 'OK I AM TIRED OF YOUR-- wait. Is that something glistening in the ground? Well guess what, Deadbrain? You lucked out. Again. The final key should be nort of home.', 'two', 'one_s', None, 'three_s', None, None, third_key, None)
three = Room('Area Three', 'I SAID THERE IS NOTHING HERE. STOP TRYING TO DIE OUT HERE. BE SMART.', 
'three_n', 'two', 'three_s', 'four', None, None, None, None)
three_n = Room('Area Three - North', 'I am not even going to.', None, 'two_n', 'three', None, None, None, None, None)
three_s = Room('Area Three - South', 'Nope.', 'three', 'two_s', None, None, None, None, None, None)
four = Room('Area Four', 'Just no.', None, 'three', None, None, None, None, None, None)
gates = Room('Gates', 'Welcome to the Rust Palace. Fun fact, did you know this place was originally just pure glass? How it went from glass to rust is beyond me. I am not scientist, but you are. Care to explain? Can\'t remember? That\'s fine.',
None, 'e_tower', 'n_exit', 'w_tower', None, None, None, None)
e_tower = Room('East Tower', 'Hey is that a key over there? North of here is the corridor and back west are the gates.', 
'corridor', None, None, 'gates', None, None, None, None)
w_tower = Room('West Tower', 'Is that another key over there? If I recall, there should be only four of them. North is the hallway and east is the gates.', 
'hallway', 'gates', None, None, None, None, None, None,)
corridor = Room('Corridor', 'Why are there keys everywhere? Did we choose the right one back there? We should keep investigating.', 
'dining', None, 'e_tower', None, None, None, None, fourth_key)
hallway = Room('Hallway', 'Keys. Keys. Keys. Keys. I count at least 5.', 
'dorms', None, 'w_tower', None, None, None, None, None)
dining = Room('Dining Room', 'Too many keys. Should we back and investigate? Or should we head west into the main hall and look for other potenial keys?', 
None, None, 'corridor', 'main', None, None, None, None)
dorms = Room('Dorms', 'This place makes me sleepy. Weirdly enough, there are no keys here. I\'d say we should keep investigating.', 
None, 'main', 'hallway', None, None, None, None, None)
main = Room('Main Hall', 'So many keys. Which is right? I am confused as you are, and that is saying something considering how clueless you can be.', 
None, 'dining', 'courtyard', 'dorms', None, None, None, None)
courtyard = Room('Courtyard', 'HOLY. WHY ARE THERE SO MANY KEYS??? I COUNT AT LEAST 60 OF THEM. AND WHY IS THERE A DRAGON? LET\'S LEAVE. You can back north into the hall or into the gates tby heading south.', 
'main', None, 'gates', None, None, None, None, None)
forest = Room('Forest', 'Hey, this place does not look half bad. Yo, that chick looks like she could help. Go ask her for some aid. Maybe she can tell us what happened here. Or you can go east, follow the south path, or head back to the camp.', 
None, 'boulder', 'path', 'e_exit', None, None, None, None)
boulder = Room('Boulder', 'That is a nice boulder. North of here is a hut. East are ruins. West is the entrance.', 'hut', 'ruins', None, 'forest', None, None, None, None)
path = Room('Muddy Path', 'This path is leading us nowhere, dude. Please, listen to me for once. Let\'s go back. Head north to go back or head east to a weird steel thing I see.', 
'forest', 'gear', None, None, None, None, None, None)
hut = Room('Abandoned Hut', 'It does not surprise me that there is nothing useful here. Actually, it is compeltely empty. Did they manage to evacuate before the Incident? Maybe we might run across them? Or maybe they died off. We can\'t go anywhere form here. Let\'s go back south.', 
None, None, 'boulder', None, None, None, None, None)
ruins = Room('Village Ruins', 'Dude, this looks an awful lot like our village back home. Can we go back? This place gives me the creeps. I do not want to find out if there are living skeletons waiting to seek us out. Let\'s head back west.', 
None, None, None, 'boulder', None, None, None, None)
gear = Room('The Gear', 'That is a huge piece of gear, I wonder what it belon-- oh nevermind. Actually that makes a lot of sense. You should go ask that fellow robot over there. Then again, he seems pretty dangerous. I say we go back. You could either go south or west. Your choice.',
None, None, 'trees', 'path', None, None, None, None)
trees = Room('Fallen Trees', 'Um, I expected this forest to be a lot nicer. Now this is just scaring me. If we go back, I promise to be nicer to you. Or you can go east into the ring, which looks a lot more unsettling.', 
'gear', 'ring', None, None, None, None, None, None)
ring = Room('Ring of Trees', 'Hey is that the key?. That is a weird looking key. Why do we need the keys? We don\'t even know where the vault is? Head back west into the fallen trees. Type pick up key to pick it up. (This applies to the rest of them).', 
None, None, None, 'trees', first_key, None, None, None,)
final = Room('The Secret Room',
'Finally. I\'m surprised someone as pathetic as you could manage to even unlock this poop hole. Are you proud of yourself? DON\'T BE. From what I can tell you, there is literally nothing here except for what? A COOKIE? THAT TALKS? GOODBYE. I AM DONE HERE.', 
'arm', None, None, None, None, None, None, None)

#sets your location to the starting room in the game
node = start 

#prints where you are and checks if you can move that way; prompts you for where to go or if you want to quit

        
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#DIALOGUE

class Character:
    def __init__(self, name):
        self. name = name
#Characters you will encounter in the game        
character_one = Character('Regina the Queen')
character_two = Character('David the Mechanical Beast')
character_three = Character('Emma the Dragon')
character_four = Character('Cookie')

#Sets up the dialogue and your choices
class Dialogue:
    def __init__(self, convo, response_one, response_two):
        self.convo = convo
        self.response_one = response_one
        self.response_two = response_two
    
    def say(self, person):
        print person.name+':"'+self.convo+'"'

#Regina's Dialogue 
intro = Dialogue('Hello, my name is Regina. I was the formal Queen of the Castle of the North before the incident. Before, I had so much power, but now, not so much.', 
'What happened here?', 'Where am I?')
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

#David's Dialogue
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
bye = Dialogue('Be careful out there. I am sorry for not being of much help. Farewell.', None, None)
key_one_location = Dialogue('If you travel past me, at some point there is a place where a shiny object can be found. Occassionally I can see its shine from here, but I can\'t go investigate since I am dismantled. You should go check it out. Just be careful out there.', 
None, None)
something = Dialogue('You should keep travelling. Who knows? You might just come across something in this wasteland. Just watch out.', 
None, None)
rude_end = Dialogue('Oh ok. I understand, it isn\'t my business to intervene what is your pivacy. Forgive me for that. You should be on your way.', 
None, None)

#Emma's Dialogue
fuego = Dialogue("Do NOT tempt me, human. I WILL burn you.", 
"Chill out. I\'m just looking for something.", 'Fine then. I\'ll leave. Gosh.')
still = Dialogue("I do NOT care. I am not going to ask you again. LEAVE. NOW.",
"Plese? Can you help me? I beg you. I am looking for something that can save this world from this hell.", "Fine then. I will leave, you useless dragon.")
short_end = Dialogue("Thank the lord. You BETTER leave. Leave now before I change my mind and roast you into a crisp.", None, None)
fine = Dialogue("FINE THEN. What are you looking for? It better not be a stupid jewel you\'re looking for.", "I\'m looking for a key that unlocks a vault back home, but there are so many I can\'t tell which is which and I still don\'t know where the vault is.", "Actually, you know what? Never mind. I\'ll go look for it myself.")
mid_end = Dialogue("YOU BETTER RUN. I DON\'T WANT TO SEE YOUR FACE AGAIN.", None, None)
true_key = Dialogue("UGH FINE. Now let me see those keys you have. Ahh. Ok. You are looking for the key that is in the corridors. And the keys are made by the same material as bullets were made of back then. You should check south of the armory back at your camp. Now GO. I don\'t want to see your face again.", None, None)
waste = Dialogue("STOP WASTING MY TIME. YOU ASK FOR HELP AND YOU JUST BACK OUT RIGHT AFTERWARDS? LEAVE.", None, None)

#Cookie Dialogue
well = Dialogue("Well look at that.", "You can talk? What the hell?", "Where is the cure?")
magical = Dialogue("Duh. This is Seaborath. ANYTHING can happen. Including a talking cookie.", "So, the cure?", "Is there nothing here?")
confused = Dialogue("What cure?", "Don\'t play with me, you stupid cookie.", "SHOW ME THE CURE!")
furious = Dialogue("WHAT CURE?!?!?", "THE CURE TO FIX THIS DAMN PLACE!", "TELL ME WHERE THE FREAKING CURE IS!")
honesty = Dialogue("I seriously do not know what cure you are talking about.", "Really? You don\'t know where the cure is?", "Wow. This whole stupid journey was useless. I am a failure to Seaborath...")
nothing_here = Dialogue("There is NOTHING here. I'm sorry. Your whole journey was a waste of time. This whole mess is permanent. Welcome to the NEW Seaborath.", None, None)
heated = Dialogue("OH NOW I\'M HEATED.", None, None)
indeed = Dialogue("Indeed. You provided false hope to the innocent souls of this land. Now you get to LIVE with it. This is the new world. This is the NEW Seaborath.", None, None)
yeah = Dialogue("Yeah. There is nothing here. I am sorry. However, at least you have found a nice snack!", None, None)
the_cure = Dialogue("There is no cure. I am the only thing here. However, I can be considered a cure to your hunger. Just a thought.", None, None)
absolutely = Dialogue("Absolutely nothing. Except me of course Cx.", None, None)

while True:   
    print node.name
    print node.description
    user_response = raw_input('> ')
    if user_response in ['north','south','east','west']:
        node.move(user_response)
    else:
        print "???"
    if user_response in ['q', 'quit', 'exit']:
        sys.exit(0)

    if node == two_s and user_response == "pick up key":
        third_key.pick_up(my_inventory)
        
   
    
    if node == ring and user_response == "pick up key":
        first_key.pick_up(my_inventory)
        
   
    
    if node == corridor and user_response == "pick up key":
        fourth_key.pick_up(my_inventory)
        final = True

    
    if node == w_peak and user_response == "pick up key":
        second_key.pick_up(my_inventory)
        
 

    
#Regina's Dialogue location and Transition  
    if node == forest:
        print intro.say(character_one)
        print '--------------------------------------------------'
        print "Type one of the following choices below EXACTLY as it is. This game is case sensitive."
        print intro.response_one
        print intro.response_two
        print '--------------------------------------------------'
        
    if user_response == intro.response_one:
        print happen.say(character_one)
        print '--------------------------------------------------'
        print "Type one of the following choices below EXACTLY as it is. This game is case sensitive."
        print happen.response_one
        print happen.response_two
        print '--------------------------------------------------'

    if user_response == intro.response_two:
        print location.say(character_one)
        print '--------------------------------------------------'
        print "Type one of the following choices below EXACTLY as it is. This game is case sensitive."
        print location.response_one
        print location.response_two
        print '--------------------------------------------------'

    if user_response == happen.response_two:
        print oh_ruins.say(character_one)
        print '--------------------------------------------------'
        print "Type one of the following choices below EXACTLY as it is. This game is case sensitive."
        print oh_ruins.response_one
        print oh_ruins.response_two
        print '--------------------------------------------------'

    if user_response == happen.response_one:
        print pity.say(character_one)
        print '--------------------------------------------------'
        print "Type one of the following choices below EXACTLY as it is. This game is case sensitive."
        print pity.response_one
        print pity.response_two
        print '--------------------------------------------------'
        
    if user_response == location.response_one:
        print notebook.say(character_one)

    if user_response == location.response_two:
        print prompt.say(character_one)
        print '--------------------------------------------------'
        print "Type one of the following choices below EXACTLY as it is. This game is case sensitive."
        print prompt.response_one
        print prompt.response_two
        print '--------------------------------------------------'
        
    if user_response == pity.response_one:
        print notebook.say(character_one)

    if user_response == pity.response_two:
        print decline.say(character_one)
        
    if user_response == oh_ruins.response_one:
        print notebook.say(character_one)

    if user_response == oh_ruins.response_two:
        print decline.say(character_one)
        print '-------------------------------------------'
        print "Type one of the following choices below EXACTLY as it is. This game is case sensitive."
        print decline.response_one
        print decline.response_two
        print '--------------------------------------------------'

    if user_response == prompt.response_one:
        print notebook.say(character_one)

    if user_response == prompt.response_two:
        print decline.say(character_one)

#David's Dialogue Location and Transitions        
    if node == gear:
        print david_intro.say(character_two)
        print '--------------------------------------------------'
        print "Type one of the following choices below EXACTLY as it is. This game is case sensitive."
        print david_intro.response_one
        print david_intro.response_two
        print '--------------------------------------------------'

    if user_response == david_intro.response_one:
        print what_happened.say(character_two)
        print '--------------------------------------------------'
        print "Type one of the following choices below EXACTLY as it is. This game is case sensitive."
        print what_happened.response_one
        print what_happened.response_two
        print '--------------------------------------------------'

    if user_response == david_intro.response_two:
        print harmless.say(character_two)
        print '--------------------------------------------------'
        print "Type one of the following choices below EXACTLY as it is. This game is case sensitive."
        print harmless.response_one
        print harmless.response_two
        print '--------------------------------------------------'

    if user_response == what_happened.response_one:
        print incident.say(character_two)
        print '--------------------------------------------------'
        print "Type one of the following choices below EXACTLY as it is. This game is case sensitive."
        print incident.response_one
        print incident.response_two
        print '--------------------------------------------------'

    if user_response == what_happened.response_two:
        print apology.say(character_two)
        print '--------------------------------------------------'
        print "Type one of the following choices below EXACTLY as it is. This game is case sensitive."
        print apology.response_one
        print apology.response_two
        print '--------------------------------------------------'

    if user_response == harmless.response_one:
        print something.say(character_two)
        print '--------------------------------------------------'
        print "Type one of the following choices below EXACTLY as it is. This game is case sensitive."
        print something.response_one
        print something.response_two
        print '--------------------------------------------------'

    if user_response == harmless.response_two:
        print rude_end.say(character_two)

    if user_response == incident.response_one:
        print bye.say(character_two)

    if user_response == incident.response_two:
        print key_one_location.say(character_two)

    if user_response == apology.response_one:
        print bye.say(character_two)

    if user_response == apology.response_two:
        print key_one_location.say(character_two)

#dialogue location and transitions for Emma    
    if node == courtyard:
        print fuego.say(character_three)
        print '--------------------------------------------------'
        print "Type one of the following choices below EXACTLY as it is. This game is case sensitive."
        print fuego.response_one
        print fuego.response_two
        print '--------------------------------------------------'
    
    if user_response == fuego.response_one:
        print still.say(character_three)
        print '--------------------------------------------------'
        print "Type one of the following choices below EXACTLY as it is. This game is case sensitive."
        print still.response_one
        print still.response_two
        print '--------------------------------------------------'
    
    if user_response == fuego.response_two:
        print short_end.say(character_three)
        
    if user_response == still.response_one:
        print fine.say(character_three)
        print '--------------------------------------------------'
        print "Type one of the following choices below EXACTLY as it is. This game is case sensitive."
        print fine.response_one
        print fine.response_two
        print '--------------------------------------------------'
    
    if user_response == still.response_two:
        print mid_end.say(character_three)
    
    if user_response == fine.response_one:
        print true_key.say(character_three)
    
    if user_response == fine.response_two:
        print waste.say(character_three)
    
    if node == final:
        print well.say(character_four)
        print '--------------------------------------------------'
        print "Type one of the following choices below EXACTLY as it is. This game is case sensitive."
        print well.response_one
        print well.response_two
        print '--------------------------------------------------'
    
    if user_response == well.response_one:
        print magical.say(character_four)
        print '--------------------------------------------------'
        print "Type one of the following choices below EXACTLY as it is. This game is case sensitive."
        print magical.response_one
        print magical.response_two
        print '--------------------------------------------------'
        
    if user_response == well.response_two:
        print confused.say(character_four)
        print '--------------------------------------------------'
        print "Type one of the following choices below EXACTLY as it is. This game is case sensitive."
        print confused.response_one
        print confused.response_two
        print '--------------------------------------------------'
    
    if user_response == magical.response_one:
        print the_cure.say(character_four)
        print "You have beat the game, despite the tragic ending. From here, you, now in depression, pick up the cookie and eat it without remorse. And then you proceed to explore the vast land of Seaborath, now a permanent land of hell and nightmares."
        sys.exit(0)
        
    if user_response == magical.response_two:
        print absolutely.say(character_four)
        print "You have beat the game, despite the tragic ending. From here, you, now in depression, pick up the cookie and eat it without remorse. And then you proceed to explore the vast land of Seaborath, now a permanent land of hell and nightmares."
        sys.exit(0)
    
    if user_response == confused.response_one:
        print honesty.say(character_four)
        print '--------------------------------------------------'
        print "Type one of the following choices below EXACTLY as it is. This game is case sensitive."
        print honesty.response_one
        print honesty.response_two
        print '--------------------------------------------------'
    
    if user_response == confused.response_two:
        print furious.say(character_four)
        print '--------------------------------------------------'
        print "Type one of the following choices below EXACTLY as it is. This game is case sensitive."
        print furious.response_one
        print furious.response_two
        print '--------------------------------------------------'
    
    if user_response == furious.response_one:
        print nothing_here.say(character_four)
        print "You have now beaten the game. Sure, the ending was pretty pointless, but yeah. From here, your character finally accepts the fate of Seaborath. Nothing can fix it. There is no cure. Out of anger, you crush the cookie to pieces and leave the vault into the unknown."
        sys.exit(0)
        
    if user_response == furious.response_two:
        print heated.say(character_four)
        print "You have lost. Due to your stupid choices in dialogue, you have angered a COOKIE. From here, the cookie turns out to be a mutated monster and jumps you. You could not fight back due to its immense strength and therefore died on the spot. Better luck next time."
        sys.exit(0)
    
    if user_response == honesty.response_one:
        print yeah.say(character_four)
        print "You have beat the game, despite the tragic ending. From here, you, now in depression, pick up the cookie and eat it. After a while, you come to accept the New Seaborath. Your past remains unknown, but you are OK with that. From here, your fate remains unknown."
        sys.exit(0)
    
    if user_response == honesty.response_two:
        print indeed.say(character_four)
        print "You have beat the game, despite the tragic ending. From here, you, now in depression, pick up the cookie and eat it without remorse. And then you proceed to explore the vast land of Seaborath, now a permanent land of hell and nightmares."
        sys.exit(0)
    
    
        

