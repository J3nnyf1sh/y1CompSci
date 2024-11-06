from graphics import *

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

def testMyPoint():
    myPoint = MyPoint(100, 50)
    print("myPoint's x coordinate is", myPoint.getX())
    print("myPoint's y coordinate is", myPoint.getY())
    myPoint.move(10, -20)
    print("myPoint's x coordinate is", myPoint.getX())
    print("myPoint's y coordinate is", myPoint.getY())
    print("myPoint is:", myPoint)

#testMyPoint()

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
    

class Circle:

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def getCentre(self):
        return self.center
    
    def getRadius(self):
        return self.radius
    
    def move(self, dx, dy):
        self.center.move(dx, dy)

    
def testCircle():
    center = MyPoint(100, 50)
    radius = 50
    circle = Circle(center, radius)
    print("the center is", circle.getCentre())
    print("the radius is", circle.getRadius())
    circle.move(10, -20)
    print("the center is", circle.getCentre())
    

#testCircle()
    
class Bank:
    
    def __init__(self, accountHolder, balance, deposit, withdraw):
        self.balance = balance
        self.accountHolder = accountHolder

    def getBalance(self):
        return self.balance
    
    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def getHolder(self):
        return self.accountHolder

def testAccount():
    balance = 0
    accountHolder = "Matthew Poole"
    deposit = 0
    withdraw = 0

    bank = Bank(accountHolder, balance, deposit, withdraw)
    
    print("The name of the account holder is", bank.getHolder())
    print(f"The initial balance of the account is £{bank.getBalance()}")
    bank.deposit(100)
    print(f"After depositing £100, the balance is £{bank.getBalance()}")
    bank.withdraw(50)
    print(f"After withdrawing £50, the balance is £{bank.getBalance()}")
    bank.withdraw(100)
    print(f"After trying to withdraw £100, the balance is £{bank.getBalance()}")
    print(f"Account name: {bank.getHolder()}")
    print(f"Balance: £{bank.getBalance()}")

#testAccount()

class Aeroplane:
    
    def __init__(self, departure, destination):
        self.fuel = 0
        self.altitude = 0
        self.departure = departure
        self.destination = destination
    
    def setFuel(self, fuel):
        pass

    def increaseAltitude(self, amount):
        self.altitude += amount

    def decreaseAltitude(self, amount):
        if self.altitude - amount >= 0:
            self.altitude -= amount

    def setDeparture(self, departure):
        self.departure = departure

    def setDestination(self, destination):
        self.destination = destination

    def getDeparture(self):
        return self.departure

    def getDestination(self):
        return self.destination

    def getAltitude(self):
        return self.altitude
    
    def __str__():
        pass

def testAeroplane():
    departure = input("Departure: ")
    destination = input("Destination: ")
    
    aeroplane = Aeroplane(departure, destination)

    print("The aeroplane is departing from", aeroplane.getDeparture())

        
        
    


