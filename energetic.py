#-----------------------------------------------
# Energetics class that defines the type
# of energetic, and the radius of influence
#
# Author: Jeremiah Casuga
# ----------------------------------------------

class Energetics:
    '''
    Energetics class that stores the name and radius of influence
    of a given energetic

        Parameters:
            energetics (dict): list of energetics and corresponding ROI
    '''
    def __init__(self, energetics):
        self.energetics = energetics

    def get_energetics(self):
        '''
        Returns the current list of energetics

            Returns:
            self.energetics: current list of energetics
        '''
        return self.energetics
    
    def add_energetics(self, name):
        '''
        Adds an energetic to the existing list of energetics

            Parameters:
                name (dict): name of energetic to be added
            
            Returns:
                self.energetics: new dictionary with added energetic
        '''
        # Check if energetic being added is valid
        if len(name) != 2: 
            print("This is not a valid energetic")
        else:
            self.energetics[name[0]] = name[1]
            return self.energetics
        

if __name__ == '__main__':
    list = {
        "A4":2,
        "S4":3
    }
    ener = Energetics(list)
    print(ener.get_energetics())
    print(ener.add_energetics(["C6", 4]))