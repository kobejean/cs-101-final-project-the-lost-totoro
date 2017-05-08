###########################################################################
#                            The Lost Totoro                              #
#                                                                         #
#  Programmed by Jean Flaherty (12-03-2016)                               #
#  Instructor:  Dean Zeller                                               #
#                                                                         #
#  This is a story of a bored totoro who decided to tour the world.       #
#  He was no longer bored. However, he soon got lost. We used search      #
#  algorithms to help him find his way back to Japan. Once he got home,   #
#  he lived happily ever after.                                           #
#                                                                         #
#  EXTERNAL FILES                                                         #
#  The following external files are used in the process of running the    #
#  animation.                                                             #
#   Bots:                                                                 #
#       FlahertyJeanBotTotoro, by Jean Flaherty                           #
#           Totoro -- An animatable totoro character                      #
#           TotoroCoordinator -- Handels animating the Totoro             #
#           Action -- Enumerated data type for 5 different actions        #
#           SacredItem -- Graphical representation of a Sacred Item       #
#           SacredItemType -- Enumerated data type for 3 SacredItemTypes  #
#       Butterfly, by Megan Rink                                          #
#           Butterfly -- A traditional butterfly bot                      #
#           Pose -- Enum 5 different butterfly poses                      #
#                                                                         #
#   Scenery:                                                              #
#       Bridge, by Joe Rider                                              #
#       chichenitza, by Kassan Qian                                       #
#       CityModern, by Mark Buerck                                        #
#       Desert, by Ian Micklethwaite                                      #
#       Forest, by Taylor Planchon                                        #
#       greatWallOfChina, by Kassan Qian                                  #
#       Paris, by Taylor Fields                                           #
#       Rockies, by Gabriela Rivera                                       #
#       tajmahal, by Kassan Qian                                          #
#       TVRoom, by Tim Adams                                              #
#       UnderSea, by Selena Baltierra                                     #
#       WelleConnorIceCave, by Connor Welle                               #
#       FlahertyJeanWorldMap, by Jean Flaherty                            #
#                                                                         #
#   Others:                                                               #
#       FlahertyJeanWorldMapNavigator, by Jean Flaherty                   #
#           Navigator -- Used in the search algorithm scene               #
#           SearchAlgorithm -- An enum for the different search algorithms#
#       FlahertyJeanAnimation, by Jean Flaherty                           #
#           Animation -- an object that handels animations                #
#       FlahertyJeanTotoroMusicBox, by Jean Flaherty                      #
#           TotoroMusicTheme -- Enum that represents a track in music box #
#           TotoroMusicBox -- An object that handels playing music        #
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
from Butterfly import Butterfly
from Butterfly import Pose as ButterflyPose
# import scenes
from Bridge import scenery_bridge
from chichenitza import chichenitza
from CityModern import city_scenery
from Desert import desert_scenery
from Forest import forest
from greatWallOfChina import greatwall
from Paris import paris_scenery
from Rockies import mountain_scenery
from tajmahal import tajmahal
from TVRoom import tv_room
from UnderSea import under_the_sea
from WelleConnorIceCave import icecave_scenery
from FlahertyJeanWorldMap import world_map
# import others
from FlahertyJeanWorldMapNavigator import *
from FlahertyJeanAnimation import Animation
from FlahertyJeanTotoroMusicBox import TotoroMusicBox
from FlahertyJeanTotoroMusicBox import TotoroMusicTheme
from tkinter import *
import math
import datetime

###########################################################################
#  draw label                                                             #
#                                                                         #
#  This function is used to draw a label on the top right corner and is   #
#  used to tell the audiance where the current scene takes place (India,  #
#  China, Mexico, Paris .ect).                                            #
###########################################################################
def drawLabel(c, text="untitled"):
    c.delete("label")
    c.create_rectangle(390,15,250,55,fill="#DE8338",tag="label")
    c.create_text(320,36,text=text,font=("Helvetica",18), fill="white",tag="label")

###########################################################################
#  draw annotation                                                        #
#                                                                         #
#  This function is used to draw text annotations.                        #
###########################################################################
def drawAnnotation(c, text="untitled"):
    c.delete("annotation")
    # shadow
    c.create_text(200,370,text=text,font=("Helvetica",10), fill="black", tag="annotation")
    # text
    c.create_text(201,371,text=text,font=("Helvetica",10), fill="white", tag="annotation")

###########################################################################
#  default event                                                          #
#                                                                         #
#  Serves as the default event when any key is pressed that has not been  #
#  bound.                                                                 #
###########################################################################
def default(event):
    print("Warning -- unbound key entered")

# just a placeholder function that can be called without doing anything
def blank(): pass
# global variable for passing clean up code to other pages
clean_up_previous_page = blank


###########################################################################
#  Title Page                                                             #
#                                                                         #
#  Shows the title of the story "The Lost Totoro" and displays instruct-  #
#  ions for starting the story.                                           #
###########################################################################
def titlepage(event=None):
    # this will be called when changing to the next page
    def clean_up():
        c.delete(ALL)
    global clean_up_previous_page
    clean_up_previous_page()
    clean_up_previous_page = clean_up
    # make sure there is no music
    musicbox.theme = TotoroMusicTheme.NONE
    
    # background color
    c.create_rectangle(5,5,400,400,fill="#DE8338")
    # draw text
    c.create_text(200,50,text="The Lost Totoro",font=("Helvetica",36), fill="white")
    c.create_text(200,200,text="Click on canvas and hit 'tab' to start story", fill="white")
    c.bind("<Button>",page1)  # binds mouse click to draw first scene
    
