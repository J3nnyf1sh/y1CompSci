from tkinter import *
from tkinter import messagebox
from backend import *

class SmartHomeSystem:

    def __init__(self, smartHome) -> None:
        self.win = Tk()
        self.win.title("Smart Home System")
        self.mainFrame = Frame(self.win)
        self.mainFrame.pack(padx=10, pady=10)
        self.smartHome = smartHome
    
    def run(self):
        self.createWidgets()
        self.win.mainloop()

    def createTopLvl(self):
        win = Toplevel()
        frame = Frame(win)
        frame.pack(padx=10, pady=10)
        return frame
  
    def enterConsumptionRate(self, frame, r):
        consumptionRate = StringVar()
        entry = Entry(
            frame,
            width=30,
            textvariable=consumptionRate
            )
        consumptionRate.set("")  
        entry.grid(row=r, column=1, pady=10, padx=10)
        return entry

    def edit(self, device, mainLabel): 
        editFrame = self.createTopLvl()

        if isinstance(device, SmartPlug):
            editFrame.master.title("Edit Plug")
            message = Label(editFrame,text = device) 
            message.grid(row=0, column=0, sticky=W, pady=10, padx=10)

            entry = self.enterConsumptionRate(editFrame, 0)

            def editPlug(event):
                cr = entry.get()
                device.setConsumptionRate(int(cr))
                mainLabel.config(text= device )

            entry.bind(
                "<Return>",
                lambda event: editPlug(event) if validation(entry.get()) else 
                messagebox.showerror("Error", "Choose between 0 and 150")
                )
            
        elif isinstance(device, SmartSpeaker):
            editFrame.master.title("Edit Speaker")
            deviceInfo = Label(editFrame, text = f"Streaming: {device.getStreaming()}") 
            deviceInfo.grid(row=0, column=0, sticky=W, pady=10, padx=10)

            for platform in device.platforms:
                btnStreaming = Button(
                    editFrame,
                    text = platform.capitalize(),
                    command = lambda p = platform: [
                    device.setStreaming(p),
                    mainLabel.config(text = device)]
                )
                btnStreaming.grid(row=0, column=editFrame.grid_size()[0], pady=10, padx=10)

    def addSpeaker(self, addFrame):
        lbl = Label(addFrame, text = "Choose a platform:")
        lbl.grid(row=1, column=0, sticky=W, pady=10, padx=10)

        def makeSpeaker(selection):
            device = SmartSpeaker()
            device.setStreaming(selection)
            self.smartHome.addDevices(device)
            widget = self.deviceWidgets(device)
            row = widget.grid_info()["row"]
            widget.grid(row = row - 1)
            self.btnAdd.grid(row = row + 2)

        selectedOption = StringVar(addFrame)
        selectedOption.set("Amazon")
        streamingOptions = OptionMenu(
            addFrame,
            selectedOption,
            "Amazon",
            "Spotify",
            "Apple",)
        streamingOptions.grid(row=1, column=1, pady=10, padx=10)
        
        btnConfirm = Button(
            addFrame,
            text="Confirm",
            command= lambda: makeSpeaker(selectedOption.get())
        )
        btnConfirm.grid(row=2, column=0, sticky=W, pady=10, padx=10)

    def addPlug(self, addFrame):
        lbl = Label(addFrame, text = "Enter a consumption rate: ")
        lbl.grid(row=1, column=0, sticky=W, pady=10, padx=10)

        entry = self.enterConsumptionRate(addFrame, 1)

        def makePlug(event):
            cr = entry.get()  
            device = SmartPlug(int(cr))
            self.smartHome.addDevices(device)
            widget = self.deviceWidgets(device)
            row = widget.grid_info()["row"]
            widget.grid(row=row-1)
            self.btnAdd.grid(row=row+2)

        entry.bind(
                "<Return>",
                lambda event: makePlug(event) if validation(entry.get()) else 
                messagebox.showerror("Error", "Choose between 0 and 150")
                )
         
    def addNewDevice(self):
        addFrame = self.createTopLvl()
        addFrame.master.title("Add Device")

        def clearAddFrame(event):
            for widget in addFrame.winfo_children():
                if widget is not deviceOptions: # not deviceOptions
                    widget.destroy()

        selectedOption = StringVar(addFrame)
        deviceOptions = OptionMenu(
            addFrame,
            selectedOption,
            "Plug",
            "Speaker",
            command= lambda event: [
                clearAddFrame(event),
                self.addSpeaker(addFrame) if selectedOption.get() == "Speaker" else self.addPlug(addFrame)
                ] )
        deviceOptions.grid(row=0, column=0, sticky=W, pady=10, padx=10)

    def deviceWidgets(self, device): # toggle, edit and delete buttons specific to a device
        miniFrame = Frame(self.mainFrame)
        rowIndex = self.mainFrame.grid_size()[1]
        miniFrame.grid(row=rowIndex, sticky=W)

        deviceInfo = Label(miniFrame, text = device) 
        deviceInfo.grid(row=0, column=0, sticky=W, pady=10, padx=10)

        btnToggle = Button(
            miniFrame, 
            text="Toggle",
            command = lambda: [device.toggleSwitch(), deviceInfo.config(text = device)]
            )
        btnToggle.grid(row=0, column=1, pady=10, padx=10)

        btnEdit = Button(
            miniFrame, 
            text="Edit",
            command = lambda d=device, lbl = deviceInfo: self.edit(d, lbl)
            )
        btnEdit.grid(row=0, column=2, pady=10, padx=10)

        btnDelete = Button(
            miniFrame, 
            text="Delete",
            command = lambda: [
                self.smartHome.removeDevice(device),
                miniFrame.destroy()]
            )
        btnDelete.grid(row=0, column=3, pady=10, padx=10)

        return miniFrame
    
    def updateSwitchedOn(self):
        i = 0
        for widget in self.mainFrame.winfo_children():
            if isinstance(widget, Frame):
                widget.winfo_children()[1].config(text = self.smartHome.getDeviceAt(i))
                i+=1
        
    def createWidgets(self):
        btnTurnOnAll = Button(
            self.mainFrame, 
            text="Turn on all",
            command = lambda: [self.smartHome.turnOnAll(), self.updateSwitchedOn()]
            )
        btnTurnOnAll.grid(row=0, column=0, sticky=W, pady=10, padx=10)

        btnTurnOffAll = Button(
            self.mainFrame, 
            text="Turn off all",
            command = lambda: [self.smartHome.turnOffAll(), self.updateSwitchedOn()]
            )
        btnTurnOffAll.grid(row=0, column=1, sticky=W, pady=10, padx=10)

        for device in self.smartHome.getDevices(): 
            self.deviceWidgets(device)
        
        self.btnAdd = Button(
            self.mainFrame, 
            text="Add",
            command = self.addNewDevice
            )
        self.btnAdd.grid(row=self.mainFrame.grid_size()[1], column=0, sticky=W, pady=10, padx=10)

def validation(rate): # validate consumption rate
    try:
        rate = int(rate)
        if rate > 150 or rate < 0:
            return False
        else:
            return True
    except ValueError:
        return False
        
def addDevices(mySmartHome):
    devices = ["plug", "speaker"]
    
    chooseDevice = input("Choose a device: Plug or Speaker: ")
    while chooseDevice.lower() not in devices:
        chooseDevice = input("Choose a valid device: Plug or Speaker: ")
    
    if chooseDevice.lower() == devices[0]: # validate consumption rate
        consumptionRate = input("Consumption Rate: ")
        while not validation(consumptionRate):
            print("Please enter a valid consumption rate between 0 and 150")
            consumptionRate = input("Consumption Rate: ")
        mySmartHome.addDevices(SmartPlug(int(consumptionRate)))
    elif chooseDevice.lower() == devices[1]:
        mySmartHome.addDevices(SmartSpeaker())

def setUpHome():
    mySmartHome = SmartHome()
    print("Enter five devices")
    for i in range(5):
        addDevices(mySmartHome)
    return mySmartHome

def main():
    smartHome = setUpHome()
    mySystem = SmartHomeSystem(smartHome)
    mySystem.run()

main()