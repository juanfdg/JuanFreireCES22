class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y


class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def contains_point(self, posn):
        return self.corner.x <= posn.x <= self.corner.x + self.width \
            and self.corner.y <= posn.y <= self.corner.y + self.height


def rectcollide(a, b):
    a1 = Point(a.corner.x, a.corner.y)
    a2 = Point(a.corner.x + a.width, a.corner.y)
    a3 = Point(a.corner.x + a.width, a.corner.y + a.height)
    a4 = Point(a.corner.x, a.corner.y + a.height)

    b1 = Point(b.corner.x, b.corner.y)
    b2 = Point(b.corner.x + b.width, b.corner.y)
    b3 = Point(b.corner.x + b.width, b.corner.y + b.height)
    b4 = Point(b.corner.x, b.corner.y + b.height)

    return a.contains_point(b1) or a.contains_point(b2) or \
           a.contains_point(b3) or a.contains_point(b4) or \
           b.contains_point(a1) or b.contains_point(a2) or \
           b.contains_point(a3) or b.contains_point(a4)


a = Rectangle(Point(0, 0), 10, 5)
b = Rectangle(Point(4, 4), 10, 5)
print(rectcollide(a, b))
