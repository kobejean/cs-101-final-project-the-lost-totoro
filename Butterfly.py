###########################################################################
#              Assignment 7 -- Complex Bot (Multi-pose)                   #
#                            Butterfly                                    #
#                                                                         #
#  Programmed by Megan Rink February 29, 2016                             #
#  Instructor:  Dean Zeller                                               #
#  Modified by Jean Flaherty (12/03/16)                                   #
#                                                                         #
#  Description:  The file contains a butterfly object and an              #
#                accompanying enumerated data type to define the          #
#                different butterfly poses.                               #
#                                                                         #
#  Objects:                                                               #
#               Pose    Enumerated data type for five different           #
#                       butterflies.                                      #
#               Butterfly   A traditional butterfly with different        #
#                           movements for each defined in the Butterfly   #
#                           class.                                        #
#                                                                         #
#  This program is copyright (c) 2016 Megan Rink and Dean Zeller.         #
#  All rights reserved.  Permission granted to use and modify for         #
#  educational purposes only.  Any commercial use of this code must       #
#  receive permission from the author(s).                                 #
###########################################################################
from tkinter import *

###########################################################################
#                           Pose                                          #
#                                                                         #
#   Description:  This class defines five different movements, for use    #
#                 in the Butterfly class.  The butterflies include:       #
#                 antenna movement, wings up, wings down, wings in,       #
#                 wings out.                                              #
###########################################################################

class Pose:  #enumerated data type
    WINGSUP=0
    WINGSDOWN=1
    WINGSOUT=2
    WINGSMIDDLE=3
    WINGSIN=4
    numPoses=5 # number of poses, necessary for nextPose method