###########################################################################
#  Credits page                                                           #
#                                                                         #
#  This page displays the credits for the program in a scrolling textbox. #
###########################################################################
def creditsPage(event=None):
    # this will be called when changing to the next page
    def clean_up():
        c.delete(ALL)
    global clean_up_previous_page
    clean_up_previous_page()
    clean_up_previous_page = clean_up
    # make sure there the right track is playing
    musicbox.theme = TotoroMusicTheme.MOTHER
    
    c.unbind("<Button>")
    
    # background color
    c.create_rectangle(5,5,400,400,fill="#DE8338")

    totoro1      = Totoro(c, left=0, top=0, width=75, height=75,
                    bodyColor="#736F5F", 
                    action=Action.STOP, name="Big Totoro",
                    sacredItemType=SacredItemType.UMBRELLA)
    totoro2      = Totoro(c, left=0, top=0, width=50, height=50,
                    bodyColor="#486189", 
                    action=Action.STOP, name="Middle Totoro",
                    sacredItemType=SacredItemType.KUDZULEAF)
    totoro3      = Totoro(c, left=0, top=0, width=25, height=25,
                    bodyColor="#ffffff", 
                    action=Action.STOP, name="Small Totoro",
                    sacredItemType=SacredItemType.KUDZULEAF)
    butterfly1     = Butterfly(c, left=-10, top=350, width=30, height=30,
                       wingColor='gold', wingColor2='gold3',
                        pose=ButterflyPose.WINGSIN, name='win', displayName=0)

    # Animation for credits page 
    stuff="Totoro got home safely!"
    temp = c.create_text(200,200,text=stuff, font=("helvetica",14), anchor=S, fill="white")
    c.update()
    
    stuff='''
The Lost Totoro

WRITTEN and PROGRAMMED by
Jean Flaherty

SCENERY by
Bridge -- Joe Rider
Chichenitza -- Gabriela Rivera
City Modern -- Mark Buerck
Desert -- Ian Micklethwaite
Forest -- Taylor Planchon
Great Wall -- Gabriela Rivera
Paris -- Taylor Fields
Rockies -- Gabriela Rivera
Tajmahal -- Gabriela Rivera
TV Room -- Tim Adams
A Peek Under the Sea -- Selena Baltierra
Ice Cave -- Connor Welle
World Map -- Jean Flaherty


BOTS by
Totoro -- Jean Flaherty
Butterfly -- Megan Rink

SEARCH ALGORITHMS Adapted from:
MIT OCW 6.01SC Lecture 12 -- Leslie Kaelbling
MIT OCW 6.01SC Lecture 13 -- Leslie Kaelbling
MIT OCW 6.034 Lecture 4 -- Patrick H. Winston

MUSIC
Sampo -- Jean Flaherty
Mei is Missing -- Jean Flaherty
The Path of the Wind -- Jean Flaherty
Totoro -- Jean Flaherty
Mother -- Jean Flaherty

INSTRUMENT
Guitar -- Austin Shroyer's guitar


All code (c)2016 by their respective authors.


THE END
'''
    creds=c.create_text(200,800, text=stuff, justify=CENTER, fill="white", tag="credits")

    # set up animation
    frame_count = 1300
    def setup():
        totoro1.sacredItem.type = SacredItemType.UMBRELLA
        totoro1.setAction(Action.STOP)
        totoro1.position(-100,385)
        totoro1.resize(75,75)
        totoro1.redraw()
        totoro1.stepRatio = 0.05

        totoro2.sacredItem.type = SacredItemType.KUDZULEAF
        totoro2.setAction(Action.STOP)
        totoro2.position(-100,385)
        totoro2.resize(50,50)
        totoro2.redraw()
        
        totoro3.sacredItem.type = SacredItemType.CAMPHORLEAF
        totoro3.setAction(Action.STOP)
        totoro3.position(-100,385)
        totoro3.resize(25,25)
        totoro3.redraw()
    def timeline(t):
        c.move(creds, 0,-1.5)
        if t == 0:
            totoro1.walkTo(200,385)
        elif t == 100:
            totoro2.walkTo(250,385)
            totoro3.walkTo(150,385)
        elif t == 150:
            c.delete(temp)  # remove message at the right time
        elif t == 200:
            # worship animation
            totoro1.setAction(Action.WORSHIPING)
            totoro2.setAction(Action.WORSHIPING)
            totoro3.setAction(Action.WORSHIPING)
            # offset time
            totoro1.time = 4
            totoro2.time = 6
            totoro3.time = 8
        elif t == 370:
            totoro1.walkTo(500,385)
            totoro2.walkTo(500,385)
            totoro3.walkTo(500,385)
        elif t > 380 and t < 550:
            butterfly1.nextPose()
            butterfly1.move(3,-1, delay=0)

        c.tag_raise("credits")# bring to front
            
    def completion():
        print("done!")

    totoroCoordinator = TotoroCoordinator(c, [totoro1, totoro2, totoro3])
    totoroCoordinator.reset = setup
    totoroCoordinator.timeline = timeline
    totoroCoordinator.completion = completion
    totoroCoordinator.frame_count = frame_count
    totoroCoordinator.fpms = 30
    totoroCoordinator.play()
            
