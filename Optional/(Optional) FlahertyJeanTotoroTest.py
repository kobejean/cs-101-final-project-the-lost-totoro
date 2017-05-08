###########################################################################
#                            Linear Story                                 #
#                                                                         #
#  Programmed by Jean Flaherty (10-27-2016)                               #
#                                                                         #
#  The following is a template for an animated linear story.  Students    #
#  add pages and content to this template, as appropriate.                #
#                                                                         #
#  EXTERNAL FILES                                                         #
#  The following external files are used in the process of running the    #
#  animation.                                                             #
#   Bots:                                                                 #
#       FlahertyJeanBotTotoro, by Jean Flaherty                           #
#           Totoro -- An animatable totoro character                      #
#           Action -- Enumerated data type for 5 different actions        #
#           SacredItem -- Graphical representation of a Sacred Item       #
#           SacredItemType -- Enumerated data type for 3 SacredItemTypes  #
#                                                                         #
#  This program is copyright (c) 2016 Jean Flaherty and Dean Zeller.      #
#  All rights reserved.  Permission granted to use and modify for         #
#  educational purposes only.  Any commercial use of this code must       #
#  receive permission from the author(s).                                 #
###########################################################################

# import bots
from FlahertyJeanBotTotoro import Totoro
from FlahertyJeanBotTotoro import TotoroCoordinator
from FlahertyJeanBotTotoro import Action
from FlahertyJeanBotTotoro import SacredItem
from FlahertyJeanBotTotoro import SacredItemType
# import others
from FlahertyJeanWorldMapNavigator import *
from FlahertyJeanAnimation import Animation
from tkinter import *
import math
import datetime

DEBUG_MODE = 1



c = Canvas(width=400, height=400, bg='white')
c.pack(expand=YES, fill=BOTH)

navigator = Navigator()


# create totoros
totoro1      = Totoro(c, left=0, top=0, width=150, height=150,
                bodyColor="#736F5F", 
                action=Action.STOP, name="Big Totoro",
                sacredItemType=SacredItemType.UMBRELLA)
totoro2      = Totoro(c, left=0, top=0, width=150, height=150,
                bodyColor="white", 
                action=Action.STOP, name="Big Totoro",
                sacredItemType=SacredItemType.UMBRELLA)

frame_count = 210

    

def setup():
    totoro1.sacredItem.type = SacredItemType.UMBRELLA
    totoro1.setAction(Action.STOP)
    totoro1.position(50,385)
    totoro1.resize(40,40)
    totoro1.redraw()
    totoro1.stepRatio = 0.1

    totoro2.sacredItem.type = SacredItemType.CAMPHORLEAF
    totoro2.setAction(Action.STOP)
    totoro2.position(350,385)
    totoro2.resize(20,20)
    totoro2.redraw()
    totoro2.stepRatio = 0.1
    
def timeline1(t):
    totoro1.move(1,-1)
    totoro2.move(-1,-1)

    
def timeline2(t):
    if t == 10:
        totoro1.walkTo(200,385)
        totoro2.walkTo(50,385)
    elif t == 60:
        totoro1.walkTo(350,385)

def timeline3(t):
    if t == 10:
        totoro1.path = [(200,385), (200,285), (50,285)]
        totoro2.path = [(50,385)]

        
def completion():
    print("Done!")   

totoroCoordinator = TotoroCoordinator(c, [totoro1, totoro2])
totoroCoordinator.reset = setup
totoroCoordinator.timeline = timeline1
totoroCoordinator.completion = completion
totoroCoordinator.frame_count = frame_count
totoroCoordinator.fps = 1
totoroCoordinator.play()
