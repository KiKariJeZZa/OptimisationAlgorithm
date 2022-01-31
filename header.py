#-----------------------------------------------
# Header class defining the size of the header
# required to mine
#
# Author: Jeremiah Casuga
# ----------------------------------------------

class Header:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height