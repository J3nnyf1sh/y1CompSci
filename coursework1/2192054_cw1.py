from graphics import *

#draws penultimate patch 5
def drawPatchwork5P(win, colour, sx, y, rects5PList):
    x = sx #sx (start x) resets x value to the leftmost side of the patch

    pattern = [0, 1]
    rectColours = [['white', colour], [colour, 'white']] #for swapping between chosen colour and white for each row
    interChange = 0 # swaps the colour each row of the back rectangle and line rectangles
    patternChange = 0 # changes for every mini patch drawn to switch between horizontal and vertical lines

    #CHALLENGE
    drawnRectangles = [] 

    for row in range(5):
        for col in range(5):
            backRect = Rectangle(Point(x, y), Point(x + 20, y + 20))
            backRect.setFill(rectColours[0][interChange])
            backRect.draw(win)
            colour = rectColours[1][interChange]
            drawnRectangles.append(backRect)

            if pattern[patternChange] == 0: #draws vertical pattern
                outline = Rectangle(Point(x, y), Point(x + 20, y + 20))
                outline.draw(win)
                drawnRectangles.append(outline)
                for VertRect in range(2):
                    rect = Rectangle(Point(x + (10 * VertRect), y), Point(x + 5 + (10 * VertRect), y + 20))
                    rect.setFill(colour)
                    rect.draw(win)
                    drawnRectangles.append(rect)
            else: #draws horizontal pattern
                outline = Rectangle(Point(x, y), Point(x + 20, y + 20))
                outline.draw(win)
                drawnRectangles.append(outline)
                for horizRect in range(2):
                    rect = Rectangle(Point(x, y + (10 * horizRect)), Point(x + 20, y + 5 + (10 * horizRect)))
                    rect.setFill(colour)
                    rect.draw(win)
                    drawnRectangles.append(rect)

            x += 20

            if patternChange == 0: 
                patternChange += 1
            else:
                patternChange -= 1

        y += 20
        x = sx    

        if interChange == 0:
            interChange += 1
        else:
            interChange -= 1

    #CHALLENGE   
    rects5PList.append(drawnRectangles)
    return rects5PList

#CHALLENGE: undraws penultimate patch 5 
def undrawPatchwork5P(x, y, allPatchworkLists, rects5PList):
    for i in range(len(allPatchworkLists[1])):
        if (x, y) == allPatchworkLists[1][i]:
            for r in range(100):
                rects5PList[i][r].undraw()
            rects5PList.remove(rects5PList[i])
    return rects5PList

#draws final patch 4
def drawPatchwork4F(win, colour, x, y, circles4FList):
    radius = 5

    outlineBackground = Rectangle(Point(x, y), Point(x + 100, y + 100))
    outlineBackground.setFill('white')
    outlineBackground.draw(win)

    x += 50
    y += 95

    drawnShapes = [outlineBackground]

    for i in range(10):
        centre = Point(x, y)

        circle = Circle(centre, radius)
        circle.setOutline(colour)
        circle.draw(win)

        radius += 5
        y -= 5

        drawnShapes.append(circle)
    
    circles4FList.append(drawnShapes)

    return circles4FList

#CHALLENGE: undraws final patch 4 
def undrawPatchwork4F(x, y, allPatchworkLists, circles4FList):
    for i in range(len(allPatchworkLists[0])):
        if (x, y) == allPatchworkLists[0][i]:
            for c in range(11):
                circles4FList[i][c].undraw()
            circles4FList.remove(circles4FList[i])
    return circles4FList

#draws plain patches
def drawPatchworkPlain(win, colour, x, y, plainRectsList):
    rect = Rectangle(Point(x, y), Point(x + 100, y + 100))
    rect.setFill(colour)
    rect.draw(win)
    plainRectsList.append(rect)
    return plainRectsList

#CHALLENGE: undraws plain patches
def undrawPatchworkPlain(x, y, allPatchworkLists, plainRectsList):
    for i in range(len(allPatchworkLists[2])):
        if (x, y) == allPatchworkLists[2][i]:
            plainRectsList[i].undraw()
            plainRectsList.remove(plainRectsList[i])
    return plainRectsList

