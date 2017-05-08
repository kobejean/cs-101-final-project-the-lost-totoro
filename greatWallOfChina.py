########################################################################
#                       The Great Wall of China                        #
#                                                                      #
#   Programmed by Kassan Qian                                          #
#   Modified by Jean Flaherty (11/30/16)                               #
#   Instructor: Dean Zeller                                            #
#                                                                      #
#   Description: This is a picture of the Great Wall of China.         #
#                                                                      #
########################################################################
from tkinter import *

def greatwall(c, tag="greatwall"):
    #c.create_image(0,0, anchor=NW, image=wall)

    #sky
    c.create_rectangle(0,0, 960,600, fill='lightcyan2', tag=tag)

    #Hills/Greenery
    c.create_polygon(0,145, 0,145, 310,70, 310,70,
                     340,65, 340,65, 375,75,
                     950,165, 950,165,
                     950,594, 950,594, 0,594, 0,594,
                     0,294, 0,294,
                     fill='chartreuse4', outline='black', smooth=1, tag=tag)

    c.create_line(430,310, 495,290, 550,215, 620,175, smooth=1, tag=tag)


    #DARK GREEN MOUNTAIN
    c.create_polygon(0,145, 0,145, 40,130, 155,60, 165,65, 165,65, 200,50, 230,60, 230,60, #start of building
                     310,75, 310,75, 200,150, 100,200, 0,245, 0,245, smooth=1, fill='forestgreen',
                     outline='black', tag=tag)
    #BACK BLUE MOUNTAIN
    c.create_polygon(400,77, 400,77,
                     425,70, 445,65,
                     465,62, 495,55, 500,55, #peak
                     540,75, 550,77, 575,79,
                     580,80, 600,78, 620,80,
                     649,95, 649,95, 665,80, 665,80,
                     695,95, 735,80, 735,80, 750,90,
                     760,90, 800,92, 850,100, 850,100,
                     915,125, 940,120, 950,124, #end
                     950,165, 950,165, 900,145, 900,145,
                     637,149, 637,149, 620,140,
                     580,135, 580,135, 550,150, 550,150, 400,77,
                     fill='darkslategray4', outline='black', smooth=1, tag=tag)
    #BACK MOUNTAIN 2
    c.create_polygon(380,78, 380,78,
                     390,75, 390,75, 400,75, 400,75,
                     450,100, 550,150,
                     580,135, 580,135, 620,140, 620,140,
                     637,149, 637,149,
                     900,145, 900,145, 950,165, 950,165,
                     850,149, 850,149, #last point on right before going back
                     637,170, 637,170,
                     600,180, 
                     520,152, 520,152, 
                     450,125, 377,75, 380,78,
                     fill='aquamarine4', outline='black', smooth=1, tag=tag)
                     

    #LEFT BRICK 1
    c.create_polygon(0,262, 80,252, 142,292, 148,315, 148,594, 0,594, 0,260,
                     fill='bisque3', outline='black', tag=tag)
    c.create_polygon(0,262, 80,252, 142,292, 0,315, fill='bisque4',
                     outline='black', tag=tag) #top

    #c.create_line(0,345, 150,315)
    

    #LEFT BRICK 2
    c.create_polygon(150,470, 315,400, 355,425, 355,594, 150,594, 150,470,
                     fill='bisque3', outline='black', tag=tag)
    c.create_polygon(150,470, 315,400, 355,425, 150,540,
                     fill='bisque4', outline='black', tag=tag)

    #LEFT BRICK 3
    c.create_polygon(355,505, 375,490, 410,480, 440,500, 440,594, 355,594, 355,505,
                     fill='bisque3', outline='black', tag=tag)
    c.create_polygon(355,505, 375,490, 410,480, 440,500,
                     440,515, 355,594, 355,505, fill='bisque4', outline='black', tag=tag)
   
    

     #BUILDING
    c.create_polygon(765,255, 635,252, 635,115, 820,115, 820,280,
                     765,255, fill='navajowhite4', outline='black', tag=tag) #front
        #795,277, 780,180, 770,180, 765,190, 768,225,
        #715,220, 720,210,705,120, 705,175, 700,170,
    c.create_polygon(820,115, 850,105, 850,255, 820,280, 820,115,
                     fill='bisque3', outline='black', tag=tag) #right side
    c.create_polygon(635,115, 700,105, 850,105, 820,115, 635,115,
                     fill='bisque3', outline='black', tag=tag) #top
    #Brown Lines
    c.create_line(635,150, 820,150, 850,137, fill='saddle brown', width=3, tag=tag)
    #Doors
    c.create_polygon(740,223, 740,223, 740,200, 742,197, 747,193, 750,190,
                     752,193, 757,197, 760,200, 760,225, 760,225, 740,223,
                     740,223, fill='black', outline='black', smooth=1, tag=tag) #right
    c.create_polygon(650,217, 650,217, 650,200, 652,195, 660,190, 668,195,
                     670,200, 670,217, 670,217, 650,217, 650,217, tag=tag) #left
    
    

    #Long Stretch (Left)
    c.create_polygon(440,500, 440,500, 510,455, 570,400, 645,295,
                     660,265, 698,175, 698,175, 701,170, 701,170,
                     705,175, 705,175, 700,200, 680,250, 660,300,
                     650,320, 630,350, 570,425, 470,510, 470,510,
                     440,500, 440,500, fill='bisque3',
                     outline='black', width=1, smooth=1, tag=tag) #top strip
    
    c.create_polygon(705,175, 705,175, 704,210, 704,210, 700,220, 675,300, 650,370,
                     605,465, 545,594, 545,594, 470,594, 470,594, 470,510, 470,510,
                     570,425, 630,350, 650,320, 660,300, 700,200, 705,175, 705,175,
                     fill='bisque3', outline='black', smooth=1, tag=tag) #bottom
                  
                     #440,500, #480,495, 480,495, 
                     #440,500, 510,455, 570,400, 645,295,
                     #660,265, 698,175, 698,175, 701,170, 701,170,
                     #705,175, 705,175, fill='', outline='black', smooth=1) #bottom
    c.create_polygon(440,500, 470,510, 470,594, 440,594, 440,500,
                     fill='bisque3', outline='black', tag=tag) #left upright strip

                     #700,220, 675,300, 650,370,
                     #605,465, 545,594, 545,594, 440,594, 440,594, 440,500, #480,495, 480,495, 
                     #440,500, fill='', outline='black', smooth=1) #left
    #c.create_rectangle(470,510, 470.2,594) #left upright strip

    #Long Stretch (Right)
    c.create_polygon(820,594, 820,594, 805,550, 795,500, 785,400, 778,350, 775,300,  
                     765,200, 770,180, 770,180, 778,250, 785,350, 795,400,
                     810,450, 835,500, 860,550, 900,594, 900,594, 820,594, 820,594, 
                     fill='bisque3', outline='black', smooth=1, tag=tag) #left strip

    c.create_polygon(900,594, 900,594, 860,550, 835,500, 810,450, 795,400, 785,350,
                     778,250, 770,180, 770,180, 780,180, 780,180, 784,200, 790,250,
                     800,300, 808,350, 825,400, 855,450, 885,500, 925,550, 956,594,
                     956,594, 900,594, 900,594,
                     fill='bisque3', outline='black', smooth=1, tag=tag) #top strip

    #Pathway
    c.create_polygon(545,594, 545,594, 605,465, 650,370, 675,300,  700,220,
                     704,210, 704,210, 720,210, 720,210, 715,220, 715,220,
                     768,225, 768,225, 775,300, 778,350, 785,400, 795,500,
                     805,550, 820,594, 820,594, 545,594, 545,594,
                     fill='bisque4', outline='black', smooth=1, tag=tag)

    #Back Paths
    c.create_polygon(230,55, 230,55, 249,55, 249,55, 300,60, 300,60,
                     310,65, 310,65, 310,75, 310,75, #tiny drop
                     320,77, 320,77, 330,85, 330,85, 333,85, 333,85,
                     303,100, 310,120, 350,135, 400,140, #gap
                     420,142, 430,135, 450,135, 500,140, 500,140,
                     520,140, 520,140, 520,165, 520,165, 550,185, 550,185, #end
                     545,200, 545,200, 500,190, 450,160, 415,150, 400,150,
                     350,148, 320,145, 300,140, 270,120, 270,120,
                     270,105, 270,105, 290,105, 290,100, 305,80,
                     230,60, 230,60, 230,55, 230,55,
                     fill='bisque4', outline='black', smooth=1, tag=tag)
    #back path right
    c.create_polygon(333,85, 333,85, 350,97, 350,97, 360,85, 
                     349,75, 349,75, 349,70, 349,70, 367,70, 367,70,
                     367,80, 367,80, 370,85, 365,100, 365,100,
                     350,100, 350,100, fill='bisque4',
                     outline='black', smooth=1, tag=tag)
        
                     #350,100, 331,85, 331,85, 

    
      # define parameters
##    left = 0
##    top = 0
##    width = 1000
##    height = 800
##    right = left + width
##    bottom = top + height
##    gridSize = 50
##    linecolor = "black"

    # draw vertical lines
##    for x in range(width):
##        if x % gridSize == 0:
##            c.create_line(x,top, x,bottom, fill=linecolor, width=2)
##            c.create_text(x,top, text=str(x), anchor=NE, justify=RIGHT)
    # draw horizontal lines
##    for y in range(height):
##        if y % gridSize == 0:
##            c.create_line(left,y, right,y, fill=linecolor, width=2)
##            c.create_text(left+2,y, text=str(y), anchor=SW, justify=LEFT)


  
##c = Canvas(width=1000, height=800, bg='lightblue1')
##c.pack(expand=YES, fill=BOTH)
###wall=PhotoImage(file="greatwallofchina2.gif")
##
##greatwall(c)

##greatwall(c, tag="scene") #calling the function
##
##c.scale("scene", 0, 0, 400/960, 400/600)

