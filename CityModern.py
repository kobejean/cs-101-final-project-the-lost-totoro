############################################################################
#                                City                                      #
#                                                                          #
#   Programmed by Mark Buerck (01-28-14)                                   #
#   Modified by Dean Zeller (01-08-15)                                     #
#                                                                          #
#   Description: This is scenery of a modern city.                         #
#                                                                          #
############################################################################
from tkinter import *

def city_scenery(c):

    # background and sky
    c.create_rectangle(10,10, 400,400, width=5, outline='red', fill='lightskyblue')
    c.create_oval(160,40, 230,110, fill='gold')
    c.create_oval(60,30, 80,40, fill='white')
    c.create_oval(240,40, 260,50, fill='white')
    c.create_oval(310,30, 330,40, fill='white')
    c.create_oval(110,60, 130,70, fill='white')

    # center back building
    c.create_rectangle(150,220, 240,400, fill='gray90')

    # center building
    c.create_rectangle(160,310, 250,400, fill='gray60')
    c.create_rectangle(165,300, 245,310, fill='gray60')
    c.create_rectangle(170,290, 240,300, fill='gray60')
    c.create_rectangle(175,160, 235,290, fill='gray60')
    c.create_rectangle(185,90, 225,160, fill='gray60')
    c.create_rectangle(187,85, 223,90, fill='gray60')
    c.create_rectangle(189,80, 221,85, fill='gray60')
    c.create_rectangle(191,75, 219,80, fill='gray60')
    c.create_rectangle(193,70, 217,75, fill='gray60')
    c.create_rectangle(195,65, 215,70, fill='gray60')
    c.create_rectangle(197,60, 213,65, fill='gray60')
    c.create_rectangle(199,55, 211,60, fill='gray60')
    c.create_rectangle(201,30, 209,55, fill='gray60')

    # right back building
    c.create_rectangle(280,50, 360,400, fill='gray90')

    # left back building
    c.create_rectangle(45,80, 130,400, fill='gray90')

    # left middle building
    c.create_rectangle(40,180, 110,400, fill='gray60')
    c.create_rectangle(50,170, 100,180, fill='gray60')

    # right middle building
    c.create_rectangle(300,100, 380,400, fill='gray60')
    c.create_rectangle(339,60, 341,80, outline='black', fill='gray60')
    c.create_polygon(300,100, 320,80, 360,80, 380,100, fill='gray60', outline='black')

    # front right building
    c.create_rectangle(230,320, 390,400, fill='gray35')
    c.create_polygon(260,320, 310,260, 360,320, outline='black', fill='gray35')

    # front left building
    c.create_rectangle(20,340, 140,400, fill='gray35')
    c.create_arc(50,310, 110,370, start=0, extent=180, fill='gray35')

