import random

class Logic:
    def __init__(self): 
        pass

    # returns random value min and max (int)
    def random_number(self, min = 0, max = 1):
        if max > min:
            return random.randint(min, max)
        else:
            return 0