###########################################################################
#  Page 1 -- TV Room                                                      #
#                                                                         #
#  Totoro is bored so he decides he wants to tour the world.              #
###########################################################################
def page1(event=None):
    # this will be called when changing to the next page
    def clean_up():
        c.delete(ALL)
        Animation.stop()
    global clean_up_previous_page
    clean_up_previous_page()
    clean_up_previous_page = clean_up
    # make sure there the right track is playing
    musicbox.theme = TotoroMusicTheme.SAMPO
    
    c.bind("<Button>",page2)
    tv_room(c)
    drawLabel(c, text="Home")

    # create totoros
    totoro1      = Totoro(c, left=0, top=0, width=150, height=150,
                    bodyColor="#736F5F", 
                    action=Action.STOP, name="Big Totoro",
                    sacredItemType=SacredItemType.UMBRELLA)

    # set up animation
    frame_count = 250
    def setup():
        totoro1.sacredItem.type = SacredItemType.UMBRELLA
        totoro1.setAction(Action.STOP)
        totoro1.position(200,385)
        totoro1.resize(150,150)
        totoro1.redraw()
    def timeline(t): 
        totoro1.stepRatio = 0.05
        c.tag_raise("annotation")# bring to front
        if t == 10:
            totoro1.walkTo(300,385)
            drawAnnotation(c, text="Totoro is bored...")
        elif t == 40:
            totoro1.walkTo(100,385)
        elif t == 90:
            drawAnnotation(c, text="What should he do?")
        elif t == 150:
            drawAnnotation(c, text="Totoro decides to travel the world")
    def completion():
        drawAnnotation(c, text="Click to continue...")

    totoroCoordinator = TotoroCoordinator(c, [totoro1])
    totoroCoordinator.reset = setup
    totoroCoordinator.timeline = timeline
    totoroCoordinator.completion = completion
    totoroCoordinator.frame_count = frame_count
    totoroCoordinator.play()

###########################################################################
#  Page 2 -- Tajmahal                                                     #
#                                                                         #
#  Totoro goes to India.                                                  #
###########################################################################
def page2(event=None):
    # this will be called when changing to the next page
    def clean_up():
        c.delete(ALL)
        Animation.stop()
    global clean_up_previous_page
    clean_up_previous_page()
    clean_up_previous_page = clean_up
    # make sure there the right track is playing
    musicbox.theme = TotoroMusicTheme.SAMPO
    
    c.bind("<Button>",page3)
    tajmahal(c, tag="tajmahal") #calling the function
    c.scale("tajmahal", 0, 0, 400/945, 400/600)
    drawLabel(c, text="India")

    # create totoros
    totoro1      = Totoro(c, left=0, top=0, width=150, height=150,
                    bodyColor="#736F5F", 
                    action=Action.STOP, name="Big Totoro",
                    sacredItemType=SacredItemType.UMBRELLA)
    butterfly1     = Butterfly(c, left=400, top=350, width=30, height=30,
                   wingColor='gold', wingColor2='gold3',
                    pose=ButterflyPose.WINGSIN, name='win', displayName=0)

    # set up animation
    frame_count = 240
    def setup():
        totoro1.sacredItem.type = SacredItemType.UMBRELLA
        totoro1.setAction(Action.STOP)
        totoro1.position(200,335)
        totoro1.resize(20,20)
        totoro1.redraw()
    def timeline(t):
        totoro1.stepRatio = 0.05

        butterfly1.nextPose()
        butterfly1.move(-3,-1, delay=0)
        
        c.tag_raise("annotation") # bring to front
        if t == 0:
            totoro1.walkTo(200,385)
            drawAnnotation(c, text="Totoro visited India...")
        elif t > 0 and t <= 30:
            totoro1.scale(1.03, 1.03)
        elif t == 70:
            drawAnnotation(c, text="He loved the Indian curry")
        elif t == 170:
            drawAnnotation(c, text="Totoro likes the idea of traveling")
    def completion():
        drawAnnotation(c, text="Click to continue...")

    totoroCoordinator = TotoroCoordinator(c, [totoro1])
    totoroCoordinator.reset = setup
    totoroCoordinator.timeline = timeline
    totoroCoordinator.completion = completion
    totoroCoordinator.frame_count = frame_count
    totoroCoordinator.play()

