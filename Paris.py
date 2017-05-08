###########################################################################
#                           Paris Background 	                          #
#                                                                         #
#   Programmed by Taylor Fields (2-13-14)                                 #
#   Modified by Bianca Avila (10-28-2015)                                 #
#   Modified by Jean Flaherty (10-27-2016)                                #
#                                                                         #
#   Description:  This is a background with the Eiffel Tower              #
#                                                                         #
###########################################################################
from tkinter import *
def paris_scenery(c):
    #Draw Boundaries of Background
    c.create_rectangle(5,5, 400,400, fill='grey13')
    c.create_rectangle(5,375, 400,400, fill='dark green')

    #Draw Eiffel Tower
    c.create_polygon(30,400, 55,400, 87.5,325, 62.5,325, 30,400, fill='DarkOrange4', outline='black') #Left leg
    c.create_polygon(170,400, 195,400, 162.5,325, 137.5,325, 170,400, fill='DarkOrange4', outline='black') #Right leg
    c.create_polygon(60,315, 62.5,325, 162.5,325, 165,315, 60,315, fill='DarkOrange4', outline='black') #Base Level
    c.create_polygon(65,315, 87.5,315, 105,250, 82.5,250, 65,315, fill='DarkOrange4', outline='black') #Middle Left Post
    c.create_polygon(160,315, 137.5,315, 120,250, 142.5,250, 160,315, fill='DarkOrange4', outline='black') #Middle Right Post
    c.create_polygon(82.5,250, 142.5,250, 145,240, 80,240, 82.5,250, fill='DarkOrange4', outline='black') #2nd Base Level
    c.create_polygon(85,240, 107.5,240, 112.5,165, 117.5,240, 140,240, 125,100, 100,100, 85,240, fill='DarkOrange4', outline='black') #3rd Post
    c.create_polygon(100,100, 95,100, 95,75, 100,75, 100,70, 125,70, 125,75, 130,75, 130,100, 100,100, fill='DarkOrange4', outline='black') #Top Level

    #Draw Flag and Pole
    c.create_rectangle(112.5,35, 125,60, fill='blue') #Blue portion of flag
    c.create_rectangle(125,60, 137.5,35, fill='white') #White portion of flag
    c.create_rectangle(137.5,35, 150,60, fill='red') #Red portion of flag
    c.create_line(112.5,70, 112.5,35, width=3, fill='black') #Flag Pole

    #Draw Moon
    c.create_oval(25,25, 75,75, fill='light goldenrod') #Moon
    c.create_oval(50,25, 100,75, fill='grey13',width=0) #Dark spot of moon

    #Draw Red Fireworks
    c.create_arc(175,75, 225,125, start=25, extent= 110, style=ARC, width=2, outline='red')
    c.create_arc(165,65, 226,125, start=25, extent= 110, style=ARC, width=2, outline='red')
    c.create_arc(155,55, 226,125, start=25, extent= 110, style=ARC, width=2, outline='red')
    c.create_arc(275,75, 220,125, start=155, extent= -110, style=ARC, width=2, outline='red')
    c.create_arc(285,65, 219,125, start=155, extent= -110, style=ARC, width=2, outline='red')
    c.create_arc(295,55, 219,125, start=155, extent= -110, style=ARC, width=2, outline='red')

    #Draw White Fireworks
    c.create_arc(225,125, 275,170, start=25, extent= 110, style=ARC, width=2, outline='white')
    c.create_arc(215,115, 276,170, start=25, extent= 110, style=ARC, width=2, outline='white')
    c.create_arc(205,105, 276,170, start=25, extent= 110, style=ARC, width=2, outline='white')
    c.create_arc(325,125, 270,170, start=155, extent= -110, style=ARC, width=2, outline='white')
    c.create_arc(335,115, 269,170, start=155, extent= -110, style=ARC, width=2, outline='white')
    c.create_arc(345,105, 269,170, start=155, extent= -110, style=ARC, width=2, outline='white')


