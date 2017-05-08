############################################################
#                        Ice Cave                          #
#                                                          #
#       Programmed by Joe Welle (August 28, 2016)          #
#       Modified by Jean Flaherty (October 22, 2016)       #
#       Class: CG 120                                      #
#       Instructor: Dean Zeller                            #
#                                                          #
#       Description: Blue and Grey themed ice cave         #
#                                                          #
############################################################

from tkinter import *
##c = Canvas(width=400, height=400, bg="#081C19")
##c.pack(expand=YES, fill=BOTH)

def icecave_scenery(c):
    # background color
    c.create_rectangle(0,0, 500,500, fill="#081C19")
    
    #background ceiling
    c.create_polygon((0,67),(34,67),(20,120),(0,120), fill="#0B4D44") #4
    c.create_polygon((34,67),(20,120),(58,132), fill="#086155") #5
    c.create_polygon((0,120),(20,120),(20,140),(0,125), fill="#086155") #6
    c.create_polygon((20,120),(20,140),(41,126), fill="#0B7769") #7
    c.create_polygon((108,119),(120,82),(133,67),(133,125),(108,132), fill="#0B4D44") #31
    c.create_polygon((133,125),(160,135),(115,130), fill="#1E3E3A") #32
    c.create_polygon((133,125),(133,67),(175,67), fill="#235650") #49
    c.create_polygon((133,125),(175,67),(200,130),(160,135), fill="#0A3C36") #50
    c.create_polygon((175,67),(200,130),(245,67), fill="#10463F") #51
    c.create_polygon((200,130),(245,67),(290,80),(280,130), fill="#174640") #52
    c.create_polygon((280,130),(290,80),(301,140), fill="#1D433F") #53
    c.create_polygon((290,80),(320,75),(320,120),(299,132), fill="#184C46") #54
    c.create_polygon((320,120),(320,75),(366,70),(380,120), fill="#0F3E38") #55
    c.create_polygon((380,120),(366,70),(400,67),(400,94), fill="#184842") #56

    #background floor and stalagmite
    c.create_polygon((0,360),(0,289),(30,343), fill="#0A3C36") #65
    c.create_polygon((30,343),(0,289),(20,280),(50,314), fill="#086155") #66
    c.create_polygon((50,314),(20,280),(40,275),(56,290), fill="#184C46") #67
    c.create_polygon((20,280),(40,275),(22,250), fill="#174640") #68
    c.create_polygon((40,275),(22,250),(35,240), fill="#0B4D44") #69
    c.create_polygon((35,240),(22,250),(30,225), fill="#086155") #70
    c.create_polygon((110,290),(125,330),(170,290), fill="#184842") #71
    c.create_polygon((188,350),(125,330),(170,290),(190,292),(260,346), fill="#184842") #72
    c.create_polygon((190,292),(285,300),(285,344),(260,346), fill="#082320") #73
    c.create_polygon((285,300),(400,289),(344,344),(285,344), fill="#0F3E38") #74
    c.create_polygon((400,289),(344,344),(400,365), fill="#11342F") #75


    #foreground floor and stalagmite
    c.create_polygon((188,350),(267,345),(180,360), fill="#20BDA8") #57
    c.create_polygon((180,360),(222,352),(222,400),(150,400), fill="#38DAC4") #58
    c.create_polygon((222,400),(222,352),(267,345),(278,345),(278,400), fill="#28A897") #59
    c.create_polygon((278,345),(278,380),(300,345), fill="#099381") #60
    c.create_polygon((290,345),(344,344),(344,400),(278,400),(278,380), fill="#20BDA8") #61
    c.create_polygon((344,344),(400,365),(400,400),(344,400), fill="#12907F") #62
    c.create_polygon((267,345),(290,345),(270,314),(260,346), fill="#12907F") #63
    c.create_polygon((260,346),(270,314),(265,280), fill="#249989") #64

    #polygons on main column (general down movement, see reference sheet)
    c.create_polygon((0,0),(67,0),(67,34),(50,51), fill="#0FD6BB") #1
    c.create_polygon((0,0),(50,51),(33,67),(0,67), fill="#0EC4AB") #2
    c.create_polygon((34,67),(67,34),(67,76),(50,111), fill="#25BCA7") #3
    c.create_polygon((67,0),(133,0),(100,50),(80,34),(67,34), fill="#28A090") #8
    c.create_polygon((133,0),(188,0),(188,34),(175,67),(133,67),(113,30), fill="#3DE5D0") #9
    c.create_polygon((113,30),(133,67),(90,120),(90,65), fill="#099381") #10
    c.create_polygon((67,34),(80,34),(100,50),(90,65),(67,76), fill="#1DA895") #11
    c.create_polygon((67,76),(90,65),(90,120),(58,132),(50,111), fill="#0FD6BB") #12
    c.create_polygon((90,120),(100,145),(120,82), fill="#28A090") #13
    c.create_polygon((58,132),(90,120),(100,145),(65,170), fill="#25BCA7") #14
    c.create_polygon((100,145),(108,119),(110,180), fill="#086155") #15
    c.create_polygon((100,145),(65,170),(65,230),(90,190), fill="#3AE7D0") #16
    c.create_polygon((100,145),(90,190),(105,230),(110,180), fill="#0B7769") #17
    c.create_polygon((65,230),(90,190),(105,230),(90,245), fill="#28A090") #18
    c.create_polygon((65,230),(90,245),(90,260),(60,280), fill="#0FD6BB") #19
    c.create_polygon((90,245),(105,230),(105,250),(90,260), fill="#0B7769") #20
    c.create_polygon((105,250),(108,280),(95,270),(90,260), fill="#086155") #21
    c.create_polygon((60,280),(90,255),(95,270),(50,314), fill="#25BCA7") #22
    c.create_polygon((72,292),(95,270),(108,280),(110,290), fill="#28A090") #23
    c.create_polygon((30,343),(50,314),(72,292),(90,291),(70,343), fill="#3AE7D0") #24
    c.create_polygon((70,343),(90,291),(110,290),(125,330), fill="#0B7769") #25
    c.create_polygon((30,343),(70,343),(60,360),(0,360), fill="#1EBDA8") #26
    c.create_polygon((0,360),(60,360),(55,400),(0,400), fill="#3AE7D0") #27
    c.create_polygon((60,360),(70,343),(125,330),(100,350), fill="#099381") #28
    c.create_polygon((60,360),(100,350),(150,400),(55,400), fill="#0B7769") #29
    c.create_polygon((100,350),(125,330),(188,350),(150,400), fill="#086155") #30

    #foreground ceiling
    c.create_polygon((188,0),(244,0),(220,34),(188,34), fill="#20BDA8") #33
    c.create_polygon((188,34),(220,34),(245,50),(240,80),(175,67), fill="#38DAC4") #34
    c.create_polygon((245,50),(220,34),(231,17),(260,45), fill="#28A897") #35
    c.create_polygon((231,17),(243,0),(277,0),(250,35), fill="#249989") #36
    c.create_polygon((277,0),(280,45),(267,52),(250,35), fill="#31BFAC") #37
    c.create_polygon((277,0),(280,45),(290,80),(320,75),(300,20), fill="#099381") #38
    c.create_polygon((277,0),(300,20),(366,0), fill="#309E8F") #39
    c.create_polygon((300,20),(366,0),(366,70),(320,75), fill="#31BFAC") #40
    c.create_polygon((366,0),(366,70),(400,67),(400,0), fill="#12907F") #41

    #foreground stalactite
    c.create_polygon((240,80),(245,50),(260,45),(267,52),(250,85), fill="#2B9385") #42
    c.create_polygon((267,52),(280,45),(290,80),(275,85), fill="#3DE5D0") #43
    c.create_polygon((250,85),(267,52),(275,85),(275,95),(255,95), fill="#20BDA8") #44
    c.create_polygon((275,95),(255,95),(273,105), fill="#38DAC4") #45
    c.create_polygon((255,95),(273,105),(260,115), fill="#3B9186") #46
    c.create_polygon((273,105),(260,115),(269,130), fill="#20BDA8") #47
    c.create_polygon((260,115),(269,130),(265,145), fill="#2D7A70") #48








    #border
    c.create_rectangle((5,5),(400,400), width=10)









