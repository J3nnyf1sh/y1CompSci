#worksheet 1 

def kilos2ounces():
    kilos = float(input("Enter a weight in kilos: "))
    #round(number, digits): digits is no. of decimals, default is 0
    ounces = 35.274 * kilos 
    print("The weight in ounces is", round(ounces, 2))

#for loop
def count():
    for i in range(5):
        print(i)

#1 Write a function called sayName that displays your name. 
def sayName():
    name = input("What is your name? ")
    print("Hello", name)

#2 Write a sayHello2 function that uses two print statements to display the text shown..
def sayHello2():
    print("Hello\nWorld")

#3 Write a function called dollars2Pounds which converts a dollar's value to pounds using the following formula:
def dollars2Pounds():
    dollars = float(input("enter currency in dollars: "))
    pounds = dollars * 0.80
    print(pounds)

#4 Write a tenHellos function that uses a loop to display “Hello World” ten times (on separate lines). 
def tenHellos():
    for i in range(10):
        print("Hello World")

#5Suppose the prices of train tickets are increasing by 2% every month. Write a function called railFareIncrease which begins by printing the current price of a ticket from Southampton to Portsmouth: £16.50. It should then display the price for 11 more months
def railFareIncrease():
    railFare = 16.50
    for i in range(11):
        railFare += railFare*0.02
        print(round(railFare, 2))

#6 Write a countTo function that asks the user for a number and then counts from 1 to that number. 
def countTo():
    number = int(input("Enter a number: "))
    for i in range(number+1):
        print(i)

#7 Based on your solution to the previous question, write a function called countFromTo that asks the user for two numbers. The first number is the start of the count and the second one is where the count ends
def countFromto():
    fromnumber = int(input("enter a number to count from: "))
    tonumber = int(input("enter a number to count to: "))
    for i in range (fromnumber,tonumber+1):
        print(i)

#8 Write a changeCounter function. This should ask the user how many 1p, 2p and 5p coins they have (using separate questions), and then display the total amount of money in pence.
def changeCounter():
    onep = int(input("How many 1p coins do you have? "))
    twop = int(input("how many 2p coins do you have? "))*2
    fivep = int(input("how many 5p do you have? "))*5
    tenp = int(input("how many 10p do you have? "))*10
    twentyp = int(input("how many 20p do you have? "))*20
    fiftyp = int(input("how many 50p do you have? "))*50
    totalChange = onep+twop+fivep+tenp+twentyp+fiftyp
    print("Your total change is", totalChange, "p")

#9 Write a function weightsTable that prints a table of kilogram weights (between 10 and 50) and their ounce equivalents. The kilogram values should be displayed as shown below:
def weightsTable():
    print("Kgs |  Ounces")
    print("==================")
    for i in range(10, 60, 10):
        print(i, " | ", float(i*35.274))
#range(start, stop, step)
#default step=1

#10 Write a function called futureRailFare that uses a for loop to calculate the future value of a train ticket assuming an monthly price rise of 2%.
def FutureRailFare():
    railFare = round(float(input("enter the current rail fare: ")), 2)
    months = int(input("enter the number of months: "))
    for i in range(months):
        railFare += railFare*0.02
    print("the fare after", months, "months is £", round(railFare, 2))

