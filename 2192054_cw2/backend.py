class SmartPlug:

    # more user-friendly format
    onOff = {
        True: "On",
        False: "Off"
    } 

    def __init__(self, consumptionRate) -> None:
        self.switchedOn = False
        self.consumptionRate = consumptionRate

    def toggleSwitch(self):
        self.switchedOn = not self.switchedOn
    
    def getSwitchedOn(self):
        return self.onOff[self.switchedOn]
    
    def getConsumptionRate(self):
        return self.consumptionRate
    
    def setConsumptionRate(self, rate):
        self.consumptionRate = rate
    
    def __str__(self) -> str:
        output = f"Plug: {self.getSwitchedOn()}, Consumption: {self.getConsumptionRate()}"
        return output
    
class SmartSpeaker:
    platforms = ["amazon", "spotify", "apple"]
    onOff = {
        True: "On",
        False: "Off"
    }

    def __init__(self) -> None:
        self.switchedOn = False
        self.streaming = "Amazon"
    
    def toggleSwitch(self):
        self.switchedOn = not self.switchedOn
    
    def getSwitchedOn(self):
        return self.onOff[self.switchedOn]
    
    def getStreaming(self):
        return self.streaming

    def setStreaming(self, streaming):
        if streaming.lower() in self.platforms:
            self.streaming = streaming.capitalize()
        
    def __str__(self) -> str:
        output = f"Speaker: {self.getSwitchedOn()}, Streaming: {self.getStreaming()}"
        return output

class SmartHome:
    
    def __init__(self) -> None:
        self.devices = []
    
    def getDevices(self):
        return self.devices
    
    def getDeviceAt(self, index):
        return self.devices[index]
    
    def addDevice(self, device):
        self.devices.append(device)
    
    def removeDevice(self, device):
        self.devices.remove(device)

    def toggleSwitch(self, index):
        self.devices[index].toggleSwitch()
    
    def turnOnAll(self):
        for device in self.devices:
            device.switchedOn = True
    
    def turnOffAll(self):
        for device in self.devices:
            device.switchedOn = False
    
    def __str__(self) -> str:
        output = f"Your Devices:\n"
        for device in self.devices:
            output += str(device)
            output += "\n\n"
        return output

def testSmartPlug():
    mySmartPlug = SmartPlug(45)

    mySmartPlug.toggleSwitch()
    print(mySmartPlug.getSwitchedOn())

    mySmartPlug.setConsumptionRate(100)
    print(mySmartPlug.getConsumptionRate())

    print(mySmartPlug)

    print("\n")

def testSmartSpeaker():
    mySmartSpeaker = SmartSpeaker()

    mySmartSpeaker.toggleSwitch()
    print(mySmartSpeaker.getSwitchedOn())

    print(mySmartSpeaker.getStreaming())
    mySmartSpeaker.setStreaming("spotify")
    print(mySmartSpeaker)

    print("\n")

def testSmartHome():
    smartHome = SmartHome()
    device1 = SmartPlug(45)
    device2 = SmartPlug(45)
    device3 = SmartSpeaker()

    device1.toggleSwitch()
    device1.setConsumptionRate(150)

    device2.toggleSwitch()
    device3.setStreaming("spotify")

    smartHome.addDevice(device1)
    smartHome.addDevice(device2)
    smartHome.addDevice(device3)

    smartHome.toggleSwitch(1)
    print(smartHome)

    smartHome.turnOnAll()
    print(smartHome)

testSmartPlug()
testSmartSpeaker()
testSmartHome()

        