###########################################################################
#  Page 3 -- Chichenitza                                                  #
#                                                                         #
#  Totoro goes to Mexico.                                                 #
###########################################################################
def page3(event=None):
    # this will be called when changing to the next page
    def clean_up():
        c.delete(ALL)
        Animation.stop()
    global clean_up_previous_page
    clean_up_previous_page()
    clean_up_previous_page = clean_up
    # make sure there the right track is playing
    musicbox.theme = TotoroMusicTheme.SAMPO
    
    c.bind("<Button>",page4)
    chichenitza(c, tag="chichenitza") #calling the function
    c.scale("chichenitza", 0, 0, 400/950, 400/594) #fit square
    drawLabel(c, text="Mexico")

    # create totoros
    totoro1      = Totoro(c, left=0, top=0, width=150, height=150,
                    bodyColor="#736F5F", 
                    action=Action.STOP, name="Big Totoro",
                    sacredItemType=SacredItemType.UMBRELLA)

    # set up animation
    frame_count = 100
    def setup():
        totoro1.sacredItem.type = SacredItemType.UMBRELLA
        totoro1.setAction(Action.STOP)
        totoro1.position(280,260)
        totoro1.resize(50,50)
        totoro1.redraw()
    def timeline(t):
        totoro1.stepRatio = 0.05
        c.tag_raise("annotation")# bring to front
        if t == 0:
            totoro1.walkTo(230,140)
            drawAnnotation(c, text="Totoro went to Mexico")
        elif t > 0 and t <= 60:
            totoro1.scale(0.996, 0.996)
            if t == 40:
                drawAnnotation(c, text="Totoro likes Mexican food too")
    def completion():
        drawAnnotation(c, text="Click to continue...")
    totoroCoordinator = TotoroCoordinator(c, [totoro1])
    totoroCoordinator.reset = setup
    totoroCoordinator.timeline = timeline
    totoroCoordinator.completion = completion
    totoroCoordinator.frame_count = frame_count
    totoroCoordinator.play()

###########################################################################
#  Page 4 -- Paris                                                        #
#                                                                         #
#  Totoro goes to Paris.                                                  #
###########################################################################
def page4(event=None):
    # this will be called when changing to the next page
    def clean_up():
        c.delete(ALL)
        Animation.stop()
    global clean_up_previous_page
    clean_up_previous_page()
    clean_up_previous_page = clean_up
    # make sure there the right track is playing
    musicbox.theme = TotoroMusicTheme.SAMPO
    
    c.bind("<Button>",page5)
    paris_scenery(c)
    drawLabel(c, text="Paris")

    # create totoros
    totoro1      = Totoro(c, left=0, top=0, width=150, height=150,
                    bodyColor="#736F5F", 
                    action=Action.STOP, name="Big Totoro",
                    sacredItemType=SacredItemType.UMBRELLA)
    
    # set up animation
    frame_count = 400
    def setup():
        totoro1.sacredItem.type = SacredItemType.UMBRELLA
        totoro1.setAction(Action.STOP)
        totoro1.position(105,70)
        totoro1.resize(35,35)
        totoro1.redraw()
    def timeline(t):
        totoro1.stepRatio = 0.05
        c.tag_raise("annotation")# bring to front
        if t == 0: 
            totoro1.setAction(Action.WORSHIPING)
            drawAnnotation(c, text="Totoro went to Paris too...")
        elif t == 70:
            drawAnnotation(c, text="He danced on top of the Eiffel Tower..")
        elif t == 140:
            drawAnnotation(c, text="He enjoying the view of the fireworks")
        elif t == 210:
            drawAnnotation(c, text="Click to continue...")

    def completion():
        totoro1.setAction(Action.STOP)

    totoroCoordinator = TotoroCoordinator(c, [totoro1])
    totoroCoordinator.reset = setup
    totoroCoordinator.timeline = timeline
    totoroCoordinator.completion = completion
    totoroCoordinator.frame_count = frame_count
    totoroCoordinator.play()

###########################################################################
#  Page 5 -- The Great Wall of China                                      #
#                                                                         #
#  Totoro goes to China.                                                  #
###########################################################################
def page5(event=None):
    # this will be called when changing to the next page
    def clean_up():
        c.delete(ALL)
        Animation.stop()
    global clean_up_previous_page
    clean_up_previous_page()
    clean_up_previous_page = clean_up
    # make sure there the right track is playing
    musicbox.theme = TotoroMusicTheme.SAMPO
    
    c.bind("<Button>",page6)
    greatwall(c, tag="greatwall") #calling the function
    c.scale("greatwall", 0, 0, 400/960, 400/600) #fit square
    drawLabel(c, text="China")

    # create totoros
    totoro1      = Totoro(c, left=0, top=0, width=150, height=150,
                    bodyColor="#736F5F", 
                    action=Action.STOP, name="Big Totoro",
                    sacredItemType=SacredItemType.UMBRELLA)
    
    # set up animation
    frame_count = 160
    def setup():
        totoro1.sacredItem.type = SacredItemType.UMBRELLA
        totoro1.setAction(Action.STOP)
        totoro1.position(305,170)
        totoro1.resize(35,35)
        totoro1.redraw()
    def timeline(t):
        totoro1.stepRatio = 0.05
        c.tag_raise("annotation")# bring to front
        if t == 0:
            totoro1.walkTo(285,370)
            drawAnnotation(c, text="Totoro visited the Great Wall of China")
        elif t == 70:
            drawAnnotation(c, text="It's a long wall")
    def completion():
        drawAnnotation(c, text="Click to continue...")

    totoroCoordinator = TotoroCoordinator(c, [totoro1])
    totoroCoordinator.reset = setup
    totoroCoordinator.timeline = timeline
    totoroCoordinator.completion = completion
    totoroCoordinator.frame_count = frame_count
    totoroCoordinator.play()

