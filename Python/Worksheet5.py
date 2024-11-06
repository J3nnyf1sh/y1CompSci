#Worksheet 5

import math
from graphics import * 

def areaOfCircle(radius):
    return math.pi * radius ** 2

def circumferenceOfCircle(radius):
    return math.pi * 2 * radius

def circleInfo(radius):
    c = circumferenceOfCircle(radius)
    a = areaOfCircle(radius)
    print(f'The area is {round(a, 3)} and the circumference is {round(c, 3)}')

def main1():
    x = float(input("Radius: "))
    circleInfo(x)

#main1()

def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)
 
def clickToClose(window):
    window.getMouse()
    window.close()

def drawBrownEyeInCentre(window):

    c = Point(125, 125)

    drawCircle(window, c, 60, 'white')
    drawCircle(window, c, 30, 'brown')
    drawCircle(window, c, 10, 'black')

def main(): 
    window = GraphWin("", 250, 250)
    window.setBackground('grey')

    drawBrownEyeInCentre(window)
    clickToClose(window)

#main()

def drawBlockOfStars(width, height):
    print((('*' * width) + '\n') * height)

def drawLetterE():
    


def main2():
    w = int(input("Width: "))
    h = int(input("Height: "))

    drawBlockOfStars(w, h)

main2()