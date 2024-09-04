from graphics import *

def drawPatchwork5P(win, colour, topLeft):
    sx = topLeft.getX()
    sy = topLeft.getY()
    x = sx
    y = sy

    for oddRow in range(3):
        ry = y
        #odd row vertical
        for oddVert in range(3):
            outline = Rectangle(Point(x, y), Point(x + 20, y + 20))
            outline.draw(win)

            for oddVertRect in range(2):
                
                rect = Rectangle(Point(x, y), Point(x + 5, y + 20))
                rect.setFill(colour)
                rect.draw(win)

                x += 10
            
            x += 20
            
        x = sx + 20
 
        #odd row horizontal
        for oddHoriz in range(2):
            outline = Rectangle(Point(x, y), Point(x + 20, y + 20))
            outline.draw(win)

            for oddHorizRect in range(2):
                rect = Rectangle(Point(x , y), Point(x + 20, y + 5))
                rect.setFill(colour)
                rect.draw(win)
                    
                y += 10
                
            y = ry
            x += 40
        
        y += 40
        x = sx
        ry = y
    
    y = sy + 20
    x = sx

    for e in range(2):
        ry = y
        #even row vertical lines
        for evenVert in range(2):
            x += 20

            outline = Rectangle(Point(x, y), Point(x + 20, y + 20))
            outline.draw(win)

            for evenVertRect in range(2):
                rect = Rectangle(Point(x + 5, y), Point(x + 10, y + 20))
                rect.setFill(colour)
                rect.draw(win)
                    
                x += 10  

        x = sx

        #even row horizontal lines
        for evenHoriz in range(3):
            y = ry

            outline = Rectangle(Point(x, y), Point(x + 20, y + 20))
            outline.draw(win)

            for evenHorizRect in range(2):
                rect = Rectangle(Point(x, y + 5), Point(x + 20, y + 10))
                rect.setFill(colour)
                rect.draw(win)

                y += 10

            x += 40
        
        x = sx
        y += 20

def drawPatchwork4F(win, colour, topLeft):
    x = topLeft.getX()
    y = topLeft.getY()
    
    radius = 5

    outline = Rectangle(topLeft, Point(x + 100, y + 100))
    outline.draw(win)

    x += 50
    y += 95

    for i in range(10):
        centre = Point(x,y)

        circle = Circle(centre, radius)
        circle.setOutline(colour)
        circle.draw(win)

        radius += 5
        y -= 5

def drawPatchworkPlain(win, colour, topLeft):
    x = topLeft.getX()
    y = topLeft.getY()
    rect = Rectangle(topLeft, Point(x + 100, y + 100))
    rect.setFill(colour)
    rect.draw(win)

def main():

    grid = input("5 x 5 or 7 x 7 or 9 x 9? ")

    while grid.isalpha() == True:
        print("Please choose between 5, 7 or 9.")
        grid = input("5 x 5 or 7 x 7 or 9 x 9? ")

    while int(grid) not in ([5, 7, 9]):
        print("Please choose between 5, 7 or 9.")
        grid = input("5 x 5 or 7 x 7 or 9 x 9? ")

    validColours = ['red', 'green', 'blue', 'magenta', 'orange', 'yellow', 'cyan']

    colour1 = input("Pick the first colour: ")
    
    while colour1.lower() not in validColours:
        print("Please choose between red, green, blue, magenta, orange, yellow or cyan")
        colour1 = input("Pick the first colour: ")

    colour2 = input("Pick the second colour: ")

    while colour2.lower() not in validColours:
        print("Please choose between red, green, blue, magenta, orange, yellow or cyan")
        colour2 = input("Pick the second colour: ")
    while colour2 == colour1:
        print("The colours must be different.")
        colour2 = input("Pick the second colour: ")
      
    colour3 = input("Pick the third colour: ")

    while colour3.lower() not in validColours:
        print("Please choose between red, green, blue, magenta, orange, yellow or cyan")
        colour3 = input("Pick the third colour: ")
    while colour3 == colour1 or colour3 == colour2:
        print("The colours must be different.")
        colour3 = input("Pick the third colour: ")
        
    grid = int(grid)
    width = grid * 100
    height = grid * 100
    win = GraphWin(" ", width, height)
    win.setBackground('white')

    if grid == 5:
        colourList = [['0', '1', '1', '1', '0'],
                      ['2', '0', '1', '0', '2'],
                      ['2', '2', '0', '2', '2'],
                      ['2', '0', '1', '0', '2'],
                      ['0', '1', '1', '1', '0']]
    elif grid == 7:
        colourList = [['0', '1', '1', '1', '1', '1', '0'],
                      ['2', '0', '1', '1', '1', '0', '2'],
                      ['2', '2', '0', '1', '0', '2', '2'],
                      ['2', '2', '2', '0', '2', '2', '2'],
                      ['2', '2', '0', '1', '0', '2', '2'],
                      ['2', '0', '1', '1', '1', '0', '2'],
                      ['0', '1', '1', '1', '1', '1', '0']]
    elif grid == 9:
        colourList = [['0', '1', '1', '1', '1', '1', '1', '1', '0'],
                      ['2', '0', '1', '1', '1', '1', '1', '0', '2'],
                      ['2', '2', '0', '1', '1', '1', '0', '2', '2'],
                      ['2', '2', '2', '0', '1', '0', '2', '2', '2'],
                      ['2', '2', '2', '2', '0', '2', '2', '2', '2'],
                      ['2', '2', '2', '0', '1', '0', '2', '2', '2'],
                      ['2', '2', '0', '1', '1', '1', '0', '2', '2'],
                      ['2', '0', '1', '1', '1', '1', '1', '0', '2'],
                      ['0', '1', '1', '1', '1', '1', '1', '1', '0']]                  
    

    for row in range(grid):

        for col in range(grid):
            x = col * 100
            y = row * 100

            #colourChoose = colourList[row[col]]

            topLeft = Point(x, y)
            patch = colourList[row][col]

            if patch[0] == '0':
                colour = colour1
            elif patch[0] == '1':
                colour = colour2
            elif patch[0] == '2':
                colour = colour3
        

            if x >= 100 and x < width - 100 and y >= 100 and y < height - 100:
                if row == col or row + col == grid - 1:
                    drawPatchwork4F(win, colour, topLeft)
                else:
                    drawPatchwork5P(win, colour, topLeft)
            else:
                drawPatchworkPlain(win, colour, topLeft)

    win.getMouse()

main()
