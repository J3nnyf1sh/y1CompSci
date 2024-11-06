class Laptop:

    ramOptions = {
        4: 0,
        8: 50,
        16: 100,
        32: 200
    }

    ssdOptions = {
        256: 0,
        512: 30,
        1024: 100
    }

    def __init__(self, brand, basePrice):
        self.brand = brand
        self.basePrice = basePrice
        self.ram = 4
        self.ssd = 256

    def getBrand(self):
        return self.brand

    def getRam(self):
        return self.ram
    
    def getSsd(self):
        return self.ssd

    def getPrice(self):
        ramPrice = self.ramOptions[self.ram]
        ssdPrice =self.ssdOptions[self.ssd]
        return self.basePrice + ramPrice + ssdPrice

    def setRam(self, ram):
        if ram in self.ramOptions:
            self.ram = ram
        
    def setSsd(self, ssd):
        if ssd in self.ssdOptions:
            self.ssd = ssd

    def __str__(self):
        output = f"{self.brand} Laptop with {self.ram} GB RAM and {self.ssd} GB SSD"
        output += f"priced at £{self.getPrice()}"
        return output


class ShoppingCart:

    def __init__(self):
        self.laptops = []
        self.total = 0

    def addLaptop(self, laptop):
        self.laptops.append(laptop)
        self.total += laptop.getPrice()

    def getLaptops(self):
        return self.laptops

    def getTotal(self):
        return self.total

    def __str__(self):
        output = "Shopping cart contains:\n"
        for laptop in self.laptops:
            output += f"{laptop}\n"
        output += f"Total price is £{self.total}"
        return output


class GamingLaptop(Laptop):

    gpuOptions = {
        "NVIDIA GTX 1650": 0,
        "NVIDIA RTX 3070": 250,
        "NVIDIA RTX 4080": 350,
        "AMD RX 6800M": 280
    }

    def __init__(self, brand, basePrice):
        super().__init__(brand, basePrice)
        self.gpu = "NVIDIA GTX 1650"

    def getGpu(self):
        return self.gpu

    def setGpu(self, gpu):
        if gpu in self.gpuOptions:
            self.gpu = gpu

    def getPrice(self):
        gpuPrice = self.gpuOptions[self.gpu]
        return super().getPrice() + gpuPrice

    def __str__(self):
        output = f"{self.brand} Laptop with {self.ram} GB RAM "
        output += f"and {self.gpu} priced at £{self.getPrice()}"
        return output


def testLaptop():
    laptop = Laptop("Dell", 999.99)
    print("laptop's brand is", laptop.getBrand())
    print("laptop's RAM is", laptop.getRam())
    print("laptop's price is", laptop.getPrice())  # 999.99

    laptop.setRam(32)
    print("laptop's RAM is now", laptop.getRam())
    laptop.setRam(30)
    print("laptop's RAM is still", laptop.getRam())

    laptop.setSsd(512)
    print("laptop's hard drive capacity is now", laptop.getSsd())
    laptop.setSsd(200)
    print("laptop's hard drive capacity is still", laptop.getSsd())

    print("laptop's price is now", laptop.getPrice())  # 999.99 + 200 = 1199.99

    print(laptop)

testLaptop()

def testShoppingCart():
    cart = ShoppingCart()
    dellLaptop = Laptop("Dell", 999.99)
    appleLaptop = Laptop("Apple", 1349.00)
    msiLaptop = GamingLaptop("MSI", 1599.00)
    msiLaptop.setRam(16)
    msiLaptop.setGpu("AMD RX 6800M0")
    cart.addLaptop(dellLaptop)
    cart.addLaptop(appleLaptop)
    cart.addLaptop(msiLaptop)

    print("Shopping cart contains:")
    for laptop in cart.getLaptops():
        print(laptop)
    print(f"Total price is £{cart.getTotal()}")

    print(cart)


def testGamingLaptop():
    gamingLaptop = GamingLaptop("Razer", 2399.99)
    print("Gaming laptop's brand is", gamingLaptop.getBrand())
    print("Gaming laptop's price is", gamingLaptop.getPrice())
    print("Gaming laptop's ram is", gamingLaptop.getRam())
    print("Gaming laptop's GPU is", gamingLaptop.getGpu())

    gamingLaptop.setGpu("NVIDIA RTX 3070")
    print("Gaming laptop's GPU is now", gamingLaptop.getGpu())
    print("Gaming laptop's price is now", gamingLaptop.getPrice())

    print(gamingLaptop)

