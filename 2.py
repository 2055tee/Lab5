class Transportation(object):
    """Abstract base class for all transportation methods"""
    def __init__(self,start,end,distance):
        if self.__class__ == Transportation:
            raise NotImplementedError
        self.start = start
        self.end = end
        self.distance = distance
    
    def find_cost(self):
        """Abstract method; derived classes must override"""
        raise NotImplementedError

    
class Walk(Transportation):
    """Walk class"""
    def __init__(self,start,end,distance):
        Transportation.__init__(self,start,end,distance)
    
    def find_cost(self):
        print("Walk from " + self.start + " to " + self.end + ". Cost: 0")
    
#main program
travel_cost = 0

trip = [Walk("KMITL","KMITL SCB Bank",0.6)]

for travel in trip:
    travel.find_cost()
