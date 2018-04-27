class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Method wont work when x = 0
    def slope_from_origin(self):
        if self.x == 0 and self.y > 0:
            return 'Point({},{}) slope is Inf'.format(self.x, self.y)
        elif self.x == 0 and self.y < 0:
            return 'Point({},{}) slope is Inf'.format(self.x, self.y)
        elif self.x == 0 and self.y == 0:
            return 'Point is origin'
        else:
            return self.y/self.x


print(Point(4, 10).slope_from_origin())
print(Point(4, -10).slope_from_origin())
print(Point(-4, 10).slope_from_origin())
print(Point(4, 10).slope_from_origin())
print(Point(0, 10).slope_from_origin())
print(Point(0, -10).slope_from_origin())
print(Point(0, 0).slope_from_origin())