###########################################################################
#  Page 6 -- Modern City                                                  #
#                                                                         #
#  Totoro goes to New York.                                               #
###########################################################################
def page6(event=None):
    # this will be called when changing to the next page
    def clean_up():
        c.delete(ALL)
        Animation.stop()
    global clean_up_previous_page
    clean_up_previous_page()
    clean_up_previous_page = clean_up
    # make sure there the right track is playing
    musicbox.theme = TotoroMusicTheme.SAMPO
    
    c.bind("<Button>",page7)
    city_scenery(c)
    drawLabel(c, text="New York")

    # create totoros
    totoro1      = Totoro(c, left=0, top=0, width=150, height=150,
                    bodyColor="#736F5F", 
                    action=Action.STOP, name="Big Totoro",
                    sacredItemType=SacredItemType.UMBRELLA)

    # set up animation
    frame_count = 70
    def setup():
        totoro1.sacredItem.type = SacredItemType.UMBRELLA
        totoro1.setAction(Action.STOP)
        totoro1.position(75,170)
        totoro1.resize(35,35)
        totoro1.redraw()
    def timeline(t): 
        totoro1.stepRatio = 0.05
        c.tag_raise("annotation")# bring to front
        if t == 0:
            totoro1.setAction(Action.WORSHIPING)
    def completion():
        page7()

    totoroCoordinator = TotoroCoordinator(c, [totoro1])
    totoroCoordinator.reset = setup
    totoroCoordinator.timeline = timeline
    totoroCoordinator.completion = completion
    totoroCoordinator.frame_count = frame_count
    totoroCoordinator.play()

###########################################################################
#  Page 7 -- Rockies                                                      #
#                                                                         #
#  Totoro goes to Colorado.                                               #
###########################################################################
def page7(event=None):
    # this will be called when changing to the next page
    def clean_up():
        c.delete(ALL)
        Animation.stop()
    global clean_up_previous_page
    clean_up_previous_page()
    clean_up_previous_page = clean_up
    # make sure there the right track is playing
    musicbox.theme = TotoroMusicTheme.SAMPO
    
    c.bind("<Button>",page8)
    mountain_scenery(c)
    drawLabel(c, text="Colorado")

    # create totoros
    totoro1      = Totoro(c, left=0, top=0, width=150, height=150,
                    bodyColor="#736F5F", 
                    action=Action.STOP, name="Big Totoro",
                    sacredItemType=SacredItemType.UMBRELLA)
    butterfly1     = Butterfly(c, left=0, top=350, width=30, height=30,
                       wingColor='gold', wingColor2='gold3',
                        pose=ButterflyPose.WINGSIN, name='win', displayName=0)

    # set up animation
    frame_count = 90
    def setup():
        totoro1.sacredItem.type = SacredItemType.UMBRELLA
        totoro1.setAction(Action.STOP)
        totoro1.position(100,385)
        totoro1.resize(35,35)
        totoro1.redraw()
    def timeline(t):
        totoro1.stepRatio = 0.1

        butterfly1.nextPose()
        butterfly1.move(3,-1, delay=0)
        
        c.tag_raise("annotation")# bring to front
        if t == 0:
            totoro1.walkTo(200,385)
        elif t == 40:
            totoro1.sacredItem.type = SacredItemType.CAMPHORLEAF
        elif t == 50:
            totoro1.sacredItem.type = SacredItemType.KUDZULEAF
        elif t == 60:
            totoro1.setAction(Action.WORSHIPING)
    def completion():
        page8()

    totoroCoordinator = TotoroCoordinator(c, [totoro1])
    totoroCoordinator.reset = setup
    totoroCoordinator.timeline = timeline
    totoroCoordinator.completion = completion
    totoroCoordinator.frame_count = frame_count
    totoroCoordinator.play()

###########################################################################
#  Page 8 -- Bridge                                                       #
#                                                                         #
#  Totoro goes to San Francisco.                                          #
###########################################################################
def page8(event=None):
    # this will be called when changing to the next page
    def clean_up():
        c.delete(ALL)
        Animation.stop()
    global clean_up_previous_page
    clean_up_previous_page()
    clean_up_previous_page = clean_up
    # make sure there the right track is playing
    musicbox.theme = TotoroMusicTheme.SAMPO
    
    c.bind("<Button>",page9)
    scenery_bridge(c)
    drawLabel(c, text="San Francisco")

    # create totoros
    totoro1      = Totoro(c, left=0, top=0, width=150, height=150,
                    bodyColor="#736F5F", 
                    action=Action.STOP, name="Big Totoro",
                    sacredItemType=SacredItemType.UMBRELLA)

    # set up animation
    frame_count = 60
    def setup():
        totoro1.sacredItem.type = SacredItemType.KUDZULEAF
        totoro1.setAction(Action.STOP)
        totoro1.position(275,200)
        totoro1.resize(35,35)
        totoro1.redraw()
    def timeline(t): 
        totoro1.stepRatio = 0.05
        c.tag_raise("annotation")# bring to front
        if t == 0: 
            totoro1.setAction(Action.WORSHIPING)
    def completion():
        page9() 

    totoroCoordinator = TotoroCoordinator(c, [totoro1])
    totoroCoordinator.reset = setup
    totoroCoordinator.timeline = timeline
    totoroCoordinator.completion = completion
    totoroCoordinator.frame_count = frame_count
    totoroCoordinator.play()

