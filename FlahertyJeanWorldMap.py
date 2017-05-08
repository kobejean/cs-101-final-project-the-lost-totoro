############################################################################
#                                World Map                                 #
#                                                                          #
#   Programmed by Jean Flaherty (10-26-16)                                 #
#                                                                          #
#   Description: This is a 400x400 picture of a world map.                 #
#                                                                          #
############################################################################
from tkinter import *

def world_map(c, tag="worldmap"):

    #border
    ocean_color = "#124B70"
    land_color = "#3B7354"
    snow_color = "#D3EAE0"
    outline_color = "#000000"
    
    #ocean
    c.create_rectangle(0,0, 405,405,
                       fill=ocean_color, outline=outline_color, tag=tag)
    #japan
    #   - mainland
    c.create_polygon(360,155, 367,153, 368,147, 370,147, 369,155, 362,157,
                     360,159, 358,159,
                     fill=land_color, outline=outline_color, tag=tag)
    #   - hokkaido
    c.create_polygon(368,145, 370,145, 370,143,
                     fill=land_color, outline=outline_color, tag=tag)
    
    #south america
    c.create_polygon( 90,260,  75,240,  80,210,  85,205, 100,210, 120,230,
                     140,240, 130,270, 110,300, 100,330,  90,300,
                     fill=land_color, outline=outline_color, tag=tag)
    #north america
    c.create_polygon( 60,200,  40,190,  30,165,  25,150,  30,135,  30,110,
                       5,113,  20, 95,  40, 90,  50, 95,  70, 90,  90, 95,
                     100,100,  80,110,  90,125, 105,105, 120,125, 100,140,
                      78,168,  75,175,  73,168,  60,164,  50,171,  55,193,
                      65,187,
                     fill=land_color, outline=outline_color, tag=tag)
    #greenland
    c.create_polygon(125, 80, 175, 75, 165, 95, 150,100, 140,110, 135,100,
                     140, 95, 135, 85,
                     fill=snow_color, outline=outline_color, tag=tag)
    #eurasia
    c.create_polygon(200,110, 220, 90, 235, 95, 265, 90, 290, 80, 350, 90,
                     385,100, 355,115, 360,140, 350,150, 355,175, 350,180,
                     335,180, 340,200, 335,210, 320,180, 300,195, 295,210,
                     285,180, 270,180, 250,200, 240,165, 240,155, 200,140,
                     178,155,
                     fill=land_color, outline=outline_color, tag=tag)
    #africa
    c.create_polygon(250,205, 260,203, 250,225, 245,250, 225,290, 210,295,
                     205,260, 200,220, 190,215, 175,220, 165,200, 165,180,
                     180,160, 200,155, 220,165, 240,180,
                     fill=land_color, outline=outline_color, tag=tag)
    #australia
    c.create_polygon(345,270, 375,250, 400,280, 375,305, 365,290, 345,295,
                     fill=land_color, outline=outline_color, tag=tag)


##c = Canvas(width=400, height=400, bg='white')
##c.pack(expand=YES, fill=BOTH)
##world=PhotoImage(file="WorldMap.gif")
##c.create_image(200,200, image=world)
##
##  # define parameters
##left = 0
##top = 0
##width = 400
##height = 400
##right = left + width
##bottom = top + height
##gridSize = 50
##linecolor = "black"
##
### draw vertical lines
##for x in range(width):
##    if x % gridSize == 0:
##        c.create_line(x,top, x,bottom, fill=linecolor, width=0.5)
##        c.create_text(x,top, text=str(x), anchor=NE, justify=RIGHT)
### draw horizontal lines
##for y in range(height):
##    if y % gridSize == 0:
##        c.create_line(left,y, right,y, fill=linecolor, width=0.5)
##        c.create_text(left+2,y, text=str(y), anchor=SW, justify=LEFT)
##
##
##world_map(c, tag="worldmap")
