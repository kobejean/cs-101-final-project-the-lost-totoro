################################################################################
#                                     A Peek Under the Sea                     #
#   Programmed by Selena Baltierra (Sept. 3rd, 2014)                           #
#   Modified by Jason Acosta (11-11-15)                                        #
#   Modified by Jean Flaherty (10-27-2016)                                     #
#   Description: This is a scenic picture of under the sea, with a fish.       #
#   Modification: Converted basic picture into a function.                     #
#                                                                              #
################################################################################
from tkinter import *
def under_the_sea(c):

    #Making the colors of the ocean
    c.create_rectangle (0,0, 600,40, outline='CadetBlue1', fill='CadetBlue1')
    c.create_rectangle (600,40, 0,80, outline='turquoise1', fill='turquoise1')
    c.create_rectangle (0,80, 600,120, outline='turquoise2', fill='turquoise2')
    c.create_rectangle (600,120, 0,160, outline='turquoise3', fill='turquoise3')
    c.create_rectangle (600,200, 0,240, outline='light sea green', fill='light sea green')
    c.create_rectangle (0,160, 600,200, outline='dark turquoise', fill='dark turquoise')
    c.create_rectangle (0,240, 600,280, outline='DeepSkyBlue4', fill='DeepSkyBlue4')
    c.create_rectangle (600,280, 0,320, outline='DodgerBlue4', fill='DodgerBlue4')
    c.create_rectangle (0,320, 600,405, outline='tan2', fill='tan2')

    #Creating the clam
    c.create_oval (45,310, 66,324, outline='peach puff', fill='peach puff')
    c.create_polygon (60,320, 60,330, 75,320, outline='peach puff', fill='peach puff')
    c.create_line (54,320, 60,324, width=.5, fill='plum3')
    c.create_line (57,316, 60,320, width=.5, fill='plum3')
    c.create_line (60,314, 63,320, width=.5, fill='plum3')

    #Creating the fish
    c.create_oval (150,160, 300,100, outline='SlateBlue2', fill='SlateBlue2')
    c.create_polygon (315,150, 315,150, 255,130, 315,100, 315,100, outline='DarkOrchid4', fill='DarkOrchid4',smooth=1)

    #Creating his eye and mouth
    c.create_oval (174,116, 183,124, outline='black', fill='black')
    c.create_oval (153,132, 159,140, outline='SlateBlue2', fill='tomato4')

    #Creating his scales
    c.create_oval (210,100, 240,120, outline='DarkOrchid4', fill='DarkOrchid4')
    c.create_oval (240,120, 210,140, outline='DarkOrchid4', fill='DarkOrchid4')
    c.create_oval (210,140, 240,160, outline='DarkOrchid4', fill='DarkOrchid4')
    c.create_oval (225,100, 255,120, outline='DarkOrchid1', fill='DarkOrchid1')
    c.create_oval (255,120, 225,140, outline='DarkOrchid1', fill='DarkOrchid1')
    c.create_oval (225,140, 255,160, outline='DarkOrchid1', fill='DarkOrchid1')
    c.create_oval (240,102, 270,122, outline='DarkOrchid4', fill='DarkOrchid4')
    c.create_oval (270,122, 240,140, outline='DarkOrchid4', fill='DarkOrchid4')
    c.create_oval (240,140, 270,158, outline='DarkOrchid4', fill='DarkOrchid4')
    c.create_oval (285,153, 255,140, outline='DarkOrchid1', fill='DarkOrchid1')
    c.create_oval (255,120, 285,140, outline='DarkOrchid1', fill='DarkOrchid1')
    c.create_oval (289,108, 252,119, outline='DarkOrchid1', fill='DarkOrchid1')
    c.create_oval (270,150, 294,110, outline='Darkorchid4', fill='DarkOrchid4')

    #Creating Bubbles
    c.create_oval (147,134, 141,130, outline='LightBlue1',width=2, fill='LightBlue2')
    c.create_oval (129,126, 111,112, outline='LightBlue1', width=2, fill='LightBlue2')
    c.create_oval (135,80, 159,100, outline='LightBlue1', width=2, fill='LightBlue2')
    c.create_oval (105,56, 126,72, outline='LightBlue1', width=2, fill='LightBlue2')
    c.create_oval (177,18, 135,52, outline='LightBlue1', width=2, fill='LightBlue2')
    c.create_oval (105,0, 138,10, outline='LightBlue1', width=2, fill='LightBlue2')


