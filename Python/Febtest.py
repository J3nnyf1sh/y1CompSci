class TravelCard:

    def __init__(self):
        self.balance = 10 #£

    def getBalance(self):
        return self.balance

    def topUp(self, amount):
        self.balance += amount

    def swipe(self):
        output = f"You do not have enough money for this on your TravelCard"
        if self.balance >= 4:
            self.balance -= 4
            output = f"Card swiped. New Balance: £{self.balance:,.2f}"
        
        return output
        
def testTravelCard():
    myCard = TravelCard()

    print(myCard.swipe())
    print(f"Balance: £{myCard.getBalance():,.2f}")

    print(myCard.swipe())
    print(f"Balance: £{myCard.getBalance():,.2f}")

    print(myCard.swipe())
    print(f"Balance: £{myCard.getBalance():,.2f}")

###################################################################
    
    #task2

###################################################################
    
class TravelCard2:

    validType = {"bus": 5, "train": 7}

    def __init__(self):
        self.balance = 10 #£

    def getBalance(self):
        return self.balance

    def topUp(self, amount):
        self.balance += amount

    def swipe(self, journeyType):
        output = f"You do not have enough money for this on your TravelCard"

        if journeyType.lower() in self.validType:
            price = self.validType[journeyType.lower()]
            if self.balance >= price:
                self.balance -= price
                output = f"Card swiped. New Balance: £{self.balance:,.2f}"
        else:
            output = f"You cannot use the TravelCard for this"
        
        return output
        

def testTravelCard2():
    myCard = TravelCard2()

    print(myCard.swipe("taxi")) #invalid
    print(f"Balance: £{myCard.getBalance():,.2f}")

    print(myCard.swipe("train"))
    print(f"Balance: £{myCard.getBalance():,.2f}")

    print(myCard.swipe("train")) 

    myCard.topUp(10) 
    print(f"Balance: £{myCard.getBalance():,.2f}")

    print(myCard.swipe("bus"))
    print(f"Balance: £{myCard.getBalance():,.2f}")

testTravelCard()
testTravelCard2()