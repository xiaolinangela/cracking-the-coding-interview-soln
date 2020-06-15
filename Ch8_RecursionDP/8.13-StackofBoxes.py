class Box:

    def __init__(self, h, w, d):
        self.h = h
        self.w = w
        self.d = l

    def __lt__(self, other):
        return self.l*self.w < other.d * other.l