#CHALLENGE: draws OK and CLOSE buttons
def buttons(win, width):
    x = 30
    x1 = 0
    text = 'OK'
    twoButtons = [] #returns a list so that they can be undrawn when in editmode

    for t in range(2):
        text = ['OK', 'CLOSE']
        button = Rectangle(Point(x1, 0), Point(x, 30))
        button.setFill('black')
        button.draw(win)
        buttonText = Text(Point(x1 + 15, 15), text[t])
        buttonText.setTextColor('white')
        buttonText.setSize(8)
        buttonText.draw(win)
        x1 = width - 30
        x = width
        twoButtons.append((button, buttonText))
    
    return twoButtons

#CHALLENGE: selecting patches
def selectionMode(win, width, selectedPatch, topLefts, allPatchworkLists, allColourLists, validColours, circles4FList, rects5PList, plainRectsList):
    twoButtons = buttons(win, width) #for undrawing in editmode

    selectMode = True

    while selectMode == True:
        click = win.getMouse()
        x = click.getX()
        y = click.getY()
        xt = (x//100)*100
        yt = (y//100)*100 

        if x < 30 and y < 30: #OK button
            editMode(win, width, selectedPatch, topLefts, allPatchworkLists, allColourLists, validColours, twoButtons, circles4FList, rects5PList, plainRectsList)
            selectMode = False
        elif x > width - 30 and y < 30: #CLOSE button
            win.close()
        elif (xt, yt) not in topLefts: #only selects if the patch isn't already selected
            rect = Rectangle(Point(xt, yt), Point(xt + 100, yt + 100))
            rect.setOutline('black')
            rect.setWidth(5)
            rect.draw(win)
            topLefts.append((xt, yt))
            selectedPatch.append(rect)
        elif (xt, yt) in topLefts: #deselection
            for i in range (len(topLefts)):
                if (xt, yt) == topLefts[i]:
                    selectedPatch[i].undraw()
                    topLefts.remove(topLefts[i])
                    selectedPatch.remove(selectedPatch[i])
                    break

#CHALLENGE: edit mode and key input from user 
def editMode(win, width, selectedPatch, topLefts, allPatchworkLists, allColourLists, validColours, twoButtons, circles4FList, rects5PList, plainRectsList):
    print("edit mode")
    print("Press a key: \n d = deselect \n s = select \n f = final patch \n p = penultimate patch \n q = plain patch \n r = red \n g = green \n b = blue \n m = magenta \n o = orange \n y = yellow \n c = cyan")
    editMode = True 

    for t in range(2): #undraws OK and CLOSE buttons
        for b in range(2):
                    twoButtons[t][b].undraw()

    while editMode == True:
        key = win.getKey()
        colourKeys = ['r', 'g', 'b', 'm', 'o', 'y', 'c']
        patchKeys = ['f', 'p', 'q']

        if key == 'd':
            deselection(selectedPatch)
            selectedPatch = []
            topLefts = []
        elif key == 's':
            selectionMode(win, width, selectedPatch, topLefts, allPatchworkLists, allColourLists, validColours, circles4FList, rects5PList, plainRectsList)
            editMode = False

        for i in range(len(patchKeys)):
            if key == patchKeys[i]:
                patchChange(win, topLefts, patchKeys[i], allPatchworkLists, allColourLists, validColours, circles4FList, rects5PList, plainRectsList)
        for i in range(len(colourKeys)):
            if key == colourKeys[i]:
                colourChange(win, topLefts, validColours[i], allPatchworkLists, allColourLists, validColours, circles4FList, rects5PList, plainRectsList)
        
        if key == 'x':
            deselection(selectedPatch)
            allPatchworkLists, allColourLists, circles4FList, rects5PList, plainRectsList = \
                funkyFunction(win, width, allPatchworkLists, allColourLists, circles4FList, rects5PList, plainRectsList)
            selectedPatch = []
            topLefts = [] 

#CHALLENGE: d undraws borders of selected patches
def deselection(selectedPatch):
    for r in range(len(selectedPatch)):
        selectedPatch[r].undraw()

#CHALLENGE: x draws a big smiley face
def funkyFunction(win, width, allPatchworkLists, allColourLists, circles4FList, rects5PList, plainRectsList):
    for i in range(len(allPatchworkLists[0])):
        for c in range(11):
            circles4FList[i][c].undraw()
    circles4FList = []

    for i in range(len(allPatchworkLists[1])):
        for r in range(100):
            rects5PList[i][r].undraw()
    rects5PList = []

    for i in range(len(allPatchworkLists[2])):
        plainRectsList[i].undraw()
    plainRectsList = []

    allPatchworkLists = [[], [], []]
    allColourLists = [[], [], [], [], [], [], []]

    if width == 500:
        design = [[0, 0, 0, 0, 0],
                  [0, 1, 0, 1, 0],
                  [0, 0, 2, 0, 0],
                  [1, 0, 0, 0, 1],
                  [0, 1, 1, 1, 0]]    
    if width == 700:
        design = [[0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 1, 0, 0],
                  [0, 0, 1, 0, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 1, 1, 1, 1, 0],
                  [0, 0, 1, 2, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0]]
    if width == 900:
        design = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0, 0, 1, 0, 0],
                  [0, 0, 1, 0, 0, 0, 1, 0, 0],
                  [0, 0, 1, 0, 0, 0, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 1, 1, 1, 1, 1, 1, 0],
                  [0, 0, 1, 2, 2, 2, 1, 0, 0],
                  [0, 0, 0, 1, 1, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0],]
        
    for row in range(int(width/100)):
        for col in range(int(width/100)):
            x = col * 100
            y = row * 100
        
            if design[row][col] == 0:
                plainRectsList = drawPatchworkPlain(win, 'yellow', x, y, plainRectsList)
                allPatchworkLists[2].append((x, y))
                allColourLists[5].append((x,y))
            elif design[row][col] == 1:
                rects5PList = drawPatchwork5P(win, 'blue', x, y, rects5PList)
                allPatchworkLists[1].append((x, y))
                allColourLists[2].append((x, y))
            elif design[row][col] == 2:
                circles4FList = drawPatchwork4F(win, 'red', x, y, circles4FList)
                allPatchworkLists[0].append((x, y))
                allColourLists[0].append((x, y))
        
    return allPatchworkLists, allColourLists, circles4FList, rects5PList, plainRectsList

