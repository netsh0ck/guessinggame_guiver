

import sys
import easygui
from random import *

treasurenum = randrange(1,10)
# debug print(treasurenum)

easygui.msgbox("Ahoy! I have a number between 1 && 10. Find it and you will find my treasure!")

counter=0



while int(treasurenum) != 0 and int(counter) < 5:
    myguess = easygui.enterbox("What's yer guess?","Treasure Number")

    if int(myguess) == 0:
        easygui.msgbox("Ahoy! Enter yer number not zero! Hararhar!")
        myguess = easygui.enterbox("What's yer guess?","Treasure Number")
    
    if int(myguess) < treasurenum:
        easygui.msgbox("YAR! Too low. Try again.")
        counter+=1
    elif int(myguess) > treasurenum:
        easygui.msgbox("YAR! Too high. Try again.")
        counter+=1
    elif int(myguess) == treasurenum:
        easygui.msgbox("Argh! You found my yer sekret treasure number! It was " + str(treasurenum))
        choices=['Yes!',"No."]
        mychoice = easygui.choicebox("Would you like to kontinue playing this game?","",choices)
        if mychoice == choices[0]:
            print("Restarting ///")
            #generate new random
            treasurenum=randrange(1,10)
            #continue from the start
            continue
        else:
            easygui.msgbox("Thanks yer for playing.")
            sys.exit(0)
    
    if counter == 5:
        easygui.msgbox("Sorry laddie! No more yer guesses! Better luck next time. Thanks yer for playing!")
        quit()




                 
