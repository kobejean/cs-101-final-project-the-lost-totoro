###########################################################################
#              Assignment 6 -- Multiple Pose Parameters                   #
#                               Totoro                                    #
#                                                                         #
#  Programmed by Jean Flaherty (10-29-2016)                               #
#  Instructor:  Dean Zeller                                               #
#                                                                         #
#  Description:  The file contains a totoro bot object with multiple      #
#                pose parameters and methods for animation.               #
#                                                                         #
#  Objects:                                                               #
#        SacredItemType -- Enumerated data type for 3 SacredItemTypes     #
#        SacredItem -- Representation of a Sacred Item                    #
#        Action -- Enumerated data type for 5 different actions           #
#        Totoro -- An animatable totoro bot                               #
#        TotoroCoordinator -- An object that handels animating the Totoro #
#                                                                         #
#  EXTERNAL FILES                                                         #
#  The following external files are used for the Totoro bot.              #
#                                                                         #
#       FlahertyJeanAnimation, by Jean Flaherty                           #
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

from tkinter import *
from FlahertyJeanAnimation import Animation
import math

###########################################################################
#                           SacredItemType                                #
#                                                                         #
#   Description:  This class defines three different sacred item types,   #
#   for use in the SacredItem class.  The types include: CAMPHORLEAF,     #
#   KUDZULEAF, and UMBRELLA.                                              #
#                                                                         #
###########################################################################

class SacredItemType:  #enumerated data type
    CAMPHORLEAF=0  # KUSUNOKINOHAPPA 
    KUDZULEAF=1    # KUZUNOHAPPA
    UMBRELLA=2     # KASA

###########################################################################
#                                  SacredItem                             #
#                                                                         #
#   Description:  This uses the tkinter graphics library to create a      #
#                 sacred item representation, based on the user's         #
#                 parameters and instructions.                            #
#                                                                         #
#   Parameters:                                                           #
#           canvas         Canvas to draw the picture                     #
#           left, top      Left and top of the entire picture             #
#           width, height  Width and height of the entire picture         #
#           type           Type of sacred item                            #
#                                                                         #
###########################################################################
class SacredItem:

    # class attributes
    objectName = "FlahertyJeanBotSacredItem"  # Title for this item
    objectNum = 0                         # Number of instances created

    #######################################################################
    #  __init__ constructor                                               #
    #                                                                     #
    #  Initializes all attributes to given parameters.                    #
    #######################################################################
    def __init__ (self, canvas, left=0,top=0,width=100,height=100,
                  type=SacredItemType.CAMPHORLEAF):
        
        # attributes directly from parameters
        self.c = canvas
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.type = type

        # calculated attributes
        self.tag = SacredItem.objectName + str(SacredItem.objectNum)
        SacredItem.objectNum += 1
        self.right = self.left + self.width
        self.bottom = self.top + self.height
        self.center = (self.left + self.right) / 2.0
        self.middle = (self.top + self.bottom) / 2.0

    #######################################################################
    #  draw method                                                        #
    #                                                                     #
    #  Draws the item according to the attributes, including size,        #
    #  and position. Does not update canvas for you.                      #
    #######################################################################
    def draw(self):

        # create X-coordinate guide list
        xspaces = 20  # number of guides in the guide list
        xgridwidth = 1.0 * self.width / xspaces
        x = []
        for i in range(xspaces+1):
            x.append(self.left + i*xgridwidth)

        # create Y-coordinate guide list
        yspaces = 20  # number of guides in the guide list
        ygridwidth = 1.0 * self.height / yspaces
        y = []
        for i in range(yspaces+1):
            y.append(self.top + i*ygridwidth)

        ###################################################################
        #                          Drawing                                #
        ###################################################################           

        if self.type == SacredItemType.CAMPHORLEAF:
            # CAMPHORLEAF Coordinates
            Stem = (  (x[10],y[ 6]) , (x[10],y[20])  )
            Leaf = (  (x[ 7],y[ 4]) , (x[13],y[ 6])  )
            # Drawing
            self.c.create_arc(Leaf, start=150, extent=240,
                              fill="#3AD22A", tag=self.tag, outline="black",
                              width=1)
            self.c.create_line(Stem, tag=self.tag, fill="black", width=1)
            
        elif self.type == SacredItemType.KUDZULEAF:
            # KUDZULEAF Coordinates
            Stem = (  (x[10],y[ 3]) , (x[10],y[20])  )
            Leaf = (  (x[ 4],y[ 1]) , (x[16],y[ 4])  )
            # Drawing
            self.c.create_arc(Leaf, start=95, extent=350,
                              fill="#3AAD2A", tag=self.tag, outline="black",
                              width=1)
            self.c.create_line(Stem, tag=self.tag, fill="black", width=1)
            
        elif self.type == SacredItemType.UMBRELLA:
            # UMBRELLA Coordinates
            Canopy    = (   (x[10],y[ 0]) , (x[16],y[ 1]) , (x[20],y[ 5]) ,
                            (x[16],y[ 6]) , (x[ 4],y[ 6]) , (x[ 0],y[ 5]) ,
                            (x[ 4],y[ 1])   )
            FrontEdge = (   (x[ 0],y[ 5]) , (x[ 5],y[ 4]) , (x[15],y[ 4]) ,
                            (x[20],y[ 5])   )
            Rib1      = (   (x[10],y[ 0]) , (x[ 7],y[ 1]) , (x[ 5],y[ 4])   )
            Rib2      = (   (x[10],y[ 0]) , (x[13],y[ 1]) , (x[15],y[ 4])   )
            Shaft     = (   (x[10],y[ 4]) , (x[10],y[17])   )
            Handle    = (   (x[10],y[17]) , (x[10],y[19]) , (x[ 9],y[20]) ,
                            (x[ 8],y[20]) , (x[ 7],y[19]) , (x[ 7],y[18])   )
            # Drawing
            self.c.create_polygon(Canopy, tag=self.tag, fill="#3C3849",
                                  outline="black", width=1)
            self.c.create_line(FrontEdge, tag=self.tag, fill="black", width=1)
            self.c.create_line(Rib1, tag=self.tag, fill="black", width=1)
            self.c.create_line(Rib2, tag=self.tag, fill="black", width=1)
            self.c.create_line(Shaft, tag=self.tag, fill="black", width=2)
            self.c.create_line(Handle, tag=self.tag, fill="#152022", width=3)

    #######################################################################
    #  setPositionAndSize method                                          #                                                       #
    #                                                                     #
    #  positions item. x,y are cordinates based on where center,bottom    #
    #  should be. Does not update canvas for you.                         #
    #######################################################################

    def setPositionAndSize(self, x, y, width, height):
        self.bottom = y
        self.center = x
        
        self.left = self.center - width / 2.0
        self.top = self.bottom - height
        self.right = self.center + width / 2.0
        self.middle = self.bottom - height / 2.0
        self.width = width
        self.height = height
        self.delete()
        self.draw()
        
    #######################################################################
    #  delete method                                                      #
    #                                                                     #
    #  Deletes the bot from the canvas.  Note that the object still       #
    #  still exists after it is deleted; it is just not displayed.        #
    #  Does not update canvas for you.                                    # 
    #######################################################################
    def delete(self):
        self.c.delete(self.tag)
        