#CHALLENGE: changes colour (key inputs: r, g, b, m, o ,y, c)
def colourChange(win, topLefts, colour, allPatchworkLists, allColourLists, validColours, circles4FList, rects5PList, plainRectsList):

    for c in range(7):
        if colour == validColours[c]:
            colourList = c
        
    for r in range(len(topLefts)):
        x = topLefts[r][0]
        y = topLefts[r][1]

        for oc in range(7): #removes coordinates from the original colour list
            if (x, y) in allColourLists[oc]:
                allColourLists[oc].remove((x, y))
        
        allColourLists[colourList].append((x, y)) #adds coordinates to the new colour list

        #undraws and redraws original patch in new colour. Coordinates removed and append so there are no duplicates
        if (x, y) in allPatchworkLists[0]:
            circles4FList = undrawPatchwork4F(x, y, allPatchworkLists, circles4FList)
            allPatchworkLists[0].remove((x, y)) 
            circles4FList = drawPatchwork4F(win, colour, x, y, circles4FList)
            allPatchworkLists[0].append((x, y)) 
        elif (x, y) in allPatchworkLists[1]:
            rects5PList = undrawPatchwork5P(x, y, allPatchworkLists, rects5PList)
            allPatchworkLists[1].remove((x, y))
            rects5PList = drawPatchwork5P(win, colour, x, y, rects5PList)
            allPatchworkLists[1].append((x, y))
        elif (x, y) in allPatchworkLists[2]:
            plainRectsList = undrawPatchworkPlain(x, y, allPatchworkLists, plainRectsList)
            allPatchworkLists[2].remove((x, y))
            plainRectsList = drawPatchworkPlain(win, colour, x, y, plainRectsList)
            allPatchworkLists[2].append((x, y))

#CHALLENGE: changes patch design (key inputs: f, p, q)
def patchChange(win, topLefts, key, allPatchworkLists, allColourLists, validColours, circles4FList, rects5PList, plainRectsList):
    for r in range(len(topLefts)):
        x = topLefts[r][0]
        y = topLefts[r][1]

        #finds the original colour to keep the same
        for c in range(7):
            if (x, y) in allColourLists[c]:
                colour = validColours[c]
        
        #undraws the selected patch and removes from its respective list
        if (x, y) in allPatchworkLists[0]:
            circles4FList = undrawPatchwork4F(x, y, allPatchworkLists, circles4FList)
            allPatchworkLists[0].remove((x, y))
        elif (x, y) in allPatchworkLists[1]:
            rects5PList = undrawPatchwork5P(x, y, allPatchworkLists, rects5PList)
            allPatchworkLists[1].remove((x, y))
        elif (x, y) in allPatchworkLists[2]:
            plainRectsList = undrawPatchworkPlain(x, y, allPatchworkLists, plainRectsList)
            allPatchworkLists[2].remove((x, y))

        #draws new patch and adds to respective list
        if key == 'f':
            circles4FList = drawPatchwork4F(win, colour, x, y, circles4FList)
            allPatchworkLists[0].append((x, y))
        elif key == 'p':
            rects5PList = drawPatchwork5P(win, colour, x, y, rects5PList)
            allPatchworkLists[1].append((x, y))
        elif key == 'q':
            plainRectsList = drawPatchworkPlain(win, colour, x, y, plainRectsList)
            allPatchworkLists[2].append((x, y))

