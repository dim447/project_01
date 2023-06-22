import math


class Rectangle:

    def __init__(self, first, second):
        self.x1 = first[0]
        self.y1 = first[1]
        self.x2 = second[0]
        self.y2 = second[1]

    def min_max(self):
        self.xmin = min(self.x1, self.x2)
        self.ymax = max(self.y1, self.y2)
        self.xmax = max(self.x1, self.x2)
        self.ymin = min(self.y1, self.y2)

    def perimeter(self):
        self.min_max()
        self.perimeter_rect = ((((self.xmax - self.xmin) ** 2) ** 0.5 + ((self.ymax - self.ymin) ** 2) ** 0.5) * 2)
        return round(self.perimeter_rect, 2)

    def area(self):
        self.min_max()
        self.area_rect = (((self.xmax - self.xmin) ** 2) ** 0.5 * ((self.ymax - self.ymin) ** 2) ** 0.5)
        return round(self.area_rect - 0.000001, 2)

    def get_pos(self):
        self.min_max()
        self.posx = (round(self.xmin, 2), round(self.ymax, 2))
        return self.posx

    def get_size(self):
        self.min_max()
        self.ab = abs(self.xmax - self.xmin)
        self.cd = abs(self.ymax - self.ymin)
        self.size_rect = (round(self.ab, 2), round(self.cd, 2))
        return self.size_rect

    def move(self, dx, dy):
        self.min_max()
        self.xmin = self.xmin + dx
        self.ymin = self.ymin + dy
        self.xmax = self.xmax + dx
        self.ymax = self.ymax + dy

    def resize(self, width, height):
        self.min_max()
        self.xmax = self.xmin + width
        self.ymin = self.ymax + height
        self.get_size()

# ''' turn() — поворачивает  прямоугольник на 90 & deg; по часовой стрелке вокруг его центра;
#     scale(factor) — изменяет размерв указанное количество раз, тоже относительно центра

    #    Находим точку А после вращения
    # по Вашей формуле
    # ox, oy = origin
    # px, py = point
    # qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    # qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)

    def turn(self):
        coner = math.radians(90)
        # self.xcentr = (self.x1 + self.x2) / 2
        # self.ycentr = (self.y1 + self.y2) / 2
        self.rotate_x1 = self.x1 * math.cos(coner) + self.y1 * math.sin(coner)
        self.rotate_y1 = - self.x1 * math.sin(coner) + self.y1 * math.cos(coner)
        self.rotate_x2 = self.x2 * math.cos(coner) + self.y2 * math.sin(coner)
        self.rotate_y2 = - self.x2 * math.sin(coner) + self.y2 * math.cos(coner)
        self.x1 = self.rotate_x1
        self.y1 = self.rotate_y1
        self.x2 = self.rotate_x2
        self.y2 = self.rotate_y2

    def scale(self, factor):
        # self.min_max()
        self.x1 = round(self.x1 * factor, 2)
        self.y1 = round(self.y1 * factor, 2)
        self.x2 = round(self.x2 * factor, 2)
        self.y2 = round(self.y2 * factor, 2)


rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
print(rect.get_pos(), rect.get_size(), sep='\n')
rect.turn()
print(rect.get_pos(), rect.get_size(), sep='\n')



