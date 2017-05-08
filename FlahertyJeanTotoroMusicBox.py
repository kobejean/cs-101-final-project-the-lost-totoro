###########################################################################
#                            Totoro Music Box                             #
#                                                                         #
#  Programmed by Jean Flaherty (12-03-2016)                               #
#                                                                         #
#  Handles Music playing.                                                 #
#                                                                         #
#  MUSIC by Jean Flaherty                                                  #
#   Sampo                                                                 #
#   Mei is Missing                                                        #
#   The Path of the Wind                                                  #
#   Totoro                                                                #
#   Mother                                                                #
#                                                                         #
#  This program is copyright (c) 2016 Jean Flaherty and Dean Zeller.      #
#  All rights reserved.  Permission granted to use and modify for         #
#  educational purposes only.  Any commercial use of this code must       #
#  receive permission from the author(s).                                 #
###########################################################################

from enum import Enum

# mac does't support winsound
try:
    import winsound
except ImportError:
    print("Music will not play on this system.")

###########################################################################
# TotoroMusicTheme: Represents the tracks                                 #
###########################################################################
class TotoroMusicTheme(Enum):
    NONE = 0
    SAMPO = 1
    MEI_IS_MISSING = 2
    THE_PATH_OF_THE_WIND = 3
    TOTORO = 4
    MOTHER = 5

    # this allows the class to support str() converting
    def __str__(self):
        if self == TotoroMusicTheme.NONE:
            return ""
        elif self == TotoroMusicTheme.SAMPO:
            return "Sampo"
        elif self == TotoroMusicTheme.MEI_IS_MISSING:
            return "Mei is Missing"
        elif self == TotoroMusicTheme.THE_PATH_OF_THE_WIND:
            return "The Path of the Wind"
        elif self == TotoroMusicTheme.TOTORO:
            return "Totoro"
        elif self == TotoroMusicTheme.MOTHER:
            return "Mother"

###########################################################################
# TotoroMusicBox: Handels music playing                                   #
###########################################################################
class TotoroMusicBox:
    def __init__(self):
        self.theme = TotoroMusicTheme.NONE
        
    _theme = TotoroMusicTheme.NONE
    @property
    def theme(self):
        return self._theme

    @theme.setter
    def theme(self, newTheme):
        if not newTheme == self.theme:
            try:
                winsound.PlaySound(None, winsound.SND_ASYNC)
            except:
                print("Error trying to stop music")
            #winsound.PlaySound(None, winsound.SND_ASYNC)
            if not newTheme == TotoroMusicTheme.NONE:
                filename = "{}.wav".format(newTheme)
                try:
                    winsound.PlaySound(filename, winsound.SND_ASYNC)
                except:
                    print("Error trying to play music file: {}".format(filename))
            self._theme = newTheme
    
    
