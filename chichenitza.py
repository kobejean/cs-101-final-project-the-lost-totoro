########################################################################
#                           Chichenitza                                #
#                                                                      #
#   Programmed by Kassan Qian                                          #
#   Modified by Jean Flaherty (12/03/16)                               #
#   Instructor: Dean Zeller                                            #
#                                                                      #
#   Description: This is a picture of Chichenitza.                     #
#                                                                      #
########################################################################
from tkinter import *

def chichenitza(c, tag='chichenitza'): #purpose of renaming function is so that others can call the function.

    #Sky
    c.create_rectangle(0,0, 950,515, fill='skyblue2', tag=tag)


    #Grass
    c.create_rectangle(0,515, 950,594, fill='darkolivegreen4', tag=tag)
    c.create_rectangle(0, 505, 950,515, fill='burlywood3', tag=tag)

    #TOP
    c.create_polygon(373,210, 370,145, 469,110, 469,190,
                     450,187, 370,210, fill='bisque4', outline='black', tag=tag) #left
    c.create_polygon(469,190, 469,110, 595,137, 592,200,
                     598,210, 469,190, fill='bisque2', outline='black', tag=tag) #right

    #left door
    c.create_polygon(400,200, 400,185, 445,170, 445, 190,
                     fill='black', outline='black', tag=tag)

    #right door
    c.create_polygon(524,200, 520,190, 520,175, 535,178, 535,190, 540,200,
                     fill='black', outline='black', tag=tag)

    #Side stairs
    c.create_polygon(30,515, 40,480, 67,479,
                     77,455, 100,452, 115,423,
                     140,420, 150,390, 175,388,
                     185,360, 210,355, 220,325,
                     247,320, 255,290, 282,285,
                     295,255, 320,250, 325,223, 350,218, #top
                     52,515, 30,515, fill='gray25', outline='black', tag=tag)
    #Left strip
    c.create_polygon(52,515, 350,218, 70,515, 52,515,
                     fill='gray63', outline='black', tag=tag)
    #Right strip
    c.create_polygon(115,515, 410,199, 420,196, 125,515,
                     fill='gray63', outline='black', tag=tag) #top
    c.create_polygon(125,515, 420,196, 427,194, 190,515, 125,515,
                     fill='bisque3', outline='black', tag=tag)

    #path
    c.create_polygon(350,218, 70,515, 115,515, 410,200, 355,215, 350,218,
                     fill='gray30', outline='black', tag=tag)

    #Left Face
    c.create_polygon(190,515, 427,194, 450,187, 370,515, 190,515,
                     fill='gray25', outline='black', tag=tag)

    #Front Face
    c.create_polygon(370,515, 450,187, 490,195,
                     492,223, 501,226, 505,260,
                     520,260, 525,295, 540,297,
                     545,330, 560,332, 565,365,
                     577,368, 585,402, 599,404,
                     601,440, 620,440, 625,473, 640,473,
                     644,507, 370,515, fill='bisque3', outline='black', tag=tag)

    #grey jagged
    c.create_polygon(490,195,
                     492,223, 501,226, 505,260,
                     520,260, 525,295, 540,297,
                     545,330, 560,332, 565,365,
                     577,368, 585,402, 599,404,
                     601,440, 620,440, 625,473, 640,473,
                     644,507, #end of jaggedness
                     700,510, 490,195, fill='gray25', outline='black', tag=tag)

    #Left Strip 2
    c.create_polygon(490,195, 501,196, 715,512, 701,512, 490,195,
                     fill='bisque3', outline='black', tag=tag)
    #Right Strip 2
    c.create_polygon(584,208, 793.5,512, 805,512, 598,210,
                     fill='bisque3', outline='black', tag=tag)

    #Pathway 2
    c.create_polygon(501,196, 715,512, 793.5,512, 584,208,
                     fill='bisque2', outline='black', tag=tag)

    #right stairs
    c.create_polygon(598,210, 622,216, 635,245,
                     660,250, 670,280, 700,285,
                     710,315, 734,320, 746,350,
                     770,350, 782,380, 805,385,
                     815,415, 840,415, 850,449,
                     874,449, 883,475, 905,475,
                     915,510, 802,509,
                     fill='bisque2', outline='black', tag=tag)