###########################################################################
#                           Action                                        #
#                                                                         #
#   Description:  This class defines five different actions, for use      #
#                 in the Totoro class.  The actions include:              #
#                 STOP, FUNNYFACE, WORSHIPING, LEFTWALKING, RIGHTWALKING. #                               #
#                                                                         #
###########################################################################

class Action:  #enumerated data type
    STOP=0
    FUNNYFACE=1
    WORSHIPING=2      #worshiping animation
    LEFTWALKING=3
    RIGHTWALKING=4

###########################################################################
#                           Totoro Coordinator                            #
#                                                                         #
#   Description:  This object makes animating the totoro easier. It is a  #
#                 subclass of the Animation object and will call          #
#                 totoro.nextFrame() for you so you only have to issue    #
#                 commands to the totoro.                                 #
#                                                                         #
#   Parameters:                                                           #
#           canvas         Canvas to draw the picture                     #
#           totoros        A list of totoros involved in the animation    #
#           fpms           Frames per milisec for animation               #
#           frame_count    The number of frames for the animation         #
#           reset          A function that resets animation positions     #
#           timeline       A function that has commands for different     #
#                          iterations of the animation loop.              #
#           completion     A function called when the animation is done   # 
#                                                                         #
###########################################################################

class TotoroCoordinator(Animation):

    
    #######################################################################
    # Timeline: define a setter and getter for timeline                   #
    # - getter will simply return the value.                              #
    # - setter adds totoro.nextFrame() for every assigned totoro to the   #
    #   timeline.                                                         #
    #######################################################################
    @property
    def timeline(self):
        return self._timeline
    
    @timeline.setter
    def timeline(self, timeline):
        # this timeline will help animate assigned totoros in parallel
        # and embed the user assigned timeline code for each frame
        def internal_timeline(frame_number):
            # call nextFrame() for all totoros
            for totoro in self.totoros:
                totoro.nextFrame()
            # call the user defined timeline if specified
            if timeline : timeline(frame_number)
            
        self._timeline = internal_timeline

    #######################################################################
    # Initialize                                                                    #
    #######################################################################
    def __init__(self, canvas, totoros=[], fpms=1000/30, frame_count=0, reset=None, timeline=None, completion=None):
            
        Animation.__init__(self, canvas, fpms, frame_count)
        self.reset = reset
        # use our setter to handle embeding timeline in animation engine
        self.timeline = timeline
        self.completion = completion
        self.totoros = totoros

###########################################################################
#                                  Totoro                                 #
#                                                                         #
#   Description:  This uses the tkinter graphics library to create a      #
#                 totoro bot, based on the user's parameters and          #
#                 instructions.                                           #
#                                                                         #
#   Parameters:                                                           #
#           canvas         Canvas to draw the picture                     #
#           left, top      Left and top of the entire picture             #
#           width, height  Width and height of the entire picture         #
#           bodyColor      Color of the body                              #
#           eyeColor       Color of the eyes                              #
#           pupilColor     Color of the pupils                            #
#           name           Name of the face                               #
#           displayName    Boolean to display the character name          #
#                              0 -> does not display name                 #
#                              1 -> displays name                         #
#           action         Type of action that is currently performed     #
#           time           Used to determine stage of action              #
#           sacredItemType Type of sacred item: CAMPHORLEAF, UMBRELLA ect.#
#                                                                         #
###########################################################################

