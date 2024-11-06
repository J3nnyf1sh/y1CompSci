from graphics import *
import math


def getName():
    name = input("Whats yo name: ")
    
    while name.isalpha() is False:
        print("Only use letters.")
        name = input("Whats ur name. ")

    print(name.capitalize())

#getName()

def trafficLights():
    win = GraphWin()
    red = Circle(Point(100, 50), 20)
    red.setFill("red")
    red.draw(win)
    amber = Circle(Point(100, 100), 20)
    amber.setFill("black")
    amber.draw(win)
    green = Circle(Point(100, 150), 20)
    green.setFill("black")
    green.draw(win)
    while True:
        pass


def calculateGrade():
    mark = int(input("Enter mark: "))

    while mark > 20 or mark < 0:
        print('enter a mark out of 20')
        mark = int(input("Enter mark: "))


    print(f"grade: {'FFFFFCCCCCBBBBBAAAAAA'[mark]}")

#calculateGrade()

def orderPrice():
    more = True
    total = 0

    while more == True:
        price = float(input('enter the price of the product: '))
        total += price

        askMore = input('Are there more products in the order? [yes/no] ')
        yesNo = ['yes', 'no']

        while askMore not in yesNo:
            print('answer yes or no')
            askMore = input('Are there more products in the order? [yes/no] ')

        if askMore.lower() == 'no':
            more = False
    
    print(f'the total is £{round(total, 2)}')

#orderPrice()
def clickToClose(window):
    window.getMouse()
    window.close()

def distanceBetweenPoints(point1, point2):
    x = point1.getX()
    y = point1.getY()

    x2 = point2.getX()
    y2 = point2.getY()

    side = x - x2
    side2 = y - y2

    distance = math.sqrt((side ** 2) + (side2 ** 2))

    return distance



def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)

def drawBrownEyeInCentre(window):

    c = Point(200, 200)

    drawCircle(window, c, 100, 'white')
    drawCircle(window, c, 50, 'brown')
    drawCircle(window, c, 20, 'black')
    text = " "
    textGraphic = Text(Point(200, 350), text)
    textGraphic.draw(window)
    eye = True

    while eye == True:
        click = window.getMouse()
        distance = distanceBetweenPoints(c, click)

        if distance <= 100:
            if distance > 50:
                textGraphic.setText('Sclera')
            elif distance > 20:
                textGraphic.setText('Iris')
            else:
                textGraphic.setText('Pupil')
        else:
            eye = False







def main():
    win = GraphWin("", 400, 400)
    win.setBackground('light grey')

    drawBrownEyeInCentre(win)
    clickToClose(win)


main()