###########################################################################
#  Page 9 -- Forest                                                       #
#                                                                         #
#  Totoro doesn't know where he is anymore.                               #
###########################################################################
def page9(event=None):
    # this will be called when changing to the next page
    def clean_up():
        c.delete(ALL)
        Animation.stop()
    global clean_up_previous_page
    clean_up_previous_page()
    clean_up_previous_page = clean_up
    # make sure there the right track is playing
    musicbox.theme = TotoroMusicTheme.MEI_IS_MISSING
    
    c.bind("<Button>",page10)
    forest(c)
    drawLabel(c, text="??????")
    
    # create totoros
    totoro1      = Totoro(c, left=0, top=0, width=150, height=150,
                    bodyColor="#736F5F", 
                    action=Action.STOP, name="Big Totoro",
                    sacredItemType=SacredItemType.UMBRELLA)

    # set up animation
    frame_count = 210
    def setup():
        totoro1.sacredItem.type = SacredItemType.KUDZULEAF
        totoro1.setAction(Action.STOP)
        totoro1.position(240,305)
        totoro1.resize(35,35)
        totoro1.redraw()        
    def timeline(t):
        totoro1.stepRatio = 0.05
        c.tag_raise("annotation")# bring to front
        if t == 0:
            totoro1.walkTo(170,385)
            drawAnnotation(c, text="Totoro had so much fun but now he's lost...")
        elif t > 0 and t <= 40:
            totoro1.scale(1.02, 1.02)
        elif t == 50:
            totoro1.advance(40,0)
        elif t == 70:
            totoro1.advance(-80,0)
        elif t == 110:
            totoro1.advance(40,0)
        elif t == 130:
            totoro1.walkTo(290,235)
        elif t > 130 and t < 210:
            totoro1.scale(1/1.02, 1/1.02)
    def completion():
        page10()

    totoroCoordinator = TotoroCoordinator(c, [totoro1])
    totoroCoordinator.reset = setup
    totoroCoordinator.timeline = timeline
    totoroCoordinator.completion = completion
    totoroCoordinator.frame_count = frame_count
    totoroCoordinator.fpms = 50
    totoroCoordinator.play()

###########################################################################
#  Page 10 -- Icecave                                                     #
#                                                                         #
#  Totoro is officially lost.                                             #
###########################################################################
def page10(event=None):
    # this will be called when changing to the next page
    def clean_up():
        c.delete(ALL)
        Animation.stop()
    global clean_up_previous_page
    clean_up_previous_page()
    clean_up_previous_page = clean_up
    # make sure there the right track is playing
    musicbox.theme = TotoroMusicTheme.MEI_IS_MISSING
    
    c.bind("<Button>",page11)
    icecave_scenery(c)
    drawLabel(c, text="Lost")

    # create totoros
    totoro1      = Totoro(c, left=0, top=0, width=150, height=150,
                    bodyColor="#736F5F", 
                    action=Action.STOP, name="Big Totoro",
                    sacredItemType=SacredItemType.UMBRELLA)

    frame_count = 140
    def setup(): 
        totoro1.sacredItem.type = SacredItemType.KUDZULEAF
        totoro1.setAction(Action.STOP)
        totoro1.position(350,385)
        totoro1.resize(40,40)
        totoro1.redraw()
    def timeline(t):
        totoro1.stepRatio = 0.1
        c.tag_raise("annotation")# bring to front
        if t == 1:
            totoro1.walkTo(200,385)
        elif t == 50:
            totoro1.sacredItem.type = SacredItemType.UMBRELLA
        elif t == 60:
            totoro1.sacredItem.type = SacredItemType.CAMPHORLEAF
        elif t == 80:
            totoro1.walkTo(50,385)
    def completion():
        page11() 

    totoroCoordinator = TotoroCoordinator(c, [totoro1])
    totoroCoordinator.reset = setup
    totoroCoordinator.timeline = timeline
    totoroCoordinator.completion = completion
    totoroCoordinator.frame_count = frame_count
    totoroCoordinator.fpms = 50
    totoroCoordinator.play()

###########################################################################
#  Page 11 -- Under Sea                                                   #
#                                                                         #
#  Totoro is officially lost.                                             #
###########################################################################
def page11(event=None):
    # this will be called when changing to the next page
    def clean_up():
        c.delete(ALL)
        Animation.stop()
    global clean_up_previous_page
    clean_up_previous_page()
    clean_up_previous_page = clean_up
    # make sure there the right track is playing
    musicbox.theme = TotoroMusicTheme.MEI_IS_MISSING
    
    c.bind("<Button>",page12)
    under_the_sea(c)
    drawLabel(c, text="Still Lost")

    # create totoros
    totoro1      = Totoro(c, left=0, top=0, width=150, height=150,
                    bodyColor="#736F5F", 
                    action=Action.STOP, name="Big Totoro",
                    sacredItemType=SacredItemType.UMBRELLA)

    frame_count = 110
    def setup(): 
        totoro1.sacredItem.type = SacredItemType.CAMPHORLEAF
        totoro1.setAction(Action.STOP)
        totoro1.position(50,385)
        totoro1.resize(40,40)
        totoro1.redraw()
    def timeline(t):
        totoro1.stepRatio = 0.1
        c.tag_raise("annotation")# bring to front
        if t == 10:
            totoro1.walkTo(200,385)
        elif t == 60:
            totoro1.walkTo(350,385)
    def completion():
        page12()

    totoroCoordinator = TotoroCoordinator(c, [totoro1])
    totoroCoordinator.reset = setup
    totoroCoordinator.timeline = timeline
    totoroCoordinator.completion = completion
    totoroCoordinator.frame_count = frame_count
    totoroCoordinator.fpms = 50
    totoroCoordinator.play()

