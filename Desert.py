############################################################################
#                                Desert                                    #
#                                                                          #
#   Programmed by Ian Micklethwaite (01-28-14)                             #
#   Modified by Dean Zeller (01-08-15)                                     #
#                                                                          #
#   Description: This is scenery of a scorching-hot desert.                #
#                                                                          #
############################################################################
from tkinter import *

def desert_scenery(c):

    #border
    c.create_rectangle(10,10, 400,400, fill="lightcyan2")

    #background sand
    c.create_rectangle(11,190, 399,399, fill="goldenrod1", outline="goldenrod1")
    c.create_rectangle(11,190, 399,399, fill="goldenrod2", outline="goldenrod2",
                       stipple='gray12')

    #sun
    c.create_oval(15,11, 105,100, fill="light cyan", outline="light cyan")
    c.create_oval(30,25, 90,85, fill="azure", outline="azure")
    c.create_oval(40,35, 80,75, fill="light yellow", outline="light yellow")
    c.create_oval(50,45, 70,65, fill="light goldenrod yellow",
                  outline="light goldenrod yellow")

    #background dune
    c.create_polygon(10,190, 10,190, 50,160, 150,140, 200,150, 300,170, 400,190,
                     smooth="1", fill="lightgoldenrod1")
    c.create_polygon(10,190, 10,190, 50,160, 150,140, 200,150, 300,170, 400,190,
                     smooth="1", fill="#ffe359", stipple='gray12')
    c.create_polygon(10,190, 10,190, 55,165, 155,145, 205,155, 305,175, 400,190,
                     smooth="1", fill="goldenrod1")
    c.create_polygon(10,190, 10,190, 55,165, 155,145, 205,155, 305,175, 400,190,
                     smooth="1", fill="#ffb916", stipple='gray12')
    c.create_polygon(10,190, 10,190, 70,180, 170,160, 220,170, 320,190, 400,190,
                     smooth="1", fill="#f4b624")
    c.create_polygon(10,190, 10,190, 70,180, 170,160, 220,170, 320,190, 400,190,
                     smooth="1", fill="#f2ae10", stipple='gray12')


    #oasis pond
    c.create_polygon(210,195, 215,200, 180,235, 200,240, 230,250,
                     260,230, 280,250, 340,220, 380,200, smooth="1",
                     fill="skyblue1", width=4)


    #middleground dune
    c.create_polygon(10,190, 10,190, 40,180, 70,175, 180,170, 310,110, 350,140,
                     400,180, 400,180, 400,190, 400,190, smooth="1",
                     fill="lightgoldenrod2")
    c.create_polygon(10,190, 10,190, 40,180, 70,175, 180,170, 310,110, 350,140,
                     400,180, 400,180, 400,190, 400,190, smooth="1",
                     fill="#ffe359", stipple='gray12')
    c.create_polygon(10,190, 10,190, 40,185, 70,180, 260,170, 310,110, 350,140,
                     400,180, 400,180, 400,190, 400,190, smooth="1",
                     fill="goldenrod1")
    c.create_polygon(10,190, 10,190, 40,185, 70,180, 260,170, 310,110, 350,140,
                     400,180, 400,180, 400,190, 400,190, smooth="1",
                     fill="#ffb916", stipple='gray12')
    c.create_polygon(10,190, 10,190, 40,185, 70,180, 300,170, 310,110, 350,140,
                     400,180, 400,180, 400,190, 400,190, smooth="1",
                     fill="#f4b624")
    c.create_polygon(10,190, 10,190, 40,185, 70,180, 300,170, 310,110, 350,140,
                     400,180, 400,180, 400,190, 400,190, smooth="1",
                     fill="#f2ae10", stipple='gray12')

    #roadway
    c.create_polygon(10,190, 10,190, 70,200, 110,220, 170,250, 230,290, 270,310,
                     330,330, 400,350, 400,350, 400,400, 400,400, 270,400, 270,400,
                     230,350, 195,310, 160,270, 130,245, 110,230, 70,205, 10,190,
                     smooth=1, fill="gray15")
    c.create_polygon(10,190, 10,190, 70,200, 110,220, 170,250, 230,290, 270,310,
                     330,330, 400,350, 400,350, 400,400, 400,400, 270,400, 270,400,
                     230,350, 195,310, 160,270, 130,245, 110,230, 70,205, 10,190,
                     smooth=1, fill="gray8", stipple='gray75')

    #dividing lines
    c.create_line(370,395, 265,335, fill="gold2", dash=(80,), width=5)
    c.create_line(265,335, 210,295, fill="gold2", dash=(40,), width=4)
    c.create_line(210,295, 155,253, fill="gold2", dash=(30,), width=2)
    c.create_line(155,253, 100,220, fill="gold2", dash=(2,), width=1)

    #sign
    c.create_line(170,390, 170,350, fill="gray60", width=4)
    c.create_rectangle(150,350, 190,300, fill="gray95", outline="gray95")
    c.create_rectangle(152,348, 188,302, fill="gray95", outline="gray6", width=3)
    c.create_text(153,316, text="85", fill="gray6", font=("Helvetica",23),
                  justify=LEFT, anchor=NW)
    c.create_text(170,305, text="SPEED \n LIMIT", fill="gray6", font=("Helvetica",5),
                  justify=CENTER, anchor=N)
