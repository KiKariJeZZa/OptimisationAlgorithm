#-----------------------------------------------
# Energetics class that defines the type
# of energetic, and the radius of influence
#
# Author: Jeremiah Casuga
# ----------------------------------------------

class Energetic:
    def __init__(self, name, roi):
        self.name = name
        self.roi = roi

    def get_name(self):
        return self.name
    
    def get_roi(self):
        return self.roi

    