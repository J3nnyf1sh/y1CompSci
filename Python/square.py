class MyPoint:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        output = f"MyPoint({self.x}, {self.y})"
        return output

class Square:

    def __init__(self, p1, side):
        self.p1 = p1
        self.side = side
        self.p2 = MyPoint(p1.getX() + side, p1.getY() + side)
        self.fillColour = "black"
        self.outlineColour = "black"
        self.getArea()
        self.getPerimeter()
        self.getCenter()

    def getP1(self):
        return self.p1
    
    def getSide(self):
        return self.side
    
    def getP2(self):
        return self.p2
    
    def move(self, dx, dy):
        self.p1.move(dx, dy)
        self.p2.move(dx, dy)
    
    def setFillColour(self, colour):
        colours = ["red", "green", "blue", "yellow", "purple"]
        if colour in colours:
            self.fillColour = colour
    
    def setOutlineColour(self, colour):
        colours = ["red", "green", "blue", "yellow", "purple"]
        if colour in colours:
            self.outlineColour = colour

    def getPerimeter(self):
        self.perimeter = self.side*4

    def getArea(self):
        self.area = self.side**2

    def getCenter(self):
        halfSide = self.side/2
        self.center = MyPoint(self.p1.getX() + halfSide, self.p1.getY() + halfSide)
    
    def scale(self, integer):
        self.p1 = MyPoint(self.center.getX() - (self.getSide() * integer)/2, self.center.getY() - (self.getSide() * integer)/2)
        self.p2 = MyPoint(self.center.getX() + (self.getSide() * integer)/2, self.center.getY() + (self.getSide() * integer)/2)
def testSquare():
    p1 = MyPoint(100, 50)
    square = Square(p1, 50)
    print("square's side length is", square.getSide())  # 50
    print("square's p1 is", square.getP1())  # MyPoint(100, 50)
    print("square's p2 is", square.getP2())  # MyPoint(150, 100)

    print("Changing square's fill colour to red")
    square.setFillColour("red")
    print("square's fill colour is", square.fillColour)  # red
    print("Changing square's fill colour to leopard print!")
    square.setFillColour("leopard print")
    print("square's fill colour is", square.fillColour)

    print("Changing square's outline colour to blue")
    square.setOutlineColour("blue")
    print("square's outline colour is", square.outlineColour)
    print("Changing square's fill colour to polka dot!")
    square.setOutlineColour("polka dot")
    print("square's outline colour is", square.outlineColour)

    print("The area of the square is", square.area)
    print("The perimeter of thesquare is", square.perimeter)

    print("The center of the square is", square.center)

    square.move(10, -20)
    print("square's side length is", square.getSide())  # 50
    print("square's p1 is", square.getP1())  # MyPoint(110, 30)
    print("square's p2 is", square.getP2())


testSquare()