###########################################################################
#  Page 12 -- Desert                                                      #
#                                                                         #
#  Totoro is officially lost.                                             #
###########################################################################
def page12(event=None):
    # this will be called when changing to the next page
    def clean_up():
        c.delete(ALL)
        Animation.stop()
    global clean_up_previous_page
    clean_up_previous_page()
    clean_up_previous_page = clean_up
    # make sure there the right track is playing
    musicbox.theme = TotoroMusicTheme.MEI_IS_MISSING
    
    c.bind("<Button>",page13)
    desert_scenery(c)
    drawLabel(c, text="Very Lost")

    # create totoros
    totoro1      = Totoro(c, left=0, top=0, width=150, height=150,
                    bodyColor="#736F5F", 
                    action=Action.STOP, name="Big Totoro",
                    sacredItemType=SacredItemType.UMBRELLA)

    frame_count = 250
    def setup():
        totoro1.sacredItem.type = SacredItemType.CAMPHORLEAF
        totoro1.setAction(Action.STOP)
        totoro1.position(210,300)
        totoro1.resize(20,20)
        totoro1.redraw()
    def timeline(t):
        totoro1.stepRatio = 0.1
        c.tag_raise("annotation")# bring to front
        if t == 10:
            totoro1.walkTo(350,385)
        elif t > 10 and t < 50:
            totoro1.scale(1.03, 1.03)
        elif t == 80:
            totoro1.walkTo(200,385)
        elif t == 120:
            totoro1.resize(5,5)
            totoro1.position(130,150)
            totoro1.advance(20,0)
        elif t == 170:
            totoro1.resize(15,15)
            totoro1.position(350,250)
            totoro1.advance(-60,0)
    def completion():
        page13()    

    totoroCoordinator = TotoroCoordinator(c, [totoro1])
    totoroCoordinator.reset = setup
    totoroCoordinator.timeline = timeline
    totoroCoordinator.completion = completion
    totoroCoordinator.frame_count = frame_count
    totoroCoordinator.fpms = 50
    totoroCoordinator.play()

###########################################################################
#  Page 13 -- Let's Help Totoro                                           #
#                                                                         #
#  Text on a page                                                         #
###########################################################################
def page13(event=None):
    # this will be called when changing to the next page
    def clean_up():
        c.delete(ALL)
    global clean_up_previous_page
    clean_up_previous_page()
    clean_up_previous_page = clean_up
    # make sure there is no music
    musicbox.theme = TotoroMusicTheme.NONE
    
    # background color
    c.create_rectangle(5,5,400,400,fill="#DE8338")
    # draw text
    c.create_text(200,50,text="Let's Help Totoro",font=("Helvetica",36), fill="white")
    c.create_text(200,200,text="""
We will use search algorithms to find the
best path to Japan.
""", justify=CENTER, fill="white")
    c.bind("<Button>",page14)  # binds mouse click to draw first scene
    
