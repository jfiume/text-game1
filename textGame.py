from gameEngine import *
from sys import exit
from random import randint

# create the Death class
class Death(Room):

    quips = [
        "So sorry you died. Better luck next time.",
        "In the next life perhaps...",
        "What a waste to perish now.",
        "Maybe try again, but without the dying part?"
    ]
    
    # Prints out random death lines
    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

# create the WhaleRoom class
class WhaleRoom(Room):

    def enter(self):
        print "You enter a room full of whales. The whales seem very nice but"
        print "you can't help but notice that there is no way out of this room and"
        print "the door has closed and locked behind you. You are trapped with these whales."
        print "Should you befriend the whales or kill the whales? (befriend, kill)"
        
        # user input
        action = raw_input("> ")

        if action == "kill":
            print "You are a monster. The whales are too intelligent and discover"
            print "that you are trying to kill them. They kill you 1st and you die."
            return 'death'

        elif action == "befriend":
            print "You are kind to the whales and the whales return your kindness by"
            print "uncovering a secret door behind them which they blow open for you"
            print "by spouting water out of their blowholes."
            return 'nap_room'

        else:
            print "Not a choice!"
            return 'whale_room'

# create the NapRoom class
class NapRoom(Room):

    def enter(self):
        print "You have befriended the whales and now you find yourself in a another room."
        print "This room is different. Its full of blankets and pillows. You find yourself"
        print "Very sleeply. zzzzzzzzzzzzzzzzzz"
        print "So tired. zzzzzzzzzzzzzzzzzz"
        print "Do you ever want to wake up? (yes, no)"

        # user input
        action = raw_input("> ")

        if action == "no":
            print "You sleep forever and ever and EVER"
            print "You never wake up and die."
            return 'death'

        elif action == "yes":
            print "You sleep for a very lone time but awake rested and happy."
            print " :) "
            return 'toy_room'

        else:
            print "Not a choice!"
            return 'nap_room'

# create the ToyRoom class
class ToyRoom(Room):

    def enter(self):
        print "After your nice restful nap, you walk into an adjacent room that you couldn't "
        print "see previously because you were so tired and sleepy. You find this room is full of toys!"
        print "You play with all the toys, except for one toy. This toy guards the toy room. He is a "
        print "9 foot tall wooden toy soldier. He warns that most people who play with the toys in this "
        print "room never leave. But, you don't care because these toys are the best toys. They are all "
        print "the toys from when you were a child. Eventually you stop playing with the toys and you "
        print "want to leave the toy room. However, the 9 foot tall wooden toy soldier won't let you leave."
        print "Do you fight him? (yes, no)"

        # user input
        action = raw_input("> ")

        # user input
        action2 = raw_input("Enter a number between 0 and 9 to hit the wooden soldier's weak spots.")
        code = "%d" % randint(1,9)
        # for when you want a cheet code:
        # print code
        while action2 != code:

            if action == "yes":
                print "You start to fight him but he's very powerful. You have to hit his weak spots. >"

                if action == code:
                    print "You scored a critial hit and defeated the wooden soldier."

                    return 'finished'

                elif action2 > code:
                    print "You scored a hit on the wooden soldier's weak spot!"
                    action2 = raw_input("Enter a number between 0 and 9 to hit the wooden soldier's weak spots. >")

                elif action2 < code:
                    print "You missed a weak spot and the wooden soldier took no damage."
                    action2 = raw_input("Enter a number between 0 and 9 to hit the wooden soldier's weak spots. >")

            if action == "no":
                print "You don't fight him and stay in the toy room forever and die."
                return 'death'

# create the Finished class
# I'm not sure why but it causes a bug in the game engine
class Finished(Room):

    def enter(self):
        print "Congratulations you Won!"
        return 'finished'

# create the Map class
class Map(object):

    # define the rooms the user will play through
    rooms = {
        'whale_room': WhaleRoom(),
        'nap_room': NapRoom(),
        'toy_room': ToyRoom(),
        'death': Death(),
        'finished': Finished(),
    }

    # init funcion
    def __init__(self, start_room):
        self.start_room = start_room

    # next_room function takes user from room to room
    def next_room(self, room_name):
        return Map.rooms.get(room_name)

    # first_room function starts the game
    def first_room(self):
        return self.next_room(self.start_room)

# play the game...
a_room = Map('whale_room')
a_game = Engine(a_room)
a_game.play()
