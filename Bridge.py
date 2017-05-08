########################################################################
#                               Bridge                                 #
#                                                                      #
#   Programmed by Joe Rider (September 2, 2014)                        #
#   Modified by James Derr (12/03/15)                                  #
#   Instructor: Dean Zeller                                            #
#                                                                      #
#   Description: This is a picture of a bridge.                        #
#                                                                      #
########################################################################
from tkinter import *

def scenery_bridge(c):
    #Sky
    c.create_rectangle(10,10, 400,400, fill="SkyBlue1")
    #Ocean
    c.create_rectangle(10,300, 400,400, fill="RoyalBlue2")
    #Sun
    c.create_oval(11,11, 47,47, fill="yellow")
    #Road
    c.create_rectangle(10,270, 400,275, fill="DarkOrange3")
    #Platforms
    c.create_rectangle(50,295, 80,300, fill="DarkOrange3")
    c.create_rectangle(270,295, 300,300, fill="DarkOrange3")
    #Left Poles
    c.create_rectangle(53,200, 58,295, fill="DarkOrange3")
    c.create_rectangle(72,200, 77,295, fill="DarkOrange3")
    #Right Poles
    c.create_rectangle(273,200, 278,295, fill="DarkOrange3")
    c.create_rectangle(292,200, 297,295, fill="DarkOrange3")
    #Left Horizontal Wires
    c.create_line(10,230, 53,200, fill="DarkOrange3")
    c.create_line(10,235, 72,200, fill="DarkOrange3")
    #Middle Horizontal Wires
    c.create_line(58,200, 163,300, 273,200, fill="DarkOrange3", smooth=1)
    c.create_line(77,200, 173,300, 292,200, fill="DarkOrange3", smooth=1)
    #Right Horizontal Wires
    c.create_line(278,200, 339,225, 400,230, fill="DarkOrange3", smooth=1)
    c.create_line(297,200, 348,225, 400,235, fill="DarkOrange3", smooth=1)
    #Vertical Wires
    c.create_line(14,227, 14,270, fill="DarkOrange3")
    c.create_line(17,230, 17,270, fill="DarkOrange3")
    c.create_line(34,214, 34,270, fill="DarkOrange3")
    c.create_line(37,219, 37,270, fill="DarkOrange3")
    c.create_line(94,228, 94,270, fill="DarkOrange3")
    c.create_line(97,218, 97,270, fill="DarkOrange3")
    c.create_line(114,240, 114,270, fill="DarkOrange3")
    c.create_line(117,232, 117,270, fill="DarkOrange3")
    c.create_line(134,245, 134,270, fill="DarkOrange3")
    c.create_line(137,242, 137,270, fill="DarkOrange3")
    c.create_line(154,250, 154,270, fill="DarkOrange3")
    c.create_line(157,249, 157,270, fill="DarkOrange3")
    c.create_line(174,250, 174,270, fill="DarkOrange3")
    c.create_line(177,250, 177,270, fill="DarkOrange3")
    c.create_line(194,246, 194,270, fill="DarkOrange3")
    c.create_line(197,249, 197,270, fill="DarkOrange3")
    c.create_line(214,240, 214,270, fill="DarkOrange3")
    c.create_line(217,244, 217,270, fill="DarkOrange3")
    c.create_line(234,230, 234,270, fill="DarkOrange3")
    c.create_line(237,236, 237,270, fill="DarkOrange3")
    c.create_line(254,216, 254,270, fill="DarkOrange3")
    c.create_line(257,226, 257,270, fill="DarkOrange3")
    c.create_line(314,213, 314,270, fill="DarkOrange3")
    c.create_line(317,209, 317,270, fill="DarkOrange3")
    c.create_line(334,219, 334,270, fill="DarkOrange3")
    c.create_line(337,217, 337,270, fill="DarkOrange3")
    c.create_line(354,223, 354,270, fill="DarkOrange3")
    c.create_line(357,223, 357,270, fill="DarkOrange3")
    c.create_line(374,227, 374,270, fill="DarkOrange3")
    c.create_line(377,230, 377,270, fill="DarkOrange3")
    c.create_line(394,229, 394,270, fill="DarkOrange3")
    c.create_line(397,235, 397,270, fill="DarkOrange3")
    #Clouds
    c.create_oval(100,36, 245,66, outline="white smoke", fill="white smoke")
    c.create_oval(235,66, 360, 86, outline="white smoke", fill="white smoke")
    c.create_oval(295,28, 386,40, outline="white smoke", fill="white smoke")

