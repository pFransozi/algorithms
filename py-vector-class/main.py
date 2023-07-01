import math

class Vector:

    def __init__(self, x = 0, y = 0):

        self.x = x
        self.y = y

    # get the string representation of the object for inspection. 
    # Without that implementation python displays <Vector object at 0x10e100070>
    # __repr__ goal is to be unambiguous
    # __str__ goal is to be readable
    # If you only implement one of these special methods in Python, choose __repr__.
    # Sometimes same string returned by __repr__ is user-friendly, and you
    #don’t need to code __str__ because the implementation inherited from
    #the object class calls __repr__ as a fallback.
    def __repr__(self):
        return f"Vector({self.x!r}, {self.y!r})" # !r gets the standard representation of the attributes to be displayed.
    
    def __abs__(self):
        return math.hypot(self.x, self.y)
    
    #     By default, instances of user-defined classes are considered truthy, unless
    # either __bool__ or __len__ is implemented. Basically, bool(x) calls
    # x.__bool__() and uses the result. If __bool__ is not implemented,
    # Python tries to invoke x.__len__(), and if that returns zero, bool
    # returns False. Otherwise bool returns True.
    def __bool__(self):
        return bool(abs(self))
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y

        return Vector(x, y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)