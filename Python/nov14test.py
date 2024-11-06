from graphics import *

def clickToclose(win):
    win.getMouse()
    win.close()

def circle(win, point, colour1, colour2):
    circle = Circle(point, 20)
    circle.setFill(colour1)
    circle.setOutline(colour2)
    circle.draw(win)

def part1(win):

    for i in range(15):
        click = win.getMouse()
        y = click.getY()

        if y < 100:
            circle(win, click, 'blue', 'blue')
        elif y < 200:
            circle(win, click, 'white', 'blue')
        elif y < 300:
            circle(win, click, 'pink', 'pink')
        else:
            circle(win, click, 'white', 'pink')
        

def main():
    win = GraphWin(" ", 400, 400)
    win.setBackground('white')

    part1(win)
    clickToclose(win)

#main()

def circle2(win, point, colour1, colour2):
    circle = Circle(point, 20)
    circle.setFill(colour1)
    circle.setOutline(colour2)
    circle.draw(win)

def part2(win, width):
    radius = 20
    diametre = int(radius * 2)
    centreX = width - (radius + (diametre*3))
    centreY = radius

    for j in range(10):
        for i in range(3):
            point = win.getMouse()
            y = point.getY()
            centreX += diametre
            centre = Point(centreX, centreY)

            if y < 100:
                circle2(win, centre, 'blue', 'blue')
            elif y < 200:
                circle2(win, centre, 'white', 'blue')
            elif y < 300:
                circle2(win, centre, 'pink', 'pink')
            else:
                circle2(win, centre, 'white', 'pink')
        
        centreY += diametre
        centreX = width - (radius + (diametre*3))

def main2():
    width = 400
    depth = 400
    win = GraphWin(" ", width, depth)
    win.setBackground('white')

    part2(win, width)
    clickToclose(win)

main2()

