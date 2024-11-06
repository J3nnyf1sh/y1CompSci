class Shopping:

    def __init__(self):
        self.total = 0

    def spend(self, amount):
        self.total += amount

    def checkout(self):
        discount = 1
        percentage = '0%'
        if self.total >= 100:
            discount = 0.75
            percentage = '25%'
        elif self.total >= 50:
            discount = 0.9
            percentage = '10%'
        self.total = self.total * discount
        return percentage, self.total

def testShopping():
    shopping = Shopping()
    shopping.spend(50)
    shopping.spend(60)
    percentage, total = shopping.checkout()
    print(f"discount is {percentage}, total is {total}")

#testShopping()

class Shopping2:

    def __init__(self):
        self.total = 0

    def spend(self, amount):
        self.total += amount

    def checkout(self):
        discountTotal = 0
        discount = 0
        if self.total >= 100:
            discount = 25
        elif self.total >= 50:
            discount = 10
        discountTotal = self.total * ((100-discount)/100)
        self.total = 0
        return discount, discountTotal

def testShopping2():
    shopping = Shopping2()
    shopping.spend(50)
    shopping.spend(60)
    percentage, total = shopping.checkout()
    print(f"discount is {percentage}%, total is £{total:,.2f}")
    shopping.spend(20)
    percentage, total = shopping.checkout()
    print(f"discount is {percentage}%, total is £{total:,.2f}")
    shopping.spend(75)
    percentage, total = shopping.checkout()
    print(f"discount is {percentage}%, total is £{total:,.2f}")

testShopping2()