class Totoro:

    # class attributes
    objectName = "FlahertyJeanBotTotoro"  # Title for this bot
    objectNum = 0                         # Number of instances created

    #######################################################################
    #  __init__ constructor                                               #
    #                                                                     #
    #  Initializes all attributes to given parameters.                    #
    #######################################################################
    def __init__ (self, canvas, left=0,top=0,width=100,height=100,
                  bodyColor="white", eyeColor="white", pupilColor="black",
                  name="blank", displayName=0, action=Action.STOP,
                  time=0, sacredItemType=SacredItemType.CAMPHORLEAF):



        # attributes directly from parameters
        self.c = canvas
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.bodyColor = bodyColor
        self.eyeColor = eyeColor
        self.pupilColor = pupilColor
        self.name = name
        self.displayName = displayName
        # pose parameters
        self.action = action
        self.time = time
        self.sacredItem = SacredItem(canvas, type=sacredItemType)

        # calculated attributes
        self.tag = Totoro.objectName + str(Totoro.objectNum)
        Totoro.objectNum += 1
        self.right = self.left + self.width
        self.bottom = self.top + self.height
        self.center = (self.left + self.right) / 2.0
        self.middle = (self.top + self.bottom) / 2.0

        self.path = []
        
        # step ratio is 1/10th of totoro width by default
        self.stepRatio = 0.1


    #######################################################################
    #  draw method                                                        #
    #                                                                     #
    #  Draws the bot according to the attributes, including size,         #
    #  position, and colors portrayed.                                    #
    #######################################################################
    def draw(self):

        # create X-coordinate guide list
        xspaces = 40  # number of guides in the guide list
        xgridwidth = 1.0 * self.width / xspaces
        x = []
        for i in range(xspaces+1):
            x.append(self.left + i*xgridwidth)

        # create Y-coordinate guide list
        yspaces = 40  # number of guides in the guide list
        ygridwidth = 1.0 * self.height / yspaces
        y = []
        for i in range(yspaces+1):
            y.append(self.top + i*ygridwidth)


        ###################################################################
        #                          Coordinates                            #
        ###################################################################

        #start with blank coordinates
        eye1  = ( (0,0), (0,0) )
        eye2  = ( (0,0), (0,0) )
        pupil1 = ( (0,0), (0,0) )
        pupil2 = ( (0,0), (0,0) )
        hand1 = ( (0,0), (0,0) )
        hand2 = ( (0,0), (0,0) )
        foot1 = ( (0,0), (0,0) )
        foot2 = ( (0,0), (0,0) )
        ear1 = ( (0,0), (0,0) )
        ear2 = ( (0,0), (0,0) )
        #default coordinates
        sacredItemPositionAndSize = (   x[10],y[30], self.width,self.height   )

        if self.action == Action.STOP:
            # STOP neutral pose
            body  = (  (x[20],y[12]) , (x[26],y[ 0]) , (x[26],y[ 0]) ,
                       (x[28],y[12]) , (x[28],y[12]) , (x[34],y[30]) ,
                       (x[30],y[38]) , (x[26],y[40]) , (x[14],y[40]) ,
                       (x[10],y[38]) , (x[ 6],y[30]) , (x[12],y[12]) ,
                       (x[12],y[12]) , (x[14],y[ 0]) , (x[14],y[ 0]) ,
                       (x[20],y[12]) , (x[20],y[12])  )
            eye1  = (  (x[12],y[18]) , (x[18],y[24])  )
            eye2  = (  (x[22],y[18]) , (x[28],y[24])  )
            pupil1 =(  (x[14],y[20]) , (x[16],y[22])  )
            pupil2 =(  (x[24],y[20]) , (x[26],y[22])  )
            
        elif self.action == Action.FUNNYFACE:
            # EXCITED eyes are crossed
            body  = (  (x[20],y[12]) , (x[26],y[ 0]) , (x[26],y[ 0]) ,
                       (x[28],y[12]) , (x[28],y[12]) , (x[34],y[30]) ,
                       (x[30],y[38]) , (x[26],y[40]) , (x[14],y[40]) ,
                       (x[10],y[38]) , (x[ 6],y[30]) , (x[12],y[12]) ,
                       (x[12],y[12]) , (x[14],y[ 0]) , (x[14],y[ 0]) ,
                       (x[20],y[12]) , (x[20],y[12])  )
            eye1  = (  (x[12],y[18]) , (x[18],y[24])  )
            eye2  = (  (x[22],y[18]) , (x[28],y[24])  )
            pupil1 =(  (x[16],y[20]) , (x[18],y[22])  )
            pupil2 =(  (x[22],y[20]) , (x[24],y[22])  )
        elif self.action == Action.WORSHIPING:
            # stage skips every other frame and repeats over 12 frames
            # we number stages 0-5
            stage = math.floor(self.time/2) % 6
            if stage == 1 or stage == 2 : # same for stage 1&2
                # WORSHIP1 worship animation pose stage 1
                body  = (  (x[20],y[22]) , (x[24],y[16]) , (x[24],y[16]) ,
                           (x[28],y[22]) , (x[28],y[22]) , (x[34],y[32]) ,
                           (x[32],y[38]) , (x[28],y[40]) , (x[12],y[40]) ,
                           (x[ 8],y[38]) , (x[ 6],y[32]) , (x[12],y[22]) ,
                           (x[12],y[22]) , (x[16],y[16]) , (x[16],y[16]) ,
                           (x[20],y[22]) , (x[20],y[22])  )
                eye1  = (  (x[12],y[24]) , (x[18],y[28])  )
                eye2  = (  (x[22],y[24]) , (x[28],y[28])  )
                pupil1 =(  (x[14],y[24]) , (x[16],y[26])  )
                pupil2 =(  (x[24],y[24]) , (x[26],y[26])  )
                hand1 = (  (x[ 8],y[28]) , (x[20],y[34]) , (x[12],y[32])  )
                hand2 = (  (x[32],y[28]) , (x[20],y[34]) , (x[28],y[32])  )
                sacredItemPositionAndSize = (   x[20] ,y[34], self.width,self.height  )

            elif stage == 0 or stage == 3: # same for stage 0&3
                # WORSHIP2 worship animation pose stage 2
                body  = (  (x[20],y[20]) , (x[24],y[12]) , (x[24],y[12]) ,
                           (x[28],y[20]) , (x[28],y[20]) , (x[34],y[32]) ,
                           (x[32],y[38]) , (x[28],y[40]) , (x[12],y[40]) ,
                           (x[ 8],y[38]) , (x[ 6],y[32]) , (x[12],y[20]) ,
                           (x[12],y[20]) , (x[16],y[12]) , (x[16],y[12]) ,
                           (x[20],y[20]) , (x[20],y[20])  )
                eye1  = (  (x[12],y[22]) , (x[18],y[26])  )
                eye2  = (  (x[22],y[22]) , (x[28],y[26])  )
                pupil1 =(  (x[14],y[22]) , (x[16],y[24])  )
                pupil2 =(  (x[24],y[22]) , (x[26],y[24])  )
                hand1 = (  (x[ 8],y[28]) , (x[20],y[32]) , (x[12],y[32])  )
                hand2 = (  (x[32],y[28]) , (x[20],y[32]) , (x[28],y[32])  )
                sacredItemPositionAndSize = (   x[20] ,y[32], self.width,self.height)

            elif stage == 4:
                # WORSHIP3 worship animation pose stage 3
                body  = (  (x[20],y[16]) , (x[24],y[ 6]) , (x[24],y[ 6]) ,
                           (x[28],y[16]) , (x[28],y[16]) , (x[34],y[30]) ,
                           (x[30],y[38]) , (x[26],y[40]) , (x[14],y[40]) ,
                           (x[10],y[38]) , (x[ 6],y[30]) , (x[12],y[16]) ,
                           (x[12],y[16]) , (x[16],y[ 6]) , (x[16],y[ 6]) ,
                           (x[20],y[16]) , (x[20],y[16])  )
                eye1  = (  (x[12],y[18]) , (x[18],y[22])  )
                eye2  = (  (x[22],y[18]) , (x[28],y[22])  )
                pupil1 =(  (x[14],y[18]) , (x[16],y[20])  )
                pupil2 =(  (x[24],y[18]) , (x[26],y[20])  )
                hand1 = (  (x[ 8],y[26]) , (x[20],y[24]) , (x[14],y[28])  )
                hand2 = (  (x[32],y[26]) , (x[20],y[24]) , (x[26],y[28])  )
                sacredItemPositionAndSize = (   x[20] ,y[24], self.width,self.height)

            elif stage == 5:
                # WORSHIP4 worship animation pose stage 4
                body  = (  (x[20],y[12]) , (x[24],y[ 0]) , (x[24],y[ 0]) ,
                           (x[28],y[12]) , (x[28],y[12]) , (x[32],y[28]) ,
                           (x[30],y[36]) , (x[26],y[40]) , (x[14],y[40]) ,
                           (x[10],y[36]) , (x[ 8],y[28]) , (x[12],y[12]) ,
                           (x[12],y[12]) , (x[16],y[ 0]) , (x[16],y[ 0]) ,
                           (x[20],y[12]) , (x[20],y[12])  )
                eye1  = (  (x[12],y[14]) , (x[18],y[20])  )
                eye2  = (  (x[22],y[14]) , (x[28],y[20])  )
                pupil1 =(  (x[14],y[14]) , (x[16],y[16])  )
                pupil2 =(  (x[24],y[14]) , (x[26],y[16])  )
                hand1 = (  (x[10],y[24]) , (x[20],y[14]) , (x[16],y[26])  )
                hand2 = (  (x[30],y[24]) , (x[20],y[14]) , (x[24],y[26])  )
                sacredItemPositionAndSize = (   x[20] ,y[14], self.width,self.height)

        elif self.action == Action.LEFTWALKING:
            # stage is a number that repeats like 0,1,2,3,4,5,0,1,2,3,4,5...
            stage = self.time % 6
            # default position for walking
            sacredItemPositionAndSize = (   x[12],y[30], self.width,self.height   )
            if stage == 0:
                # LWALKING1 walking left animation stage 1
                body  = (  (x[17],y[13]) , (x[19],y[12]) , (x[22],y[12]) ,
                           (x[25],y[14]) , (x[27],y[19]) , (x[29],y[31]) ,
                           (x[28],y[35]) , (x[25],y[37]) , (x[11],y[35]) ,
                           (x[ 9],y[32]) , (x[ 9],y[28]) , (x[14],y[16])  )
                eye1  = (  (x[15],y[16]) , (x[18],y[22])  )
                pupil1 =(  (x[15],y[18]) , (x[16],y[20])  )
                foot1 = (  (x[ 6],y[33]) , (x[ 8],y[33]) , (x[12],y[36]) ,
                           (x[11],y[37]) , (x[ 8],y[35])  )
                foot2 = (  (x[24],y[39]) , (x[25],y[38]) , (x[28],y[37]) ,
                           (x[29],y[38]) , (x[26],y[39])  )
                ear1 =  (  (x[19],y[12]) , (x[21],y[ 6]) , (x[22],y[ 5]) ,
                           (x[21],y[12])  )
                ear2 =  (  (x[22],y[12]) , (x[25],y[ 6]),  (x[26],y[ 5]) ,
                           (x[25],y[14])  )
                # only this frame will change sacred item position
                sacredItemPositionAndSize = (   x[12],y[29], self.width,self.height   )
            elif stage == 1:
                # LWALKING2 walking left animation stage 2
                body  = (  (x[16],y[13]) , (x[18],y[12]) , (x[21],y[12]) ,
                           (x[24],y[14]) , (x[26],y[17]) , (x[29],y[31]) ,
                           (x[28],y[35]) , (x[25],y[37]) , (x[10],y[34]) ,
                           (x[ 9],y[31]) , (x[ 9],y[27]) , (x[13],y[17])  )
                eye1  = (  (x[15],y[16]) , (x[18],y[22])  )
                pupil1 =(  (x[15],y[18]) , (x[16],y[20])  )
                foot1 = (  (x[ 7],y[30]) , (x[ 8],y[31]) , (x[ 9],y[34]) ,
                           (x[ 8],y[35]) , (x[ 7],y[32])  )
                foot2 = (  (x[24],y[39]) , (x[26],y[38]) , (x[28],y[36]) ,
                           (x[29],y[37]) , (x[27],y[39])  )
                ear1 =  (  (x[18],y[12]) , (x[21],y[ 6]) , (x[22],y[ 5]) ,
                           (x[21],y[12])  )
                ear2 =  (  (x[21],y[12]) ,  (x[25],y[6]) , (x[26],y[ 5]) ,
                           (x[24],y[14])  )
            elif stage == 2:
                #LWALKING3 walking left animation stage 3
                body  = (  (x[16],y[14]) , (x[18],y[13]) , (x[21],y[13]) ,
                           (x[24],y[14]) , (x[27],y[19]) , (x[29],y[32]) ,
                           (x[28],y[35]) , (x[25],y[36]) , (x[12],y[36]) ,
                           (x[ 9],y[34]) , (x[ 9],y[28]) , (x[14],y[16])  )
                eye1  = (  (x[14],y[16]) , (x[17],y[22])  )
                pupil1 =(  (x[14],y[18]) , (x[15],y[20])  )
                foot1 = (  (x[ 6],y[35]) , (x[ 8],y[35]) , (x[12],y[37]) ,
                           (x[12],y[38]) , (x[ 8],y[37]) )
                foot2 = (  (x[27],y[38]) , (x[28],y[37]) , (x[28],y[34]) ,
                           (x[30],y[34]) , (x[29],y[38]) )
                ear1 =  (  (x[18],y[13]) , (x[21],y[ 7]) , (x[22],y[ 6]) ,
                           (x[21],y[13])  )
                ear2 =  (  (x[21],y[13]) ,  (x[24],y[ 8]), (x[26],y[ 6]) ,
                           (x[24],y[14])  )
            elif stage == 3:
                #LWALKING4 walking left animation stage 4
                body  = (  (x[16],y[14]) , (x[18],y[13]) , (x[21],y[13]) ,
                           (x[24],y[14]) , (x[27],y[19]) , (x[29],y[32]) ,
                           (x[28],y[35]) , (x[25],y[36]) , (x[12],y[36]) ,
                           (x[ 9],y[34]) , (x[ 9],y[28]) , (x[14],y[16])  )
                eye1  = (  (x[14],y[16]) , (x[17],y[22])  )
                pupil1 =(  (x[14],y[18]) , (x[15],y[20])  )
                foot1 = (  (x[10],y[38]) , (x[12],y[37]) , (x[16],y[37]) ,
                           (x[16],y[38]) , (x[12],y[38])  )
                foot2 = (  (x[27],y[36]) , (x[28],y[36]) , (x[29],y[37]) ,
                           (x[28],y[38]) , (x[27],y[37])  )
                ear1 =  (  (x[18],y[13]) , (x[21],y[ 7]) , (x[22],y[ 6]) ,
                           (x[21],y[13])  )
                ear2 =  (  (x[21],y[13]) , (x[24],y[ 8]) , (x[26],y[ 6]) ,
                           (x[24],y[14])  )
            elif stage == 4:
                #LWALKING5 walking left animation stage 5
                body  = (  (x[16],y[14]) , (x[18],y[13]) , (x[21],y[13]) ,
                           (x[24],y[14]) , (x[27],y[19]) , (x[29],y[32]) ,
                           (x[28],y[35]) , (x[25],y[36]) , (x[12],y[36]) ,
                           (x[ 9],y[34]) , (x[ 9],y[28]) , (x[14],y[16])  )
                eye1  = (  (x[14],y[16]) , (x[17],y[22])  )
                pupil1 =(  (x[14],y[18]) , (x[15],y[20])  )
                foot1 = (  (x[15],y[38]) , (x[17],y[37]) , (x[21],y[37]) ,
                           (x[21],y[38]) , (x[17],y[38])  )
                foot2 = (  (x[15],y[38]) , (x[17],y[37]) , (x[21],y[37]) ,
                           (x[21],y[38]) , (x[17],y[38])  )
                ear1 =  (  (x[18],y[13]) , (x[20],y[ 7]) , (x[21],y[ 6]) ,
                           (x[21],y[13])  )
                ear2 =  (  (x[21],y[13]) , (x[23],y[ 8]) , (x[26],y[ 5]) ,
                           (x[24],y[14])  )
            elif stage == 5:
                #LWALKING6 walking left animation stage 6
                body  = (  (x[16],y[14]) , (x[18],y[13]) , (x[21],y[13]) ,
                           (x[25],y[15]) , (x[27],y[19]) , (x[29],y[32]) ,
                           (x[28],y[35]) , (x[25],y[37]) , (x[12],y[36]) ,
                           (x[10],y[34]) , (x[ 9],y[30]) , (x[14],y[16])  )
                eye1  = (  (x[14],y[16]) , (x[17],y[22])  )
                pupil1 =(  (x[14],y[18]) , (x[15],y[20])  )
                foot1 = (  (x[13],y[37]) , (x[14],y[36]) , (x[18],y[37]) ,
                           (x[17],y[38]) , (x[15],y[38])  )
                foot2 = (  (x[21],y[38]) , (x[23],y[37]) , (x[26],y[37]) ,
                           (x[26],y[39]) , (x[22],y[39])  )
                ear1 =  (  (x[18],y[13]) , (x[21],y[ 7]) , (x[22],y[ 6]) ,
                           (x[21],y[13]) )
                ear2 =  (  (x[21],y[13]) , (x[24],y[ 8]) , (x[27],y[ 5]) ,
                           (x[25],y[15]) )
        elif self.action == Action.RIGHTWALKING:
            # stage is a number that repeats like 0,1,2,3,4,5,0,1,2,3,4,5...
            stage = self.time % 6
            # default position for walking
            sacredItemPositionAndSize = (   x[28],y[30], self.width,self.height   )
            if stage == 0 :
                #RWALKING1 walking right animation stage 1
                body  = (  (x[23],y[13]) , (x[21],y[12]) , (x[18],y[12]) ,
                           (x[15],y[14]) , (x[13],y[19]) , (x[11],y[31]) ,
                           (x[12],y[35]) , (x[15],y[37]) , (x[29],y[35]) ,
                           (x[31],y[32]) , (x[31],y[28]) , (x[26],y[16])  )
                eye1  = (  (x[25],y[16]) , (x[22],y[22])  )
                pupil1 =(  (x[25],y[18]) , (x[24],y[20])  )
                foot1 = (  (x[34],y[33]) , (x[32],y[33]) , (x[28],y[36]) ,
                           (x[29],y[37]) , (x[32],y[35])  )
                foot2 = (  (x[16],y[39]) , (x[15],y[38]) , (x[12],y[37]) ,
                           (x[11],y[38]) , (x[14],y[39])  )
                ear1 =  (  (x[21],y[12]) , (x[19],y[ 6]),  (x[18],y[ 5]) ,
                           (x[19],y[12])  )
                ear2 =  (  (x[18],y[12]) , (x[15],y[ 6]),  (x[14],y[ 5]) ,
                           (x[15],y[14])  )
                # only this frame will change sacred item position
                sacredItemPositionAndSize = (   x[28],y[29], self.width,self.height   )
            elif stage == 1 :
                #RWALKING2 walking right animation stage 2
                body  = (  (x[24],y[13]) , (x[22],y[12]) , (x[19],y[12]) ,
                           (x[16],y[14]) , (x[14],y[17]) , (x[11],y[31]) ,
                           (x[12],y[35]) , (x[15],y[37]) , (x[30],y[34]) ,
                           (x[31],y[31]) , (x[31],y[27]) , (x[27],y[17])  )
                eye1  = (  (x[25],y[16]) , (x[22],y[22])  )
                pupil1 =(  (x[25],y[18]) , (x[24],y[20])  )
                foot1 = (  (x[33],y[30]) , (x[32],y[31]) , (x[31],y[34]) ,
                           (x[32],y[35]) , (x[33],y[32])  )
                foot2 = (  (x[16],y[39]) , (x[14],y[38]) , (x[12],y[36]) ,
                           (x[11],y[37]) , (x[13],y[39])  )
                ear1 =  (  (x[22],y[12]) , (x[19],y[ 6]) , (x[18],y[ 5]) ,
                           (x[19],y[12])  )
                ear2 =  (  (x[19],y[12]) , (x[15],y[ 6]) , (x[14],y[ 5]) ,
                           (x[16],y[14])  )
            elif stage == 2 :
                #RWALKING3 walking right animation stage 3
                body  = (  (x[24],y[14]) , (x[22],y[13]) , (x[19],y[13]) ,
                           (x[16],y[14]) , (x[13],y[19]) , (x[11],y[32]) ,
                           (x[12],y[35]) , (x[15],y[36]) , (x[28],y[36]) ,
                           (x[31],y[34]) , (x[31],y[28]) , (x[26],y[16])  )
                eye1  = (  (x[26],y[16]) , (x[23],y[22])  )
                pupil1 =(  (x[26],y[18]) , (x[25],y[20])  )
                foot1 = (  (x[34],y[35]) , (x[32],y[35]) , (x[28],y[37]) ,
                           (x[28],y[38]) , (x[32],y[37])  )
                foot2 = (  (x[13],y[38]) , (x[12],y[37]) , (x[12],y[34]) ,
                           (x[10],y[34]) , (x[11],y[38])  )
                ear1 =  (  (x[22],y[13]) , (x[19],y[ 7]) , (x[18],y[ 6]) ,
                           (x[19],y[13])  )
                ear2 =  (  (x[19],y[13]) , (x[16],y[ 8]) , (x[14],y[ 6]),
                           (x[16],y[14])  )
            elif stage == 3 :
                #RWALKING4 walking right animation stage 4
                body  = (  (x[24],y[14]) , (x[22],y[13]) , (x[19],y[13]) ,
                           (x[16],y[14]) , (x[13],y[19]) , (x[11],y[32]) ,
                           (x[12],y[35]) , (x[15],y[36]) , (x[28],y[36]) ,
                           (x[31],y[34]) , (x[31],y[28]) , (x[26],y[16])  )
                eye1  = (  (x[26],y[16]) , (x[23],y[22])  )
                pupil1 =(  (x[26],y[18]) , (x[25],y[20])  )
                foot1 = (  (x[30],y[38]) , (x[28],y[37]) , (x[24],y[37]) ,
                           (x[24],y[38]) , (x[28],y[38])  )
                foot2 = (  (x[13],y[36]) , (x[12],y[36]) , (x[11],y[37]) ,
                           (x[12],y[38]) , (x[13],y[37])  )
                ear1 =  (  (x[22],y[13]) , (x[19],y[ 7]) , (x[18],y[ 6]) ,
                           (x[19],y[13])  )
                ear2 =  (  (x[19],y[13]) , (x[16],y[ 8]) , (x[14],y[ 6]) ,
                           (x[16],y[14])  )
            elif stage == 4 :
                #RWALKING5 walking right animation stage 5
                body  = (  (x[24],y[14]) , (x[22],y[13]) , (x[19],y[13]) ,
                           (x[16],y[14]) , (x[13],y[19]) , (x[11],y[32]) ,
                           (x[12],y[35]) , (x[15],y[36]) , (x[28],y[36]) ,
                           (x[31],y[34]) , (x[31],y[28]) , (x[26],y[16])  )
                eye1  = (  (x[26],y[16]) , (x[23],y[22])  )
                pupil1 =(  (x[26],y[18]) , (x[25],y[20])  )
                foot1 = (  (x[25],y[38]) , (x[23],y[37]) , (x[19],y[37]) ,
                           (x[19],y[38]) , (x[23],y[38])  )
                foot2 = (  (x[25],y[38]) , (x[23],y[37]) , (x[19],y[37]) ,
                           (x[19],y[38]) , (x[23],y[38])  )
                ear1 =  (  (x[22],y[13]) , (x[20],y[ 7]) , (x[19],y[ 6]) ,
                           (x[19],y[13])  )
                ear2 =  (  (x[19],y[13]) , (x[17],y[ 8]),  (x[14],y[ 5]) ,
                           (x[16],y[14])  )
            elif stage == 5 :
                #RWALKING6 walking right animation stage 6
                body  = (  (x[24],y[14]) , (x[22],y[13]) , (x[19],y[13]) ,
                           (x[15],y[15]) , (x[13],y[19]) , (x[11],y[32]) ,
                           (x[12],y[35]) , (x[15],y[37]) , (x[28],y[36]) ,
                           (x[30],y[34]) , (x[31],y[30]) , (x[26],y[16])  )
                eye1  = (  (x[26],y[16]) , (x[23],y[22])  )
                pupil1 =(  (x[26],y[18]) , (x[25],y[20])  )
                foot1 = (  (x[27],y[37]) , (x[26],y[36]) , (x[22],y[37]) ,
                           (x[23],y[38]) , (x[25],y[38])  )
                foot2 = (  (x[19],y[38]) , (x[17],y[37]) , (x[14],y[37]) ,
                           (x[14],y[39]) , (x[18],y[39])  )
                ear1 =  (  (x[22],y[13]) , (x[19],y[ 7]) , (x[18],y[ 6]) ,
                           (x[19],y[13])  )
                ear2 =  (  (x[19],y[13]) , (x[16],y[ 8]),  (x[13],y[ 5]) ,
                           (x[15],y[15])  )
        else:  # print warning message, unimplemented emotion
            print ("Error -- unimplemented action")

        ###################################################################
        #                   Drawing                                       #
        ###################################################################

        # calculate boolean values to simplify hiding and showing certain shapes
        isWorshiping =  (   self.action == Action.WORSHIPING   )
        isWalking =     (   self.action == Action.LEFTWALKING or
                            self.action == Action.RIGHTWALKING   )
        # draw body
        self.bodyID = self.c.create_polygon(body, fill=self.bodyColor,
                                            tag=self.tag, outline="black",
                                            width=1, smooth=NO, splinesteps=3)

        # draw eyes (right eye will be hidden when walking. only need 1 eye)
        leftEyeState = "normal"
        rightEyeState = ("hidden" if isWalking else "normal")
        self.leftEyeID = self.c.create_oval(eye1, fill=self.eyeColor,
                                            tag=self.tag, state=leftEyeState)
        self.rightEyeID = self.c.create_oval(eye2, fill=self.eyeColor,
                                            tag=self.tag, state=rightEyeState)

        # draw pupils (right pupil will be hidden when walking. only need 1 eye)
        leftPupilState = "normal"
        rightPupilState = ("hidden" if isWalking else "normal")
        self.leftPupilID = self.c.create_oval(pupil1, fill=self.pupilColor,
                                            tag=self.tag, state=leftPupilState)
        self.rightPupilID = self.c.create_oval(pupil2, fill=self.pupilColor,
                                            tag=self.tag, state=rightPupilState)

        # draw hands (only shown when worshiping)
        # fill and outline are drawn separately to separate end points
        handState = ("normal" if isWorshiping else "hidden")
        self.leftHandFillID = self.c.create_polygon(hand1, fill=self.bodyColor,
                                            tag=self.tag, state=handState)
        self.rightHandFillID = self.c.create_polygon(hand2, fill=self.bodyColor,
                                            tag=self.tag, state=handState)
        self.leftHandLineID = self.c.create_line(hand1, width=1, fill="black",
                                            tag=self.tag, state=handState)
        self.rightHandLineID = self.c.create_line(hand2, width=1, fill="black",
                                            tag=self.tag, state=handState)

        # draw feet (only shown when walking)
        feetState = ("normal" if isWalking else "hidden")
        self.leftFootID = self.c.create_polygon(foot1, fill=self.bodyColor,
                                                tag=self.tag, outline="black",
                                                width=1, smooth=YES, splinesteps=2,
                                                state=feetState)
        self.rightFootID = self.c.create_polygon(foot2, fill=self.bodyColor,
                                                 tag=self.tag, outline="black",
                                                 width=1, smooth=YES, splinesteps=2,
                                                 state=feetState)

        # draw ears (only shown when walking)
        # fill and outline are drawn separately to separate end points
        earState = ("normal" if isWalking else "hidden")
        self.leftEarFillID = self.c.create_polygon(ear1, fill=self.bodyColor,
                                        tag=self.tag, outline=self.bodyColor,
                                        width=1, state=earState)
        self.rightEarFillID = self.c.create_polygon(ear2, fill=self.bodyColor,
                                        tag=self.tag, outline=self.bodyColor,
                                        width=1, state=earState)
        self.leftEarLineID = self.c.create_line(ear1, width=1, fill="black",
                                        tag=self.tag, smooth=NO, splinesteps=2,
                                        state=earState)
        self.rightEarLineID = self.c.create_line(ear2, width=1, fill="black",
                                        tag=self.tag, smooth=NO, splinesteps=2,
                                        state=earState)

        # set frame of our sacred item
        self.sacredItem.setPositionAndSize(*sacredItemPositionAndSize)


        # draw name
        if self.displayName:  # only display if displayName flag is set
            self.c.create_text(self.center, self.bottom, fill="white", anchor=N,
                               text=self.name, tag=self.tag)
        
        
    #######################################################################
    #  move method                                                        #
    #                                                                     #
    #  Moves the bot on the canvas, relative to its current position.     #
    #  Attributes are adjusted accordingly.                               #
    #  Does not update canvas for you.                                    #
    #######################################################################
    def move (self, deltaX=0, deltaY=0):
        # adjust attributes
        self.left += deltaX
        self.top += deltaY
        self.right += deltaX
        self.bottom += deltaY
        self.center += deltaX
        self.middle += deltaY
        # move totoro
        self.c.move(self.tag,deltaX,deltaY)
        self.c.move(self.sacredItem,deltaX,deltaY)


    #######################################################################
    #  position method                                                    #
    #                                                                     #
    #  Moves the bot on the canvas, to an absolute position.              #
    #  Attributes are adjusted accordingly.                               #
    #  Does not update canvas for you.                                    #
    #######################################################################
    def position (self, x=0, y=0):
        # adjust attributes
        self.bottom = y
        self.center = x
        self.left = x - self.width / 2
        self.top = y - self.height
        self.right = x + self.width / 2
        self.middle = y - self.height/2
        
        self.path = [] # reset path
        
        # redraw
        self.redraw()

    #######################################################################
    #  resize method                                                      #                                                       #
    #                                                                     #
    #  Resizes Totoro.                                                    #
    #  Does not update canvas for you.                                    #
    #######################################################################

    def resize(self, width, height):        
        self.left = self.center - width / 2.0
        self.top = self.bottom - height
        self.right = self.center + width / 2.0
        self.middle = self.bottom - height / 2.0
        self.width = width
        self.height = height
        # redraw
        self.redraw()


    #######################################################################
    #  walkTo method                                                      #
    #                                                                     #
    #  Sets the totoro's destination and picks an action animation that   #
    #  matches the direction of movement. This method does not actually   #
    #  perform the animation. The nextFrame() method needs to be called   #
    #  in order to animate it and allows totoros to move in parallel.     #
    #######################################################################
    def walkTo (self, x, y):

        # set destination

        self.path += [(x,y)]
        
        # calculate deltaX and deltaY
        distX = x - self.center
        distY = y - self.bottom
        
        # true if x-axis is dominant direction 
        isHorizontal = abs(distX) >= abs(distY)
        
        # set up walking poses
        if distX < 0.0 and isHorizontal:    # left and horizontal
            self.setAction(Action.LEFTWALKING)
        
        elif distX > 0.0 and isHorizontal:  # right and horizontal
            self.setAction(Action.RIGHTWALKING)
            
        elif distY != 0 :                   # for verticle movement
            self.setAction(Action.WORSHIPING)
            
        else:                               # stop if distX & distY == 0
            self.setAction(Action.STOP)

    #######################################################################
    #  advance method                                                     #
    #                                                                     #
    #  Sets the totoro's destination using relative coordinates to call   #
    #  the destination method.                                            #
    #######################################################################

    def advance(self, deltaX, deltaY):
        destX = self.center + deltaX
        destY = self.bottom + deltaY
        self.walkTo(destX, destY)
            

    #######################################################################
    #  setProperties method                                               #
    #                                                                     #
    #  Changes the parameters of the bot.  If a parameter is not          #
    #  specified, then it remains unchanged.                              #
    #######################################################################
    def setProperties (self, bodyColor="default", eyeColor="default",
                       pupilColor="default"):
        if bodyColor != "default":
            self.bodyColor=bodyColor
            #recolor body, hands, feet and ears
            self.c.itemconfig(self.bodyID, fill=self.bodyColor)
            self.c.itemconfig(self.leftFootID, fill=self.bodyColor)
            self.c.itemconfig(self.rightFootID, fill=self.bodyColor)
            self.c.itemconfig(self.leftHandFillID, fill=self.bodyColor)
            self.c.itemconfig(self.rightHandFillID, fill=self.bodyColor)
            self.c.itemconfig(self.leftEarFillID, fill=self.bodyColor)
            self.c.itemconfig(self.rightEarFillID, fill=self.bodyColor)
        if eyeColor != "default":
            self.eyeColor=eyeColor
            #recolor eyes
            self.c.itemconfig(self.leftEyeID, fill=self.eyeColor)
            self.c.itemconfig(self.rightEyeID, fill=self.eyeColor)
        if pupilColor != "default":
            self.pupilColor=pupilColor
            #recolor pupil
            self.c.itemconfig(self.leftPupilID, fill=self.pupilColor)
            self.c.itemconfig(self.rightPupilID, fill=self.pupilColor)


    #######################################################################
    #  setAction method                                                   #
    #                                                                     #
    #  Changes the action and resets the time parameter.                  #
    #  Does not animate. Use nextFrame() in for loop to animate.          #
    #######################################################################
    def setAction (self, action):
        # set new action & reset time
        self.action = action
        self.time = 0
        
        self.redraw()

    #######################################################################
    #  nextFrame method                                                   #
    #                                                                     #
    #  Advances the time pose parameter as well as move totoro toward     #
    #  its destination if a destination is set. Frame is then redrawn.    #
    #  Does not update canvas for you. Allows parallel animating.         #
    #######################################################################
    def nextFrame (self):
        self.time += 1
        self.stepTowardDest()
        
        self.redraw()


    #######################################################################
    #  stepTowardDest method                                              #                                                  #
    #                                                                     #
    #  Moves the totoro toward its destination if destination is not      #
    #  reached. Does not update canvas for you.                           #
    #######################################################################

    def stepTowardDest(self):
        # calculate distance
        if self.path:
            nextDestX = self.path[0][0]
            nextDestY = self.path[0][1]
            distX = nextDestX - self.center
            distY = nextDestY - self.bottom
            # calculate step length depending on width and step ratio
            stepLength = self.width * self.stepRatio
            # targetDisplacement (direction & magnitude)
            targetDisplacement = complex(distX, distY)
            # targetDistance (only magnitude)
            targetDistance = abs(targetDisplacement)
            # avoid overshooting 
            nextStepLength = min(stepLength, targetDistance)
            # targetDisplacement with magnitude:1
            angle = targetDisplacement / targetDistance if targetDistance != 0 else complex(0,0)
            # multiply by angle to give length a direction
            nextStep = nextStepLength * angle
            # actual moving of the totoro
            self.move(nextStep.real, nextStep.imag)

            # true if x-axis is dominant direction 
            isHorizontal = abs(distX) >= abs(distY)
            if distX < 0.0 and isHorizontal:    # left and horizontal
                self.action = Action.LEFTWALKING
            elif distX > 0.0 and isHorizontal:  # right and horizontal
                self.action = Action.RIGHTWALKING
            elif distY != 0 :                   # for verticle movement
                self.action = Action.WORSHIPING
            #else:                               # stop if distX & distY == 0
                #self.action = Action.STOP
            
            # stop at last step
            if targetDistance <= stepLength:
                self.path.pop(0)
                if not self.path :
                    self.time = 0
                    self.setAction(Action.STOP)
            

    #######################################################################
    #  doEverything method                                                #
    #                                                                     #
    #  cycles through all pose parameters. Will animate on its own.       #
    #  dont use nextFrame() method in this case.                          #
    #######################################################################
    def doEverything(self, delay=100):
        # we will use the name to print pose parameter state
        # we want to set it back to the original state later so store values
        savedName = self.name
        savedDisplayName = self.displayName
        # display name
        self.displayName = 1
        # loop through sacred items
        for s in range(3):
            sacredItemTypes = [SacredItemType.CAMPHORLEAF,
                               SacredItemType.KUDZULEAF,
                               SacredItemType.UMBRELLA]
            self.sacredItem.type = sacredItemTypes[s]
            # loop through actions
            for a in range(5):
                actions = [Action.STOP,
                           Action.FUNNYFACE,
                           Action.WORSHIPING,
                           Action.LEFTWALKING,
                           Action.RIGHTWALKING]
                self.action = actions[a]
                # loop through frames (time)
                for t in range(12):
                    self.time = t

                    # redraw
                    self.delete()
                    self.name = "Sacred Item: "+str(s)+" Action: "+str(a)+" Time: "+str(t)
                    self.draw()
                    self.c.after(delay)
                    self.c.update()
                    
        self.name = savedName
        self.displayName = savedDisplayName
        self.c.after(delay)
        self.c.update()
                    
    #######################################################################
    #  scale method                                                       #
    #                                                                     #
    #  Changes the size of the object, according to the xscale and        #
    #  yscale parameters, after a given delay.                            #
    #  Does not update canvas for you.                                    #
    #######################################################################
    def scale(self, xscale=1.0, yscale=1.0):
        self.c.scale(self.tag, self.center, self.bottom, xscale, yscale)
        self.c.scale(self.sacredItem, self.center, self.bottom, xscale, yscale)
        self.width = self.width * xscale
        self.height = self.height * yscale
        self.left = self.center - self.width/2
        self.right = self.center + self.width/2
        self.top = self.bottom - self.height
        self.middle = self.bottom - self.height/2


    #######################################################################
    #  delete method                                                      #
    #                                                                     #
    #  Deletes the bot from the canvas.  Note that the object still       #
    #  still exists after it is deleted; it is just not displayed.        #
    #  Does not update canvas for you.                                    #
    #######################################################################
    def delete(self):
        self.c.delete(self.tag)
        self.c.delete(self.sacredItem)

    #######################################################################
    #  redraw method                                                      #
    #                                                                     #
    #  Redraws the bot on the canvas.                                     #
    #  Does not update canvas for you.                                    #
    #######################################################################
    def redraw(self):
        self.delete()
        self.draw()
