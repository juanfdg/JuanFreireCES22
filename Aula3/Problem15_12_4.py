class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Method wont work when other_point.x - self.x = 0
    def get_line_to(self, other_point):
        slope = (other_point.y-self.y)/(other_point.x-self.x)
        linear_coef = self.y - slope*self.x

        return (slope, linear_coef)


print(Point(4, 11).get_line_to(Point(6, 15)))