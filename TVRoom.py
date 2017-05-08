###########################################################################
#                           Scenery TV Room Picture                       #
#                                                                         #
#   Programmed by Tim Adams (2/12/14)                                     #
#   Modified by Jaime Rodriguez (11/09/15)                                #
#                                                                         #
#   Description:  This a picture of a tv room.                            #
#                                                                         #
###########################################################################
from tkinter import *

def tv_room(c):
    left = 0
    top = 0
    width = 500
    height = 500
    right = left + width
    bottom = top + height
    gridSize = 50
    linecolor = "grey"

    #draw background-wall
    c.create_rectangle(10,10, 400,400, fill="light grey")

    #draw floor
    c.create_rectangle(10,275, 400,400, fill="saddle brown")

    #draw rug
    c.create_oval(150,287, 275,375, fill="light blue")
    #draw trim
    c.create_rectangle(10,270, 400,280,  fill="antique white")
    c.create_line(10,273, 400,273)

    #draw couch

    c.create_rectangle(315,235, 370,270, width=1, fill="grey20") #couch arm
    c.create_rectangle(360,180, 395,350, width=2, fill="grey14")#couch back
    c.create_polygon(395,350, 395,260, 325,250, 280,350, fill="grey14")#couch body
    c.create_rectangle(310,240, 395,280, width=2, fill="grey20")#couch arm


    #draw coffee table
    c.create_polygon(180,350, 183,353, 228,300, 225,303, 180,350)#table leg
    c.create_polygon(250,350, 253,347, 183,300, 180,303, 250,350)#table leg
    c.create_rectangle(175,290, 250,320, fill="grey19")#table surface

    #draw TV
    c.create_rectangle(12,140, 25,250, fill="black")#tv
    c.create_rectangle(15,145, 22,245, fill="blue")#tv screen

    #draw poster
    c.create_rectangle(140,60, 250,180, fill="gold")
    c.create_text(145,95,text="Don't worry. Be happy.", width=130, fill="black", font=("Helvetica",20), justify=CENTER, anchor=NW)

    #draw clock
    c.create_oval(310,60, 340,100, fill="ghost white")
    c.create_line(325,80, 334,92) 

    #draw remote control
    c.create_rectangle(205,295 , 230,301, width=2, fill="grey32") #controler
    c.create_oval(208,296, 210,297, fill="red", outline="red3") #power button
    c.create_oval(212,296, 214,297, fill="black")#button
    c.create_oval(216,296, 218,297, fill="black")#button
    c.create_oval(220,296, 222,297, fill="black")#button
    c.create_oval(224,296, 226,297, fill="black")#button