def main():
    grid = input("5, 7 or 9? ")

    while grid not in ('5', '7', '9'): #checks
        print("Please choose between 5, 7 or 9.")
        grid = input("5 x 5 or 7 x 7 or 9 x 9? ")

    validColours = ['red', 'green', 'blue', 'magenta', 'orange', 'yellow', 'cyan']
    selectedColours = [] 
    
    #colour selection
    for i in range(3):
        no = ['first', 'second', 'third'] #list to update question each round
        print("Please choose between red, green, blue, magenta, orange, yellow or cyan")
        colour = input(f"Pick the {no[i]} colour: ").lower()
        valid = False

        #colour checker and reprompt
        while valid == False:
                if colour not in validColours: 
                    print("Please choose between red, green, blue, magenta, orange, yellow or cyan")
                    colour = input(f"Pick the {no[i]} colour: ")
                elif colour in selectedColours: 
                    print("The colours must be different.")
                    colour = input(f"Pick the {no[i]} colour: ")
                else:
                    selectedColours.append(colour)
                    valid = True
    
    #creating window
    grid = int(grid)
    width = grid * 100
    height = grid * 100
    win = GraphWin(" ", width, height)
    win.setBackground('white')

    #CHALLENGE: lists to store drawn patches and their colours
    allPatchworkLists = [[], [], []] #1st = 4F, 2nd = 5P, 3rd = Plain
    allColourLists = [[], [], [], [], [], [], []] #1st = red, 2nd = green, 3rd = blue, 4th = magenta, 5th = orange, 6th = yellow, 7th = cyan

    circles4FList = [] #lists for undrawing patches
    rects5PList = []
    plainRectsList = []

    for row in range(grid):
        for col in range(grid):
            x = col * 100 
            y = row * 100
            
            #determines colour from patch location
            if row == col or row + col == grid - 1: #if patch coordinate are diagonal (negative line is shifted as coordinates are of the topleft of the patch)
                colour = selectedColours[0]
            elif row < col:    #if patch coordinates are greater than the postive line
                if row + col > grid - 1:    #if coordinates are less than the negative line
                    colour = selectedColours[2]
                else:    #if coordinates are greater than the negative line
                    colour = selectedColours[1]
            else:    #if patch coordinates are less than the positive line
                if row + col > grid - 1:
                    colour = selectedColours[1]
                else:
                    colour = selectedColours[2]
            
            #CHALLENGE: appending (x, y) to respective colour lists
            for c in range(7):
                if colour == validColours[c]:
                    allColourLists[c].append((x, y))

            #determines patch location and drawing
            #CHALLENGE: appending (x, y) to respective patch lists
            if x >= 100 and x < width - 100 and y >= 100 and y < height - 100: #keeps the border patches plain
                if row == col or row + col == grid - 1: #row == col is the diagonal line going downwards from the topleft, row + col == grid - 1 is the linee going up from the bottomleft
                    circles4FList = drawPatchwork4F(win, colour, x, y, circles4FList)
                    allPatchworkLists[0].append((x, y))
                elif row != col or row + col != grid - 1:
                    rects5PList = drawPatchwork5P(win, colour, x, y, rects5PList)
                    allPatchworkLists[1].append((x, y))
            else:
                plainRectsList = drawPatchworkPlain(win, colour, x, y, plainRectsList)
                allPatchworkLists[2].append((x, y))

    selectedPatch = [] #lists the drawn rectangles(borders) of the selected patches
    topLefts = [] #lists the x and y coordinates of the top left of the selected patches
    selectionMode(win, width, selectedPatch, topLefts, allPatchworkLists, allColourLists, validColours, circles4FList, rects5PList, plainRectsList)
    win.getMouse()

main()