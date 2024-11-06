from graphics import *


def clickToclose(win):
    win.getMouse()
    win.close()

#------------------------------------------------------------------------
#------------------------------------------------------------------------

def circle(win, point, colour1, colour2):
    circle = Circle(point, 20)
    circle.setFill(colour1)
    circle.draw(win)


def part1(win):

    for i in range(10):
        click = win.getMouse()
        x = click.getX()
        y = click.getY()

        if x <= 300:
            if y <= 200:
                circle(win, click, 'pink', 'purple')
            else:
                circle(win, click, 'purple', 'pink')
        else:
            if y <= 200:
                circle(win, click, 'blue', 'green')
            else:
                circle(win, click, 'green', 'blue')

def part1(win):

    for i in range(10):
        click = win.getMouse()
        x = click.getX()
        y = click.getY()

        if x <= 300:
            if y <= 200:
                circle(win, click, 'pink', 'purple')
            else:
                circle(win, click, 'purple', 'pink')
        else:
            if y <= 200:
                circle(win, click, 'blue', 'green')
            else:
                circle(win, click, 'green', 'blue')

def main():
    win = GraphWin(" ", 600, 400)
    win.setBackground('white')

    part1(win)
    clickToclose(win)

#main()

#------------------------------------------------------------------------
#------------------------------------------------------------------------

def circle2(win, point, colour1, colour2):
    circle = Circle(point, 50)
    circle.setFill(colour1)
    circle.setOutline(colour2)
    circle.draw(win)

def part2(win, width, depth):
    radius = 50
    diametre = int(radius * 2)
    centreX = radius
    centreY = -radius

    for j in range(width//diametre):
        for i in range(depth//diametre):
            win.getMouse()
            centreY += diametre
            centre = Point(centreX, centreY)

            if centreX <= 300:
                if centreY <= 200:
                    circle2(win, centre, 'pink', 'purple')
                else:
                    circle2(win, centre, 'purple', 'pink')
            else:
                if centreY <= 200:
                    circle2(win, centre, 'blue', 'green')
                else:
                    circle2(win, centre, 'green', 'blue')
        
        centreX += diametre
        centreY = -radius


def main2():
    width = 600
    depth = 400
    win = GraphWin(" ", width, depth)
    win.setBackground('white')

    part2(win, width, depth)
    clickToclose(win)

#main2()

#------------------------------------------------------------------------
#------------------------------------------------------------------------

def circle3(win, point, colour1, colour2):
    circle = Circle(point, 50)
    circle.setFill(colour1)
    circle.setOutline(colour2)
    circle.draw(win)

def part3(win, width, depth):
    radius = 50
    diametre = int(radius * 2)
    centreX = radius
    centreY = -radius

    for j in range(width//diametre):
        for i in range(depth//diametre):
            win.getMouse()
            centreY += diametre
            centre = Point(centreX, centreY)

            if centreX <= 400 and centreX >= 200 and centreY <= 300 and centreY >= 200:
                circle3(win, centre, 'pink', 'purple')
            elif centreX <= 500 and centreX >= 100 and centreY <= 400 and centreY >= 100:
                circle3(win, centre, 'blue', 'green')
            else:
                circle3(win, centre, 'brown', 'green')
        
        centreX += diametre
        centreY = -radius

def main3():
    width = 600
    depth = 500
    win = GraphWin(" ", width, depth)
    win.setBackground('white')

    part3(win, width, depth)
    clickToclose(win)

#main3()

def circle4(win, centreX, centreY, size, colour):
    circle = Circle(Point(centreX, centreY), size)
    circle.setFill(colour)
    circle.draw(win)

def colourSelector(point, hWidth, hHeight):
    colours = ["blue","red","yellow","green"]
    x = point.getX()
    y = point.getY()
    #print("x: ",x," y: ",y)

    if x < hWidth and y <hHeight :
        return colours[0]
    elif x >= hWidth and y <hHeight :
        return colours[1]
    elif x < hWidth and y >= hHeight :
        return colours[2]
    else:
        return colours[3]
    
    
def main4():
    width = 300
    height = 200
   
    hWidth = width//2
    hHeight = height//2

    win = GraphWin(" ",width,height)
    win.setBackground('white')

    size = 20
    diametre = int(size * 2)

    centreY = size
    centreX = -size

    for y in range(0, height//diametre):
        for x in range(0, width//diametre):
            point = win.getMouse()
            centreX += diametre
            colour = colourSelector(point, hWidth, hHeight)
            circle4(win, centreX, centreY, size, colour)

        centreY += diametre
        centreX = -size

main4()

def circle5(win, point, colour1, colour2):
    circle = Circle(point, 50)
    circle.setFill(colour1)
    circle.setOutline(colour2)
    circle.draw(win)

def part5(win, width, depth):
    radius = 50
    diametre = int(radius * 2)
    centreX = width + radius
    centreY = depth - radius

    for j in range(depth//diametre):
        for i in range(width//diametre):
            win.getMouse()
            centreX -= diametre
            centre = Point(centreX, centreY)

            if centreX <= 400 and centreX >= 200 and centreY <= 300 and centreY >= 200:
                circle3(win, centre, 'pink', 'purple')
            elif centreX <= 500 and centreX >= 100 and centreY <= 400 and centreY >= 100:
                circle3(win, centre, 'blue', 'green')
            else:
                circle3(win, centre, 'brown', 'green')
        
        centreY -= diametre
        centreX = width + radius

def main5():
    width = 600
    depth = 500
    win = GraphWin(" ", width, depth)
    win.setBackground('white')

    part5(win, width, depth)
    clickToclose(win)









