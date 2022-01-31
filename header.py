#-----------------------------------------------
# Header class defining the size of the header
# required to mine
#
# Author: Jeremiah Casuga
# ----------------------------------------------

class Header:
    def __init__(self, header):
        self.header = header
        
    def get_header(self):
        return self.header
    
    def add_header(self, name):
        # Check if energetic being added is valid
        if len(name) != 2: 
            print("This is not a valid energetic")
        else:
            self.energetics[name[0]] = name[1]
            return self.energetics
