###########################################################################
#                                Animation                                #
#                                                                         #
#   Programmed by Jean Flaherty (11-17-2016)                              #
#   Instructor:  Dean Zeller                                              #
#   Description:  The Animation class handels starting and stoping        #
#                 animations. All animations that use this object will    #
#                 be canceled whan a new animation starts.                #
#                                                                         #
#   Parameters:                                                           #
#           canvas         Canvas to draw the picture                     #
#           fpms            Frames per second                              #
#           frame_count    Number of frames in the animation              #
#           reset          A function that resets the animation. The      #
#                          function should handle any repositioning or    #
#                          resetting any properties so that the animation #
#                          can be replayed.                               #
#           timeline       A function that makes incremental changes to   #
#                          the object you are animating. The function     #
#                          should take one parameter that represents the  #
#                          current frame number (iteration of animation   #
#                          loop) and handle any repositioning or setting  #
#                          properties. Think of this function as the      #
#                          inside of a for loop.                          # 
#           completion     A function that gets called when the animation #
#                          is complete.                                   #
#                                                                         #
###########################################################################

from tkinter import *
import datetime

class Animation:
    # inititalize
    def __init__ (self, canvas, fpms=1000/30, frame_count=0, reset=None, timeline=None, completion=None):
        self.reset = reset
        self.timeline = timeline
        self.fpms = fpms
        self.frame_count = frame_count
        self.frame = 0
        self.canvas = canvas
        self.completion = completion
        self._start_time = datetime.datetime(1, 1, 1, 0, 0) # didn't start yet

    # animation stopping is handled on a class level. class variable
    _stop_time = datetime.datetime(1, 1, 1, 0, 0)

    # will stop all current animations. We want this on the class level.
    @classmethod
    def stop(self):
        Animation._stop_time = datetime.datetime.now()

    # returns true if stop was called after the animation started
    def _shouldStop(self):
        # compare times
        return self._start_time < Animation._stop_time

    # play this animation
    def play(self):
        if self.reset: self.reset() # reset animation
        self.frame = 0 # reset frame number
        Animation.stop() # stop any animations before continuing
        self._start_time = datetime.datetime.now() # uptate to current time
        
        for frame in range(self.frame, self.frame_count):
            # update frame
            self.canvas.after(int(self.fpms))
            self.canvas.update()

            # if any interuptions occur, loop will pause here and will continue
            # after completing new task (usually happens when animation is
            # requested to end)
            # check if stop() was called after current animation started
            # if so, we don't want to continue this loop
            
            if self._shouldStop():
                print("Animation cancelled")
                break
            self.frame = frame

            # user set timeline
            if self.timeline: self.timeline(frame)

            # if last frame
            if frame == self.frame_count-1:
                # call the competion handler
                if self.completion: self.completion()
