import math


class rectPrism:

    def __init__(self,l, w, h):
        
        # note you will need to specify more input parameters
        if l <= 0 or w <= 0 or h <= 0:
            print("Error: Dimensions must be positive numbers.")
            self.length = self.width = self.height = None
        else:
            self.length = l
            self.width = w
            self.height = h
        pass

    def volume(self):
        if self.width == None or self.height == None or self.length == None:
            return None
        b = self.width * self.height * self.length
        print(b)
        
        return b
    
    def surfaceArea(self):
        if self.width == None or self.height == None or self.length == None:
            return None
        answer = (self.width * self.length) + (self.height * self.length) + (self.width * self.height)
        x = answer * 2
        print(x)
        return x
#2(wl+hl+hw)

# class instances and assertions below:

a = rectPrism(l=10,w=2,h=5)
assert a.volume() == 100
assert a.surfaceArea() == 160

b = rectPrism(l=1,w=1,h=1)
assert b.volume() == 1
assert b.surfaceArea() == 6

c = rectPrism(l=2,w=0,h=10)
# note the invalid width
assert c.volume() == None
assert c.surfaceArea() == None