import math

# Driver program for A8 - COP 4045
class Shape(object):
    def __init__(self, shape='Shape'):
        self.shape = shape
        self.perimeter = None
        self.area = None

    def __str__(self):
        return "{} || Perimeter: {}\tArea: {}".format(self.shape, self.perimeter, self.area)



class Circle(Shape):
    def __init__(self, radius):
        Shape.__init__(self, shape='Circle')
        self.radius = float(radius)
        self.find_perimeter()
        self.find_area()
    
    def find_perimeter(self):
        self.perimeter = 2 * math.pi * self.radius

    def find_area(self):
        self.area = math.pi * self.radius ** 2



class Polygon(Shape):
    def __init__(self, shape):
        Shape.__init__(self, shape)
    
    def find_perimeter(self):
        self.perimeter = sum(self.side_lengths)


class Triangle(Polygon):
    def __init__(self, side1, side2, side3):
        Polygon.__init__(self, shape='Triangle')
        # check sides
        if (side1 + side2 <= side3) or (side1 + side3 <= side2) or (side2 + side3 <= side1):
            print("The triangle is invalid")
        else: 
            self.side_lengths = [side1, side2, side3]
            self.a = float(side1)
            self.b = float(side2)
            self.c = float(side3)
            self.find_perimeter()
            self.find_area()

    def find_area(self):
        # Heron's Formulas
        half_perim = self.perimeter / 2
        self.area = (half_perim*(half_perim-self.a)*(half_perim-self.b)*(half_perim-self.c)) ** 0.5


class Rectangle(Polygon):
    def __init__(self, width, length):
        Polygon.__init__(self, shape='Rectangle')
        # check sides
        if (width < 0) or (length < 0):
            print("The rectangle is invalid")
        else: 
            self.side_lengths = [width, length, width, length]
            self.width = float(width)
            self.length = float(length)
            self.find_perimeter()
            self.find_area()

    def find_area(self):
        self.area = self.width * self.length


class Pentagon(Polygon):
    def __init__(self, side):
        Polygon.__init__(self, shape='Pentagon')
        # check sides
        if (side < 0):
            print("The pentagon is invalid")
        else: 
            self.side_lengths = [side, side, side, side, side]
            self.side = float(side)
            self.find_perimeter()
            self.find_area()

    def find_area(self):
        self.area = 0.25 * (math.sqrt(5*(5+2*math.sqrt(5)))) * (self.side ** 2)


class Hexagon(Polygon):
    def __init__(self, side):
        Polygon.__init__(self, shape='Hexagon')
        # check sides
        if (side < 0):
            print("The hexagon is invalid")
        else: 
            self.side_lengths = [side, side, side, side, side, side]
            self.side = float(side)
            self.find_perimeter()
            self.find_area()

    def find_area(self):
        self.area = ((3 * math.sqrt(3)) / 2) * (self.side ** 2)


    
###############################################################################################
######################################## MAIN FUNCTION ########################################   
## Create variables
print()

# create a circle of radius = 2
my_circle = Circle(2) 
# print(my_circle)

# attempt to create a triangle with "incorrect" values
# should produce error message
my_triangle = Triangle(3, 1.7, 4.9) 
# print(my_triangle)

# create a triangle passing the length of each side
my_triangle = Triangle(3, 7, 4.6) 
# print(my_triangle)

# create a rectangle of sides 3 and 4.5
my_rectangle = Rectangle(3, 4.5) 
# print(my_rectangle)

# create a pentagon with sides of equal length
my_pentagon = Pentagon(3) 
# print(my_pentagon)

# create a hexagon with sides of equal length
my_hexagon = Hexagon(3) 
# print(my_hexagon)


############################################
## Print area and perimeter for each variable
print()

print("Circle")
print(f"Perimeter: {my_circle.perimeter:.3f}\tArea: {my_circle.area:.3f}\n")

print("Triangle")
print(f"Perimeter: {my_triangle.perimeter:.3f}\tArea: {my_triangle.area:.3f}\n")

print("Rectangle")
print(f"Perimeter: {my_rectangle.perimeter:.3f}\tArea: {my_rectangle.area:.3f}\n")

print("Pentagon")
print(f"Perimeter: {my_pentagon.perimeter:.3f}\tArea: {my_pentagon.area:.3f}\n")

print("Hexagon")
print(f"Perimeter: {my_hexagon.perimeter:.3f}\tArea: {my_hexagon.area:.3f}\n")

