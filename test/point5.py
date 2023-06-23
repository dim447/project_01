class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, xx, yy):
        self.x = self.x + xx
        self.y = self.y + yy

    def length(self, p):
        return round(((p.x - self.x) ** 2 + (p.y - self.y) ** 2) ** 0.5, 2)


class PatchedPoint(Point):
    def __init__(self, *args):
        if not args:
            self.x = self.y = 0
        elif len(args) == 1 and (isinstance(args[0], (list, tuple, set))):
            self.x = args[0][0]
            self.y = args[0][1]
        else:
            self.x = args[0]
            self.y = args[1]

    def __add__(self, args):
        self.x1 = self.x + args[0]
        self.y1 = self.y + args[1]
        self.new_point = (self.x1, self.y1)
        return self.new_point

    def __iadd__(self, args):
        self.x += args[0]
        self.y += args[1]
        return self

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"PatchedPoint({self.x}, {self.y})"


# point = PatchedPoint()
# print(point)
# new_point = point + (2, -3)
# print(point, new_point, point is new_point)

first_point = second_point = PatchedPoint((5, -7))
first_point += (7, 3)
print(first_point, second_point, first_point is second_point)