class Pizza:

    pizzaPrices = {"small": 8, "medium": 10, "large": 12}

    def __init__(self, size):
        self.toppings = set()
        self.size = "small"
        if size.lower() in self.pizzaPrices:
            self.size = size.lower()

    def addTopping(self, topping):
        self.toppings.add(topping.lower())

    def removeTopping(self, topping):
        self.toppings.discard(topping.lower())

    def setSize(self, newSize):
        if newSize.lower() in self.pizzaPrices:
            self.size = newSize.lower()

    def getSize(self):
        return self.size

    def getPrice(self):
        return self.pizzaPrices[self.size]

    def getToppings(self):
        return self.toppings

    def __str__(self):
        output = f"{self.size} pizza with:"
        for topping in self.toppings:
            output += f"\n- {topping}"
        output += f"\nPrice: £{self.getPrice()}\n"
        return output


class Order:

    def __init__(self):
        self.pizzas = []

    def addPizza(self, pizza):
        self.pizzas.append(pizza)
    
    def changeSize(self, pizza, size):
        if pizza in self.pizzas:
            self.pizzas.remove(pizza)
        
        pizza.setSize(size)
        self.pizzas.append(pizza)

    def addTopping(self, pizza, topping):
        if pizza in self.pizzas:
            self.pizzas.remove(pizza) 
        
        pizza.addTopping(topping)
        self.pizzas.append(pizza)

    def removeTopping(self, pizza, topping):
        if pizza in self.pizzas:
            self.pizzas.remove(pizza) 

        pizza.removeTopping(topping)
        self.pizzas.append(pizza)

    def upgradePizza(self, pizza, crust):
        if pizza in self.pizzas:
            self.pizzas.remove(pizza)
        
        toppings = pizza.getToppings()

        pizza = StuffedCrustPizza(pizza.getSize(), crust)

        for topping in toppings:
            pizza.addTopping(topping)

        self.pizzas.append(pizza)
        return pizza

    def getTotalPrice(self):
        totalPrice = 0
        for pizza in self.pizzas:
            totalPrice += pizza.getPrice()
        return totalPrice

    def __str__(self):
        output = "Your order contains:\n"
        for pizza in self.pizzas:
            output += str(pizza)
        output += f"Total: £{self.getTotalPrice()}"
        return output


class StuffedCrustPizza(Pizza):
    
    crustTypes = ("cheese", "garlic", "hot dog")

    def __init__(self, size, crust):
        super().__init__(size)
        self.crust = "cheese"
        if crust.lower() in self.crustTypes:
            self.crust = crust.lower()

    def getCrust(self):
        return self.crust

    def setCrust(self, newCrust):
        if newCrust in self.crustTypes:
            self.crust = newCrust

    def getPrice(self):
        return super().getPrice() + 2

    def __str__(self):
        output = f"A {self.size} stuffed crust pizza with:"
        for topping in self.toppings:
            output += f"\n- {topping}"
        output += f"\nCrust type: {self.crust}"
        output += f"\nPrice: £{self.getPrice()}\n"
        return output


def test():
    myOrder = Order()
    pizza1 = Pizza("small")
    pizza1.addTopping("Pepperoni")
    pizza1.addTopping("Jalapenos")
    pizza1.setSize("large")

    pizza2 = StuffedCrustPizza("Medium", "Cheese")
    pizza2.addTopping("Ham")
    pizza2.addTopping("Mushrooms")
    pizza2.setCrust("Garlic")

    myOrder.addPizza(pizza1)
    myOrder.addPizza(pizza2)

    print(myOrder)
    myOrder.changeSize(pizza1, "medium")
    print(myOrder)
    myOrder.addTopping(pizza1, "Mushroom")
    print(pizza1)
    myOrder.removeTopping(pizza2, "Jalapenos")
    print(pizza2)
    pizza1 = myOrder.upgradePizza(pizza1, "cheese")
    print(myOrder)
    print(pizza1)

    

test()