###########################################################################
#  Page 14 -- World Map                                                   #
#                                                                         #
#  Can we help Totoro find home? Choose the best path-finding algorithm   #
#  to help Totoro find home.                                              #
###########################################################################
def page14(event=None, searchAlgorithm=None):
    if searchAlgorithm:
        # set search algorithm
        navigator.searchAlgorithm = searchAlgorithm
        
    # this will be called when changing to the next page
    def clean_up():
        c.delete(ALL)
        startOption.destroy()
        algoOption.destroy()
        Animation.stop()
    global clean_up_previous_page
    clean_up_previous_page()
    clean_up_previous_page = clean_up

    # play different music for last algorithm
    if searchAlgorithm == SearchAlgorithm.A_STAR:
        musicbox.theme = TotoroMusicTheme.TOTORO
    else:
        musicbox.theme = TotoroMusicTheme.THE_PATH_OF_THE_WIND
    
    c.bind("<Button>",creditsPage)
    
    world_map(c, tag="world_map")
    navigator.drawNetwork(c, tag="network")
    drawLabel(c, text="Where's {}?".format(navigator.finalState))

    def setStart(value):
        navigator.initialState = value
        page14()

    def setAlgorithm(value):
        for algorithm in SearchAlgorithm:
            if value == str(algorithm):
                navigator.searchAlgorithm = algorithm
                page14()

    startOptions = []
    for key, value in navigator.coordinates.items():
        if key != navigator.finalState:
            startOptions.append(key)
    startVar = StringVar()
    startVar.set(navigator.initialState)
    startOption = OptionMenu(c, startVar, *startOptions, command=setStart)
    startOption.config(bg = "#124B70")
    startOption.place(x=10, y=5)

    algoOptions = []
    for algorithm in SearchAlgorithm:
        algoOptions.append(str(algorithm))
    algoVar = StringVar()
    algoVar.set(str(navigator.searchAlgorithm))
    algoOption = OptionMenu(c, algoVar, *algoOptions, command=setAlgorithm)
    algoOption.config(bg = "#124B70")
    algoOption.place(x=10, y=30)

    # explain algorithms with annotations
    if navigator.searchAlgorithm == SearchAlgorithm.DEPTH_FIRST:
        drawAnnotation(c, text="""
The depth first algorithm picks one direction and sticks to it untill
it meets a dead end. Slowly it works backwards untill it figures out
what went wrong.
""")
    elif navigator.searchAlgorithm == SearchAlgorithm.DEPTH_FIRST_DYNAMIC:
        drawAnnotation(c, text="""
The depth first algorithm with dynamic programming does what the depth
first algorithm does without repeating nodes that have already been
checked. This speeds things up immensely.
""")
    elif navigator.searchAlgorithm == SearchAlgorithm.BREADTH_FIRST:
        drawAnnotation(c, text="""
The breadth first algorithm checks level by level starting by searching
all nodes one node away then two nodes away and keeps going untill the
goal is reached.
""")
    elif navigator.searchAlgorithm == SearchAlgorithm.BREADTH_FIRST_DYNAMIC:
        drawAnnotation(c, text="""
The breadth first algorithm with dynamic programming does what the
breadth first algorithm does without repeating nodes that have already
been checked. This speeds things up immensely.
""")
    elif navigator.searchAlgorithm == SearchAlgorithm.HILL_CLIMBING :
        drawAnnotation(c, text="""
The hill climbing algorithm compares each adjacent node to see which
one is closer to our goal, effectively avoiding searching in the wrong
direction. Unfortunately, sometimes it reaches a local minima and assumes
it can't go further.
""")
    elif navigator.searchAlgorithm == SearchAlgorithm.UNIFORM_COST :
        drawAnnotation(c, text="""
The uniform cost algorithm prioritizes low cost paths.
""")
    elif navigator.searchAlgorithm == SearchAlgorithm.UNIFORM_COST_DYNAMIC :
        drawAnnotation(c, text="""
The uniform cost algorithm prioritizes low cost paths. It will keep track
of states that it already expanded. 
""")
    elif navigator.searchAlgorithm == SearchAlgorithm.A_STAR :
        drawAnnotation(c, text="""
The A* algorithm estimates the total cost of paths prioritizes low cost
paths. In this case the estimate cost is calculated by length of path plus
the remaining distance. A* is guaranteed to find the shortest path.
""")

    # create totoros
    totoro1      = Totoro(c, left=0, top=0, width=150, height=150,
                    bodyColor="#736F5F", 
                    action=Action.STOP, name="Big Totoro",
                    sacredItemType=SacredItemType.UMBRELLA)

    def completion():
        frame_count = 1000
        def setup(): 
            totoro1.sacredItem.type = SacredItemType.CAMPHORLEAF
            totoro1.setAction(Action.STOP)
            totoro1.position(*navigator.coordinates[navigator.initialState])
            totoro1.resize(20,20)
            totoro1.redraw()
        def timeline(t):
            totoro1.stepRatio = 0.1
            c.tag_raise("annotation")# bring to front
            if t == 0:
                totoro1.path = pathBackHome
        def completion():
            drawAnnotation(c, text="Click when done")

        totoroCoordinator = TotoroCoordinator(c, [totoro1])
        totoroCoordinator.reset = setup
        totoroCoordinator.timeline = timeline
        totoroCoordinator.completion = completion
        totoroCoordinator.frame_count = frame_count
        totoroCoordinator.play()

    searchResult = navigator.search()
    pathBackHome = navigator.coordinatesFromPath(searchResult.path)
    navigator.animateSearchLog(c, searchResult.log, completion, 200)

    
###########################################################################
#  Main Program                                                           #
#                                                                         #
#  Sets up the canvas to contain the story and displays the title page.   #
###########################################################################

c = Canvas(width=400, height=400, bg='white')
c.pack(expand=YES, fill=BOTH)

# set up objects
navigator = Navigator()
musicbox = TotoroMusicBox()

# show title page first
titlepage()

# bind keys
c.bind("<Key>",default)  # bind default keyboard
c.bind("1",page1)
c.bind("2",page2)
c.bind("3",page3)
c.bind("4",page4)
c.bind("5",page5)
c.bind("6",page6)
c.bind("7",page7)
c.bind("8",page8)
c.bind("9",page9)
c.bind("0",page10)
c.bind("q",page11)
c.bind("w",page12)
c.bind("e",page13)
c.bind("r",lambda event: page14(event,SearchAlgorithm.DEPTH_FIRST))
c.bind("t",lambda event: page14(event,SearchAlgorithm.DEPTH_FIRST_DYNAMIC))
c.bind("y",lambda event: page14(event,SearchAlgorithm.BREADTH_FIRST))
c.bind("u",lambda event: page14(event,SearchAlgorithm.BREADTH_FIRST_DYNAMIC))
c.bind("i",lambda event: page14(event,SearchAlgorithm.HILL_CLIMBING))
c.bind("o",lambda event: page14(event,SearchAlgorithm.UNIFORM_COST))
c.bind("p",lambda event: page14(event,SearchAlgorithm.UNIFORM_COST_DYNAMIC))
c.bind("a",lambda event: page14(event,SearchAlgorithm.A_STAR))
c.bind("s",creditsPage)
c.bind("x",titlepage)
