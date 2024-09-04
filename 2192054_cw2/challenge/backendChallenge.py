class SmartDevice:

    onOff = {
        True: "On",
        False: "Off"
    } # User friendly print statements

    def __init__(self) -> None:
        self.switchedOn = False
        self.schedule = None
    
    def toggleSwitch(self):
        self.switchedOn = not self.switchedOn
    
    def getSwitchedOn(self):
        return self.onOff[self.switchedOn]
    
    def setSchedule(self, hour, onOff):
        self.schedule = hour , onOff
    
    def removeSchedule(self):
        self.schedule = None

    def getSchedule(self):
        return self.schedule

class SmartPlug(SmartDevice):

    def __init__(self, consumptionRate) -> None:
        super().__init__()
        self.consumptionRate = consumptionRate

    def getConsumptionRate(self):
        return self.consumptionRate
    
    def setConsumptionRate(self, rate):
        self.consumptionRate = rate
    
    def __str__(self) -> str:
        output = f"Plug: {self.getSwitchedOn()}, Consumption: {self.getConsumptionRate()}"
        return output

class SmartSpeaker(SmartDevice):
    
    platforms = ("amazon", "spotify", "apple")

    def __init__(self) -> None:
        super().__init__()
        self.streaming = "Amazon"
    
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
        output = f"\nYour Devices:\n"
        for device in self.devices:
            output += str(device) + "\n\n"
        return output

def testSmartPlug():
    mySmartPlug = SmartPlug(45)
    mySmartPlug.toggleSwitch()
    print(mySmartPlug.getSwitchedOn())
    mySmartPlug.setConsumptionRate(100)
    print(mySmartPlug.getConsumptionRate())
    print(mySmartPlug)

def testSmartSpeaker():
    mySmartSpeaker = SmartSpeaker()
    mySmartSpeaker.toggleSwitch()
    print(mySmartSpeaker.getSwitchedOn())
    print(mySmartSpeaker.getStreaming())
    mySmartSpeaker.setStreaming("spotify")
    print(mySmartSpeaker)

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

        
