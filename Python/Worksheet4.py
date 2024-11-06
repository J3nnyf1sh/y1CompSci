#Worksheet 1 
from graphics import * 

def clickToClose(win):
    win.getMouse()
    win.close()

def personalGreeting():
    name = input("what is your name? ")
    print(f"Hello, {name}, nice to see you!")

def formalName():
    givenName = input("What is your given name? ")
    familyName = input("What is your family name? ")
    print("Hello", givenName, familyName + ", nice to see you!")

def kilos2ounces():
    kilos = float(input("Enter a weight in kilos: "))
    ounces = 35.274 * kilos 
    print(kilos, "kilos is equal to", round(ounces, 2), "ounces")

def generateEmail():
    foreName = input("What is your forename? ") #2 first letter 
    lastName = input("What is your last name? ") #1 first 4 letters 
    year = input("What year did you enter university? ") #3 final 2 digits
    email = lastName[:4].lower() + "."  + foreName[0].lower() + "." + year[-2:]
    print(email + "@myport.ac.uk")

def graphicLetters(win):

    sentence = input("Please enter sentence: ")

    x = 10 
    y = 10
    p = Point(x,y)
 
    for i in range(len(sentence)):
        win.getMouse()
        x = x + 10
        p = Point(x,y)

        text = Text(p, sentence[i])
        text.draw(win)

def singASong():

    word = input("Choose a word: ")
    repeats = int(input("How many repeats: "))
    lines = int(input("How many lines: "))

    print((((word + " ") * repeats) + "\n") * lines )

def exchangeTable():
    
    print("Euros  |  Pounds")
    print("-----------------")

    for i in range(21):
        pounds = i / 1.17
        print(i, "     |   ", round(pounds, 2))

def makeInitialism():
    abriviation = " "
    phrase = input("Phrase: ")
    phrase = phrase.split(" ")

    for ew in range(len(phrase)):
        word = phrase[ew]
        letter = word[0]
        abriviation += letter

    print(abriviation.upper())
    
def nameToNumber():
    name = input("Name: ")

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ans = 0

    for eachLetter in name.lower():
        ans += alphabet.index(eachLetter) + 1
    
    print(ans)


def main():
    win = GraphWin("Lecture 4", 500, 500)
    win.setBackground("white")


    clickToClose(win)

makeInitialism()


    
    
