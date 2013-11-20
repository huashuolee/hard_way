print "You enter a dark room with too doors. Do you go through door #1 or door #2?"
door = raw_input("> ")
if door == "1":
    print "These's a giant bear here eating a cheese cake. what do you do?"
    print "1. Take the cake."
    print "2. Screem at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probalby bettery. Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins"
    print "3. Understanding revolverts yelling melodies."

    insanity = raw_input("> ")
    if insanity =="1" or insanity == "2":
        print "Your body survices powered by a mind of jello. Good jobs!"
    else:
        print "THe insanity rots your eyes into a pool of muck. Good jobs!"

else:
    print "You tumble around and fall on a knife and die. Good job!"

