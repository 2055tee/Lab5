class Transportation(object):
    """Abstract base class for all transportation methods"""

    def __init__(self, start, end, distance):
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

    def __init__(self, start, end, distance):
        Transportation.__init__(self, start, end, distance)

    def find_cost(self):
        return 0


class Taxi(Transportation):
    """Taxi class"""

    def __init__(self, start, end, distance):
        Transportation.__init__(self, start, end, distance)

    def find_cost(self):
        return 40 * self.distance


class Bus(Transportation):
    """Bus class"""

    def __init__(self, start, end, distance):
        Transportation.__init__(self, start, end, distance)

    def find_cost(self):
        return 13 * self.distance


class Train(Transportation):
    """Train class"""

    def __init__(self, start, end, distance, station):
        Transportation.__init__(self, start, end, distance)
        self.station = station

    def find_cost(self):
        return 5 * self.station


# main program
travel_cost = 0

trip = [
    Walk("KMITL", "KMITL SCB Bank", 0.6),
    Taxi("KMITL SCB Bank", "Ladkrabang Station", 5),
    Train("Ladkrabang Station", "Payathai Station", 40, 6),
    Taxi("Payathai Station", "The British Council", 3),
    Bus("The British Council", "Central World", 0.5),
]

for travel in trip:
    print(travel.start, "to", travel.end, ": ", end="")
    travel_cost += travel.find_cost()

print("\nTotal cost: " + str(travel_cost))