###########################################################################
#                               Butterfly                                 #
#                                                                         #
#   Description:  This uses the tkinter graphics library to create a      #
#                 classic butterfly, based on the user's parameters.      #
#                                                                         #
#   Parameters:                                                           #
#           canvas         Canvas to draw the picture                     #
#           left, top      Left and top of the entire picture             #
#           width, height  Width and height of the entire picture         #
#           butterflyColor      Color of the body                         #
#           wingColor       Color of the wings                            #
#           antennaColor     Color of the antennas                        #
#           name           Name of the face                               #
#           displayName    Boolean to display the character name          #
#                              0 -> does not display name                 #
#                              1 -> displays name                         #
#           pose           Butterfly poses (see Pose class above)         #
###########################################################################
class Butterfly:

    # class attributes
    objectName = "RinkMeganBotButterfly"  # Title for this object
    objectNum = 0                     # Number of instances created

    #######################################################################
    #  __init__ constructor                                               #
    #                                                                     #
    #  Initializes all attributes to given parameters.                    #
    #######################################################################
    def __init__ (self, canvas, left=0,top=0,width=400,height=400,
                  butterflyColor="grey13", wingColor="lightcoral", wingColor2="coral2", antennaColor="grey33", lineColor="coral1",
                  name="blank", displayName=0, pose=Pose.WINGSUP):
        
        # attributes directly from parameters
        self.c = canvas
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.butterflyColor = butterflyColor
        self.wingColor = wingColor
        self.wingColor2 = wingColor2
        self.antennaColor = antennaColor
        self.lineColor = lineColor
        self.name = name
        self.displayName = displayName
        self.pose = pose

        # calculated attributes
        self.tag = Butterfly.objectName + str(Butterfly.objectNum)
        Butterfly.objectNum += 1
        self.right = self.left + self.width
        self.bottom = self.top + self.height
        self.center = (self.left + self.right) / 2.0
        self.middle = (self.top + self.bottom) / 2.0

    #######################################################################
    #  draw method                                                        #
    #                                                                     #
    #  Draws the face according to the attributes, including size,        #
    #  position, colors, and pose portrayed.                              #
    #                                                                     #
    #  Common coordinates:                                                #
    #      body                                                           #
    #      body lines                                                     #
    #                                                                     #
    #  Variable coordinates:                                              #
    #      wings                                                          #
    #      antenna                                                        #
    #                                                                     #
    #  Drawing:                                                           #
    #      Draw all shapes in their assigned coordinates.                 #
    #######################################################################
    def draw(self):

        # create X-coordinate guide list
        xspaces = 150  # number of guides in the guide list
        xgridwidth = 1.0 * self.width / xspaces
        x = []
        for i in range(xspaces+1):
            x.append(self.left + i*xgridwidth)

        # create Y-coordinate guide list
        yspaces = 150  # number of guides in the guide list
        ygridwidth = 1.0 * self.height / yspaces
        y = []
        for i in range(yspaces+1):
            y.append(self.top + i*ygridwidth)
            
        ###################################################################
        #                   Coordinates                                   #
        ###################################################################
        
        # butterfly guides (two points)
        body  = ((x[70],y[50]),(x[80],y[100]))

        # line guides (two points each)
        line1  = (( x[70],y[70]),(x[80],y[70]))
        line2  = ((x[70],y[80]) , (x[80],y[80]))
        line3  = ((x[71],y[90]) , (x[79],y[90]))

        # antenna guides (two points each)
        antenna1 = ((x[75],y[50]) ,  (x[70],y[40]))
        antenna2 = ((x[75],y[50]) , (x[80],y[40]))

        # wing1 guides (eight points)
        wing1 =  ((x[70],y[70]) , (x[60],y[80]) , (x[30],y[100]) , (x[30],y[110]) , (x[40],y[120]) , (x[60],y[110]) , (x[70],y[100]) , (x[70],y[90]))

        # wing2 guides (eight points)
        wing2 =  ((x[80],y[70]) , (x[90],y[80]) , (x[120],y[100]) , (x[120],y[110]) , (x[110],y[120]) , (x[90],y[110]) , (x[80],y[100]) , (x[80],y[90]))

        # wing3 guides (eight points)
        wing3 =  ((x[70],y[60]) , (x[60],y[40]) , (x[50],y[30]) , (x[30],y[30]) , (x[20],y[40]) , (x[20],y[50]) , (x[50],y[80]) , (x[70],y[90]))

        # wing4 guides (eight points)
        wing4 =  ((x[80],y[60]) , (x[90],y[40]) , (x[100],y[30]) , (x[120],y[30]) , (x[130],y[40]) , (x[130],y[50]) , (x[100],y[80]) , (x[80],y[90]))

        ###################################################################
        #                   Common Coordinates                            #
        ###################################################################
        
       # butterfly guides (two points)
        body  = ((x[70],y[50]),(x[80],y[100]))

        # line guides (two points each)
        line1  = (( x[70],y[70]),(x[80],y[70]))
        line2  = ((x[70],y[80]) , (x[80],y[80]))
        line3  = ((x[71],y[90]) , (x[79],y[90]))

        # antenna guides (two points each)
        antenna1 = ((x[75],y[50]) ,  (x[70],y[40]))
        antenna2 = ((x[75],y[50]) , (x[80],y[40]))

        ###################################################################
        #                 Variable Coordinates                            #
        ###################################################################

        diff=7
        
        # wings and antenna guides
        if self.pose == Pose.WINGSUP:
            # wings move upward
            wing1 =  ((x[70],y[60]) , (x[60],y[70]) , (x[30],y[90]) , (x[30],y[100]) , (x[40],y[110]) , (x[60],y[100]) , (x[70],y[90]) , (x[70],y[80]))
            wing2 =  ((x[80],y[60]) , (x[90],y[70]) , (x[120],y[90]) , (x[120],y[100]) , (x[110],y[110]) , (x[90],y[100]) , (x[80],y[90]) , (x[80],y[80]))
            wing3 =  ((x[70],y[50]) , (x[60],y[30]) , (x[50],y[20]) , (x[30],y[20]) , (x[20],y[30]) , (x[20],y[40]) , (x[50],y[70]) , (x[70],y[80]))
            wing4 =  ((x[80],y[50]) , (x[90],y[30]) , (x[100],y[20]) , (x[120],y[20]) , (x[130],y[30]) , (x[130],y[40]) , (x[100],y[70]) , (x[80],y[80]))
        elif self.pose == Pose.WINGSDOWN:
            # wings move downward
            wing1 =  ((x[70],y[80]) , (x[60],y[90]) , (x[30],y[110]) , (x[30],y[120]) , (x[40],y[130]) , (x[60],y[120]) , (x[70],y[110]) , (x[70],y[100]))
            wing2 =  ((x[80],y[80]) , (x[90],y[90]) , (x[120],y[110]) , (x[120],y[120]) , (x[110],y[130]) , (x[90],y[120]) , (x[80],y[110]) , (x[80],y[100]))
            wing3 =  ((x[70],y[70]) , (x[60],y[50]) , (x[50],y[40]) , (x[30],y[40]) , (x[20],y[50]) , (x[20],y[60]) , (x[50],y[90]) , (x[70],y[100]))
            wing4 =  ((x[80],y[70]) , (x[90],y[50]) , (x[100],y[40]) , (x[120],y[40]) , (x[130],y[50]) , (x[130],y[60]) , (x[100],y[90]) , (x[80],y[100]))
        elif self.pose == Pose.WINGSOUT:
            # wings move outward
            wing1 =  ((x[70],y[70]) , (x[60],y[80]) , (x[30],y[100]) , (x[30],y[110]) , (x[40],y[120]) , (x[60],y[110]) , (x[70],y[100]) , (x[70],y[90]))
            wing2 =  ((x[80],y[70]) , (x[90],y[80]) , (x[120],y[100]) , (x[120],y[110]) , (x[110],y[120]) , (x[90],y[110]) , (x[80],y[100]) , (x[80],y[90]))
            wing3 =  ((x[70],y[60]) , (x[60],y[40]) , (x[50],y[30]) , (x[30],y[30]) , (x[20],y[40]) , (x[20],y[50]) , (x[50],y[80]) , (x[70],y[90]))
            wing4 =  ((x[80],y[60]) , (x[90],y[40]) , (x[100],y[30]) , (x[120],y[30]) , (x[130],y[40]) , (x[130],y[50]) , (x[100],y[80]) , (x[80],y[90]))
        elif self.pose == Pose.WINGSMIDDLE:
            wing1 =  ((x[70],y[70]) , (x[60+diff//2],y[80]) , (x[30+diff],y[100]) , (x[30+diff*2],y[110]) , (x[40+diff*2],y[120]) , (x[60+diff//2],y[110]) , (x[70],y[100]) , (x[70],y[90]))
            wing2 =  ((x[80],y[70]) , (x[90-diff//2],y[80]) , (x[120-diff],y[100]) , (x[120-diff*2],y[110]) , (x[110-diff*2],y[120]) , (x[90-diff//2],y[110]) , (x[80],y[100]) , (x[80],y[90]))
            wing3 =  ((x[70],y[60]) , (x[60+diff//2],y[40]) , (x[50+diff],y[30]) , (x[30+3*diff//2],y[30]) , (x[20+diff*2],y[40]) , (x[20+diff*2],y[50]), (x[50+diff],y[80]) , (x[70],y[90]))
            wing4 =  ((x[80],y[60]) , (x[90-diff//2],y[40]) , (x[100-diff],y[30]) , (x[120-3*diff//2],y[30]) , (x[130-diff*2],y[40]) , (x[130-diff*2],y[50]) , (x[100-diff],y[80]) , (x[80],y[90]))
        elif self.pose == Pose.WINGSIN:
            wing1 =  ((x[70],y[70]) , (x[60+diff],y[80]) , (x[30+diff*2],y[100]) , (x[30+diff*4],y[110]) , (x[40+diff*4],y[120]) , (x[60+diff],y[110]) , (x[70],y[100]) , (x[70],y[90]))
            wing2 =  ((x[80],y[70]) , (x[90-diff],y[80]) , (x[120-diff*2],y[100]) , (x[120-diff*4],y[110]) , (x[110-diff*4],y[120]) , (x[90-diff],y[110]) ,(x[80],y[100]) , (x[80],y[90]))
            wing3 =  ((x[70],y[60]) , (x[60+diff],y[40]) , (x[50+diff*2],y[30]) , (x[30+diff*2],y[30]) , (x[20+diff*4],y[40]) , (x[20+diff*4],y[50]) ,  (x[50+diff*2],y[80]) , (x[70],y[90]))
            wing4 =  ((x[80],y[60]) , (x[90-diff],y[40]) , (x[100-diff*2],y[30]) , (x[120-diff*2],y[30]) , (x[130-diff*4],y[40]) , (x[130-diff*4],y[50]) , (x[100-diff*2],y[80]) , (x[80],y[90]))
        else:  # print warning message, unimplemented emotion
            print ("Error -- unimplemented pose")

        ###################################################################
        #                   Drawing                                       #
        ###################################################################
        
        # draw body
        self.bodyID = self.c.create_oval(body, fill=self.butterflyColor, tag=self.tag)

        # draw lines
        self.c.create_line(line1, width=3, fill='coral1', tag=self.tag)
        self.c.create_line(line2, width=3, fill='coral1', tag=self.tag)
        self.c.create_line(line3, width=3, fill='coral1', tag=self.tag)

        # draw antenna
        self.c.create_line(antenna1, width=5, fill="grey33", tag=self.tag)
        self.c.create_line(antenna2, width=5, fill="grey33", tag=self.tag)

        # draw wing1 
        self.wing1ID = self.c.create_polygon(wing1, fill=self.wingColor, tag=self.tag)

        # draw wing2
        self.wing2ID = self.c.create_polygon(wing2, fill=self.wingColor, tag=self.tag)
        
        #draw wing3
        self.wing3ID = self.c.create_polygon(wing3, fill=self.wingColor2, tag=self.tag)

        #draw wing4
        self.wing4ID = self.c.create_polygon(wing4, fill=self.wingColor2, tag=self.tag)

        # 
        if self.displayName:  # only display if displayName flag is set
            self.c.create_text(self.center, self.bottom, anchor=N,
                               text=self.name, tag=self.tag)

##        self.c.update()
        
    #######################################################################
    #  move method                                                        #
    #                                                                     #
    #  Moves the bot on the canvas, relative to its current position,     #
    #  after the specified delay.  Attributes are adjusted accordingly.   #
    #######################################################################
    def move (self, deltaX=0, deltaY=0, delay=0):
        # adjust attributes
        self.left += deltaX
        self.top += deltaY
        self.right += deltaX
        self.bottom += deltaY
        self.center += deltaX
        self.middle += deltaY
        # move face
##        self.c.after(delay)
        self.c.move(self.tag,deltaX,deltaY)
##        self.c.update()

    #######################################################################
    #  moveTo method                                                      #
    #                                                                     #
    #  Moves the bot on the canvas to a specific location, broken         #
    #  into a series of steps, each after the specified delay.            #
    #######################################################################
    def moveTo (self, x=0, y=0, steps=10, delay=0):
        # calculate deltaX and deltaY
        distX = x - self.left
        deltaX = distX * 1.0 / steps
        distY = y - self.top
        deltaY = distY * 1.0 / steps
        # move in steps
        for i in range(steps):
            self.move(deltaX=deltaX, deltaY=deltaY, delay=delay)

    #######################################################################
    #  setProperties method                                               #
    #                                                                     #
    #  Changes the parameters of the bot.  If a parameter is not          #
    #  specified, then it remains unchanged.                              #
    #######################################################################
    def setProperties (self, butterflyColor="default", butterflyColor2="default",
                       wingColor="default", wingColor2="defalt"):
        
        if butterflyColor != "default":
            self.butterflyColor=butterflyColor
            self.c.itemconfig(self.bodyID, fill=self.butterflyColor)
            self.c.update()
##        if butterflyColor2 != "default":
##            self.butterflyColor2=butterflyColor2
##            self.c.itemconfig(self.topLineID, fill=self.butterflyColor2)
##            self.c.itemconfig(self.middleLineID, fill=self.butterflyColor2)
##            self.c.itemconfig(self.bottomLineID, fill=self.butterflyColor2)
##            self.c.update()
        if wingColor != "default":
            self.wingColor=wingColor
            self.c.itemconfig(self.wing1ID, fill=self.wingColor)
            self.c.itemconfig(self.wing2ID, fill=self.wingColor)
            self.c.update()
        if wingColor2 != "default":
            self.wingColor2=wingColor2
            self.c.itemconfig(self.wing3ID, fill=self.wingColor2)
            self.c.itemconfig(self.wing4ID, fill=self.wingColor2)
            self.c.update()

    #######################################################################
    #  setPose method                                                     #
    #                                                                     #
    #  Changes the pose of the face to the specified pose.                #
    #######################################################################
    def setPose (self, pose=Pose.WINGSUP, delay=5):
##        self.c.after(delay)
##        self.delete(delay=0)
        self.pose = pose
        self.draw()
##        self.c.update()

    #######################################################################
    #  nextPose method                                                    #
    #                                                                     #
    #  Changes the pose of the face to the next in the defined list.      #
    #######################################################################
    def nextPose (self, delay=5):
##        self.c.after(delay)
        self.delete(delay=0)
        self.pose = (self.pose + 1) % Pose.numPoses
        self.draw()
##        self.c.update()
        
    #######################################################################
    #  scale method                                                       #
    #                                                                     #
    #  Changes the size of the object, according to the xscale and        #
    #  yscale parameters, after a given delay.                            #
    #                                                                     #
    #  Note:  There is a bug in this method.  The left, right, top, and   #
    #  bottom are not recalculated.  For most cases, this will not affect #
    #  animation playback.  However, the potential for problems exist.    #
    #######################################################################
    def scale(self, xscale=1.0, yscale=1.0, delay=0):
##        self.c.after(delay)
        self.c.scale(self.tag, self.center, self.middle, xscale, yscale)
        self.width = self.width * xscale
        self.height = self.height * yscale
##        self.c.update()

    #######################################################################
    #  pause method                                                       #
    #                                                                     #
    #  Delays the animation, according to the after parameter specified.  #
    #######################################################################
    def pause(self, delay):
        self.c.after(delay)
        self.c.update()

    #######################################################################
    #  delete method                                                      #
    #                                                                     #
    #  Deletes the bot from the canvas.  Note that the object still       #
    #  still exists after it is deleted; it is just not displayed.        #
    #######################################################################
    def delete(self, delay=0):
##        self.c.after(delay)
        self.c.delete(self.tag)
##        self.c.update()



    

    

