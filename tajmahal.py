########################################################################
#                             Tajmahal                                 #
#                                                                      #
#   Programmed by Kassan Qian                                          #
#   Modified by Jean Flaherty (11/30/16)                               #
#   Instructor: Dean Zeller                                            #
#                                                                      #
#   Description: This is a picture of Tajmahal.                        #
#                                                                      #
########################################################################
from tkinter import *

def tajmahal(c, tag="tajmahal"):
    c.create_rectangle(0,0, 945,600, fill="light blue", tag=tag)
    #backwhite
    c.create_rectangle(261,400, 696,436, fill='floral white', tag=tag)
    #strips between side frames
    #left
    c.create_rectangle(305,267, 310,436, fill='floral white', outline='', tag=tag)
    #right
    c.create_rectangle(649,265, 655,436, fill='floral white', outline='', tag=tag)

    #LEFT AND RIGHT POLES
    botLeftx=15
    botLefty=435 #370

    topLeftx=40
    topLefty=148 #120

    topRightx=75
    topRighty=149 #123

    botRightx=75
    botRighty=435 #370

    c.create_polygon(15,435, 15,435, 21,350, 21,350, 10,345, 21,340, 21,340, #left bulge
                     27,250, 27,250, 13,245, 27,240, 27,240, #left bulge 2
                     34,148, 34,148, 27,143, 40,138, #left bulge 3
                     75,138, 75,138, 80,143, 75,148, 75,148, #right bulge 1
                     75,240, 75,240, 85,245, 75,250, 75,250, #right bulge 2
                     75,340, 75,340, 85,345, 75,350, 75,350, #right bulge 3
                     75,435, 75,435, 15,435, 15,435, smooth=1,
                     fill='floral white', outline='black', tag=tag) #left

    c.create_polygon(876,435, 876,435, 876,349, 876,349, 865,345, #left bulge 1
                     876,340, 876,340, 876,252, 876,252, 865,245, #left bulge 2
                     876,240, 876,240, 876,150, 876,150, 865,145, #left bulge 2
                     876,140, 876,140, 920,140, 920,140, 925,145, #right bulge 1
                     920,150, 920,150, 925,240, 925,240, 935,245, #right bulge 2
                     927,252, 927,252, 932,340, 932,340, 940,345, #right bulge 3
                     932,349, 932,349, 937,436, 937,436, 876,436, 876,436,
                     fill='floral white', outline='black', smooth=1, tag=tag) #right
    #c.create_polygon(botLeftx+861,botLefty, topLeftx+836,topLefty+2,
                     #topRightx+840,topRighty+1, botRightx+865,435,
                     #fill='floral white', outline='black') #right
    #LEFT GROOVES
    #c.create_oval(10,335, 85,350, fill='floral white', outline='black') #1
    #c.create_oval(22,235, 83,250, fill='floral white', outline='black') #2
    #c.create_arc(32,145, 80,145, start=0, extent=180, style=ARC, width=5,
                 #fill='floral white', outline='black') #3
    #c.create_arc(10,340, 85,340, start=0, extent=180, style=ARC, width=10) #1
    #c.create_arc(22,235, 80,235, start=0, extent=180, style=ARC, width=10) #2
    #c.create_oval(32,145, 80,155, fill='black') #3

    #RIGHT GROOVES
    #c.create_oval(865,335, 943,350, fill='floral white', outline='black') #1
    #c.create_oval(865,240, 933,255, fill='floral white', outline='black') #2
    #c.create_arc(870,145,  920,145, start=0, extent=180, style=ARC, width=10,
                 #fill='floral white', outline='black') #3
    #c.create_arc(865,335, 940,340, start=0, extent=180, style=ARC, width=10) #1
    #c.create_arc(865,240, 930,245, start=0, extent=180, style=ARC, width=10) #2 

    #LEFT POLE DOME
    c.create_polygon(40,143, 40,143, 45,105, 55,109,
                     74,107, 74,143, 74,143,
                     fill='floral white', smooth=1, outline='black', tag=tag)
    c.create_polygon(45,110, 45,110, 35,100, 35,100, 45,97, 45,97,
                     47,80, 58,75, 60,60, 60,60, 62,75, 73,80, 76,97, 76,97,
                     85,100, 85,100, 70,110, 70,110,
                     fill='floral white', smooth=1, outline='black', tag=tag) #top
    #RIGHT POLE DOME
    c.create_polygon(877,143, 877,143, 877,115, 895,105,
                     910,115, 914,143, 914,143,
                     fill='floral white', smooth=1, outline='black', tag=tag)
    c.create_polygon(877,118, 877,118, 863,108, 863,108, 876, 100, 876,100,
                     877,90, 893,75, 895,60, 895,60, 897,75, 908,90,
                     908,100, 908,100, 918,108, 918,108, 910,118, 910,118,
                     fill='floral white', smooth=1, outline='black', tag=tag)

    #910,102, 910,102, 909,110, 909,110,

    #SMALLER POLES\
    c.create_polygon(202,436, 202,436, 205,400, 205,400, 200,395, 207,390, 207,390, #LB1
                     210,340, 210,340, 206,335, 212,332, 212,332, #LB2
                     215,275, 215,275, 211,270, 217,268, 217,268, #LB3
                     235,268, 239,272, 235,275, 235,275, #RB1
                     235,333, 235,333, 240,338, 235,341, 235,341, #RB2
                     235,392, 235,392, 240,398, 235,400, 235,400, #RB3
                     235,436, 235,436, 202,436, 202,436, fill='floral white', outline='black',
                     smooth=1, tag=tag) #left
    c.create_polygon(720,436, 720,436, 720,400, 720,400, 715,397, 720,394, 720,394, #LB1
                     720,345, 720,345, 715,342, 720,339, 720,339, #LB2
                     720,275, 720,275, 715,272, 720,269, 720,269, #LB3
                     740,269, 745,272, 740,275, 740,275, #RB1
                     745,339, 745,339, 750,343, 747,345, 747,345, #RB2
                     749,393, 749,393, 755,396, 749,399, 749,399, #RB3
                     751,436, 751,436, 720,436, 720,436, fill='floral white', outline='black',
                     smooth=1, tag=tag) #right
                     
                    
    #c.create_polygon(215,275, 235,275, 235,430, 203,430,
                     #fill='floral white', outline='black') #left
   # c.create_polygon(720,275, 740,275, 750,430, 720,430,
                     #fill='floral white', outline='black') #right
    #Left
    #Grooves
    #c.create_oval(200,390, 240,400, fill='floral white', outline='black') #bottom to top
    #c.create_oval(205,330, 240,340, fill='floral white', outline='black')
    #c.create_oval(210,270, 240,276, fill='floral white', outline='black')
    #Domes
    c.create_polygon(215,272, 215,272, 217,254, 217,254, 205,250, 205,250,
                  215,245, 215,245, 217,235, 224,230, 226,218, 228,230,
                  235,235, 235,245, 235,245, 245,250, 245,250,
                  235,254, 235,254, 235,272, 235,272,
                     fill='floral white', smooth=1, outline='black', tag=tag)
    #Right
    #Grooves
    #c.create_oval(715,390, 753,400, fill='floral white', outline='black')
    #c.create_oval(715,335, 750,345, fill='floral white', outline='black')
    #c.create_oval(715,271, 744,279, fill='floral white', outline='black')
    #Domes
    c.create_polygon(720,273, 720,273, 720,254, 720,254, 708,250, 708,250,
                     720,245, 720,245, 720,235, 727,230, 729,218, 731,230,
                     738,235, 739,245, 739,245, 750,250, 750,250,
                     740,254, 740,254, 740,273, 740,273,
                     fill='floral white', smooth=1, outline='black', tag=tag)



    #INFRASTUCTURE
    #bottom rectangle (from bottom line, not including strip between center rect.)
    c.create_rectangle(botLeftx-10,botRighty, botLeftx+930,botLefty+45, fill='floral white', tag=tag)
    #strip above rectangle
    c.create_rectangle(15,430, 945,435, fill='floral white', outline='black', tag=tag)
    #center rectangle (measured inside of round poles, not including little strip on top)
    c.create_rectangle(390,230, 565,425, fill='floral white', outline='black', tag=tag)



    leftX1=310
    leftY1=263
    leftX2=385
    leftY2=427
    #LEFT RECTANGLE (inside poles)
    c.create_rectangle(leftX1,leftY1, leftX2, leftY2, fill='floral white', outline='black', tag=tag)
    #2frames
    c.create_rectangle(320,270, 375,348, fill='old lace', outline='black', tag=tag) #top
    c.create_rectangle(320,348, 375,425, fill='old lace', outline='black', tag=tag) #bottom
    #2doors
    c.create_polygon(320,348, 320,348, 320,290, 348,275, 348,275,
                     375,290, 375,348, 375,348,
                     fill='antique white', smooth=1, outline='black', tag=tag) #top
    c.create_polygon(320,425, 320,425, 320,367, 348,353, 348,353,
                     375,367, 375,425, 375,425, smooth=1,
                     fill='antique white', outline='black', tag=tag) #bottom
    #RIGHT RECTANGLE
    c.create_rectangle(leftX1+260, leftY1+2, leftX2+264, leftY2,
                       fill='floral white', outline='black', tag=tag)
    #2frames
    c.create_rectangle(580,275, 638,348, fill='old lace', outline='black', tag=tag) #top
    c.create_rectangle(580,348, 638,425, fill='old lace', outline='black', tag=tag) #bottom
    #2doors
    c.create_polygon(580,348, 580,348, 580,295, 610,280, 610,280,
                    638,295, 638,348, 638,348,
                     smooth=1, fill='antique white', outline='black', tag=tag) #top
    c.create_polygon(580,425, 580,425, 580,367, 610,353, 610,353,
                     638,367, 638,425, 638,425, smooth=1,
                     fill='antique white', outline='black', tag=tag) #bottom

    #left slanted rectangle
    #c.create_polygon(250,230, 255,276, 302,254, 300,430)
    c.create_polygon(260,275, 306,270, 305,428, 260,428, fill='floral white',
                     outline='', tag=tag)
    #2 frames
    c.create_polygon(265,280, 301,276, 301,348, 265,353, fill='old lace',
                     outline='black', tag=tag) #top
    c.create_polygon(265,358, 301,353, 301,420, 265, 420, fill='old lace',
                     outline='black', tag=tag) #bottom
    #2 doors
    c.create_polygon(265,353, 265,353, 265,300, 283,280, 283,280,
                     300,295, 300,348, 300,348,
                     smooth=1, fill='antique white', outline='black', tag=tag) #top
    c.create_polygon(265,420, 265,420, 265,373, 283,356, 283,356,
                     300,367, 300,420, 300,420,
                     smooth=1, fill='antique white', outline='black', tag=tag) #bottom
    #right slanted rectangle
    c.create_polygon(654,265, 697,275, 697,428, 654,428, fill='floral white',
                     outline='', tag=tag)
    #2 frames
    c.create_polygon(659,273, 692,280, 692,353, 659,348, fill='old lace',
                     outline='black', tag=tag) #top
    c.create_polygon(659,353, 692,358, 692,420, 659,420, fill='old lace',
                     outline='black', tag=tag) #bottom
    #2 doors
    c.create_polygon(659,348, 659,348, 659,295, 675,280, 675,280,
                     692,300, 692,353, 692,353,
                     smooth=1, fill='antique white', outline='black', tag=tag) #top
    c.create_polygon(659,420, 659,420, 659,370, 675,358, 675,358,
                     692,371, 692,420, 692,420,
                     smooth=1, fill='antique white', outline='black', tag=tag) #bottom



    #DOME STUFF
    #TOP DOME
    #c.create_polygon(390,230, 380,185, 380,150, 400,115, 440, 90, 455,70,
                     #475,50, 475,50, 500,70, 560,120, 570,150, 570,200, 565,230)
    centerx=475
    c.create_polygon(centerx-85,230, centerx-95,185, centerx-95,150, centerx-75,115,
                     centerx-35,85, 460,60, 475,40, 475,40, 490,60,
                     centerx+35,85, centerx+75,115,
                     centerx+95,150, centerx+95,185, centerx+85,230, smooth=1,
                     fill='floral white', outline='black', tag=tag)
    #spire
    c.create_polygon(468,50, 468,50, 475,38, 475,38,
                     471,35, 474,30, 474,30,
                     470,25, 472,20, #472,20,
                     475,5, 475,5, 478,20, 478,20, 480,25, 480,25,
                     475,30, 475,30, 480,35, 477,38, 477,38,
                     483,50, 483,50, smooth=1, fill='darkgoldenrod', tag=tag)


                     #470,40, 470,40,
                     #465,35, 470,30, 470,30,
                     #465,25, 470,20, 470,20,
                     #475,5, 475,5, 480,20, 480,20,
                     #475,)
    #arc line 1
    c.create_line(450,73, 475,63, 500,73, smooth=1, tag=tag)
    #arc line 2
    #.create_line(390,205, 475,160, 565,205, smooth=1)

    #arc under top dome
    c.create_arc(307,200, 643,650, start=60, extent=60,
                 style=CHORD, fill='floral white', outline='black', tag=tag)

    #left strip
    c.create_rectangle(385,205, 390,425, fill='floral white', outline='black', tag=tag)
    #right strip
    c.create_rectangle(385+180,205, 390+180,425, fill='floral white', outline='black', tag=tag)
    #main door
    c.create_polygon(420,425, 420,425, 420,300, 475,275, 475,275,
                     535,300, 535,425, 535,425,
                     smooth=1, fill='old lace', outline='black', tag=tag)

    #2 frames around door
    c.create_rectangle(415,260, 540,425, fill='', outline='black', tag=tag) #outer
    c.create_rectangle(415+5,260+5, 540-5,425, fill='', outline='black', tag=tag) #inner
    #425,323, , 505,425


    #LEFT DOME
    c.create_polygon(325,264, 325,264, 325,242, 325,242,
                     320,240, 320,240, 315,235, 315,235, #outersharppoint
                     325,230, 325,230, 329,216, 345,202,
                     353,197, 353,197, 354,167, 355,197, #rightpointoftopspire
                     355,197, 370,205, 385,216, #385,204,
                     385,264, 385,264, 325,264, 325,264,
                     smooth=1, fill='floral white', outline='black', tag=tag)
                     
    #RIGHT DOME
    c.create_polygon(570,265, 570,265, 570,225, 575,210,
                    598,197, 598,197, 600,167, 602,197, 602,197,
                     620,210, #curve on right
                     625,220, 625,225, 635,230, 635,230, 630,235, 625,235,
                     625,265, 625,265, 570,265, 570,265, smooth=1,
                     fill='floral white', outline='black', tag=tag)

    #weird red rectangle thing above the pathway
    c.create_rectangle(5,480, 945,500, fill='indianred4', tag=tag)

    #PATHWAY (brick shadow included in trapezoid)
    c.create_polygon(450,500, 500,500, 645,600, 305,600, fill='lightsteelblue1', tag=tag)
    #left brick
    c.create_polygon(400,500, 450,500, 305,600,200,600, fill='indianred4', tag=tag)
    #right brick
    c.create_polygon(500,500, 550,500, 750,600, 645,600, fill='indianred4', tag=tag)
    #left grass
    c.create_polygon(5,500, 400,500, 200,600, 5,600, 5,500, fill='forest green', tag=tag)
    #right grass
    c.create_polygon(550,500, 945,500, 945,600, 750,600,550,500, fill='forest green', tag=tag)



##c = Canvas(width=1000, height=800, bg='white')
##c.pack(expand=YES, fill=BOTH)
##
##tajmahal(c, tag="scene") #calling the function
##
##c.scale("scene", 0, 0, 400/945, 400/600)
