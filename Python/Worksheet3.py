from graphics import *
import math

#1
def clickToClose(win):
    win.getMouse()
    win.close()

def drawStickFigure(win):

    head = Circle(Point(100,60), 20)
    head.draw(win)

    body = Line(Point(100,80), Point(100,120))
    body.draw(win)

    arms = Line(Point(70, 90), Point(130, 90))
    arms.draw(win)

    leg1 = Line(Point(100, 120), Point(130, 150))
    leg1.draw(win)

    leg2 = Line(Point(100, 120), Point(70, 150))
    leg2.draw(win)

def drawCircle(win):
    radius = float(input("Radius: "))

    circle = Circle(Point(250, 250), radius)
    circle.draw(win)

def drawArcheryTarget(win):
    blueCircle = Circle(Point(250, 250), 30)
    blueCircle.setFill("blue")

    redCircle = Circle(Point(250, 250), 20)
    redCircle.setFill("red")

    yellowCircle = Circle(Point(250, 250), 10)
    yellowCircle.setFill("yellow")

    blueCircle.draw(win)
    redCircle.draw(win)
    yellowCircle.draw(win)

def drawRectangle(win):
    height = float(input("Height: "))
    width = float(input("Width: "))

    x = 10 + width
    y = 10 + height

    rect = Rectangle(Point(10,10), Point(x, y))
    rect.draw(win)

def blueCircle(win):
    circle = Circle(win.getMouse(), 50)
    circle.draw(win)

def tenLines(win):
    for i in range(10):
        p1 = win.getMouse()
        p2 = win.getMouse()
        line = Line(p1, p2)
        line.draw(win)

def tenStrings(win):
    string = input("Text: ")
    count = 0

    for i in range(10):
        point = win.getMouse()
        count += 1
        x = string, str(count)
        n = Text(point, x)
        n.draw(win)


def tenColouredRectangles(win):
    inputBox = Entry(Point(100, 100,), 10)
    inputBox.draw(win)

    message = Text(Point(100,50), "Pick a colour:")
    message.draw(win)
        
    
    for i in range(10):
        
        userInput = inputBox.getText()

        p1 = win.getMouse()
        p2 = win.getMouse()

        rect = Rectangle(p1,p2)
        rect.setFill(userInput)
        rect.draw(win)
        
def fiveClickStickFigure(win):

    #head
    headCentre = win.getMouse()
    headEdge = win.getMouse()

    headX = headCentre.getX()
    headY = headCentre.getY()

    headX2 = headEdge.getX()
    headY2 = headEdge.getY()

    pyX = headX - headX2
    pyY = headY - headY2

    radius = math.sqrt((pyX ** 2) + (pyY ** 2))

    head = Circle(headCentre, radius)
    head.draw(win)

    #body 
    xBody = headX
    yBody = headY + radius
    startPointBody = Point(xBody, yBody)

    endYBody = win.getMouse()
    endYBody = endYBody.getY()
    endPointBody = Point(xBody, endYBody)
    body = Line(startPointBody, endPointBody)
    body.draw(win)

    #arms
    arms = Line(Point(70, 90), Point(130, 90))
    arms.draw(win)

    #leg
    leg1 = Line(Point(, endPointBody)
    leg1.draw(win)

    leg2 = Line(Point(100, 120), Point(70, 150))
    leg2.draw(win)


def main():
    win = GraphWin("Worksheet 3", 200, 200)
    win.setBackground("white")

    fiveClickStickFigure(win)
    clickToClose(win)


main()