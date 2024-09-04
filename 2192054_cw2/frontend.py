from tkinter import *
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

 # ==== REPEATED WIDGET/FRAME MAKING =============================================================================
        
    # create new adding and editing windows
    def createTopLvl(self): 
        win = Toplevel(self.win)
        frame = Frame(win)
        frame.pack(padx=10, pady=10)
        return frame
    
    def createButton(self, frame, width, text, command, sticky, row, col):
        btn = Button(frame, width= width, text=text, command=command)
        if sticky != None:
            btn.grid(row=row, column=col, sticky=sticky, padx=10, pady=10)
        else:
            btn.grid(row=row, column=col, padx=10, pady=10)
        return btn
    
    def createLabel(self, frame, width, text, sticky, row, col):
        lbl = Label(frame, width=width, text=text)
        if sticky != None:
            lbl.grid(row=row, column=col, sticky=sticky, padx=10, pady=10)
        else:
            lbl.grid(row=row, column=col, padx=10, pady=10)
        return lbl

    def enterConsumptionRate(self, frame, rowNumber): 
        """
        Creates Entry widget for adding/editing a plug
        """

        consumptionRate = StringVar()
        entry = Entry(
            frame,
            width=30,
            textvariable=consumptionRate
            )
        consumptionRate.set("")  
        entry.grid(row=rowNumber, column=1, sticky=W, padx=10, pady=10)
        return entry
    

 # ==== MAIN WINDOW WIDGET CREATION =============================================================================
    def createWidgets(self):
        """
        Creates widgets of self.mainFrame
        """

        def updateToggleAll():
            """
            Update all labels after turn off/on all
            """

            i = 0
            for widget in self.mainFrame.winfo_children():
                if isinstance(widget, Frame):
                    widget.winfo_children()[0].config(text=self.smartHome.getDeviceAt(i))

                    # only increases if the widget is a frame relating to a device
                    i+=1  

        self.createButton(
            self.mainFrame, 20, "Turn on all",
            lambda: [self.smartHome.turnOnAll(), updateToggleAll()],
            W, 0, 0)

        self.createButton(
            self.mainFrame, 20, "Turn off all",
            lambda: [self.smartHome.turnOffAll(), updateToggleAll()],
            E, 0, 0)
    
        for device in self.smartHome.getDevices(): 
            self.deviceWidgets(device)
        
        # instance variable so it can be re-grid in the GUI easily
        lastRow = self.mainFrame.grid_size()[1]
        self.btnAdd = self.createButton(
            self.mainFrame, 20, "Add",
            self.addNewDevice,
            W, lastRow, 0)
    
    def deviceWidgets(self, device): 
        """
        Create device-specific frame containing its label and setter buttons 
        """
        
        miniFrame = Frame(self.mainFrame)
        rowIndex = self.mainFrame.grid_size()[1]
        miniFrame.grid(row=rowIndex, sticky=W)

        deviceLbl = self.createLabel(miniFrame, 25, device, W, 0, 0)

        self.createButton(
            miniFrame, 10, "Toggle",
            lambda: [device.toggleSwitch(), deviceLbl.config(text=device)],
            None, 0, 1)
        
        self.createButton(
            miniFrame, 10, "Edit",
            lambda: self.edit(device, deviceLbl),
            None, 0, 2)
        
        self.createButton(
            miniFrame, 10, "Delete",
            lambda: [self.smartHome.removeDevice(device), miniFrame.destroy()],
            None, 0, 3)

        #returned for swapping self.btnAdd and new device frame
        return miniFrame 
  

 # ==== ADDING DEVICE METHOD =============================================================================
    def addNewDevice(self):
        """
        Creates new window for adding a new device to the smart home system
        """

        addFrame = self.createTopLvl()
        addFrame.master.title("Add Device")

        def makeNewDevice(device):
            """
            Creates device-specific frame to GUI and updates backend
            """

            self.smartHome.addDevice(device)
            widget = self.deviceWidgets(device)

            # swap add button and new widget in the GUI
            row = widget.grid_info()["row"] 
            widget.grid(row=row-1)  
            self.btnAdd.grid(row=row+2) 
        

        def addPlug():
            """
            Create Entry box for consumption rate if plug is selected
            """

            self.createLabel(addFrame, 20, "Enter a consumption rate:", W, 1, 0)

            entry = self.enterConsumptionRate(addFrame, 1)

            def userEntry():
                if validation(entry.get()):
                    device = SmartPlug(int(entry.get()))
                    makeNewDevice(device)
                    addFrame.master.destroy()
                else:
                    invalidMessage = Label(addFrame, fg="red", text="Please enter a valid consumption rate between 0 and 150")
                    invalidMessage.grid(row=2, columnspan=2, sticky=W, padx=10, pady=10)

            entry.bind("<Return>", lambda _: userEntry())


        def addSpeaker():
            """
            Create OptionMenu of platforms if speaker is selected
            """

            self.createLabel(addFrame, 20, "Choose a platform:", W, 1, 0)

            selectedOption = StringVar()
            selectedOption.set("Amazon")
            streamingOptions = OptionMenu(
                addFrame,
                selectedOption,
                "Amazon",
                "Spotify",
                "Apple")
            streamingOptions.grid(row=1, column=1, padx=10, pady=10)

            self.createButton(
                addFrame, 10, "Confirm",
                lambda device = SmartSpeaker(): [
                    device.setStreaming(selectedOption.get()),
                    makeNewDevice(device),
                    addFrame.master.destroy()],
                W, 2, 0)
           
        def clearAddFrame():
            """
            Destroys previous device widgets if selection changes
            """
            for widget in addFrame.winfo_children():
                if widget is not deviceOptions and widget is not promptLbl: # not deviceOptions
                    widget.destroy()

        promptLbl = self.createLabel(addFrame, 20, "Select a device type:", W, 0, 0)

        selection = StringVar()
        deviceOptions = OptionMenu(
            addFrame,
            selection,
            "Plug",
            "Speaker",
            command= lambda _: [
                clearAddFrame(),
                addSpeaker() if selection.get() == "Speaker" else addPlug()]
            )
        deviceOptions.grid(row=0, column=1, sticky=W, padx=10, pady=10)


 # ==== EDITING DEVICE METHOD =============================================================================
    def edit(self, device, mainLabel): 
        """
        Creates new window for editing a specific device
        """

        editFrame = self.createTopLvl()

        if isinstance(device, SmartPlug): 
            editFrame.master.title("Edit Plug")

            self.createLabel(editFrame, 20, "Enter a consumption rate:", W, 0, 0)

            entry = self.enterConsumptionRate(editFrame, 0)

            def userEntry():
                if validation(entry.get()):
                    device.setConsumptionRate(int(entry.get()))
                    mainLabel.config(text= device )
                    editFrame.master.destroy()
                else:
                    invalidMessage = Label(editFrame, fg="red", text="Please enter a valid consumption rate between 0 and 150")
                    invalidMessage.grid(row=2, columnspan=2, sticky=W, padx=10, pady=10)

            entry.bind("<Return>", lambda _: userEntry())

        elif isinstance(device, SmartSpeaker):
            editFrame.master.title("Edit Speaker")

            self.createLabel(editFrame, 20, "Choose a platform:", W, 0, 0)

            selectedOption = StringVar(editFrame)
            selectedOption.set("Amazon")
            streamingOptions = OptionMenu(
                editFrame,
                selectedOption,
                "Amazon",
                "Spotify",
                "Apple",)
            streamingOptions.grid(row=0, column=1, padx=10, pady=10)
            
            self.createButton(
                editFrame, 10, "Confirm",
                lambda: [
                    device.setStreaming(selectedOption.get()),
                    mainLabel.config(text=device),
                    editFrame.master.destroy()],
                W, 1, 0)

# ==== VALIDATE CONSUMPTION RATE =============================================================================
def validation(rate): 
    try:
        rate = int(rate)
        if rate > 150 or rate < 0:
            return False 
        else:
            return True
    except ValueError: # if string
        return False 

# ==== SET UP SYSTEM =============================================================================
def setUpDevice(smartHome):
    devices = ["plug", "speaker"]

    deviceChoice = input("Choose a device: Plug or Speaker: ")
    choice = deviceChoice.lower().strip()

    #validate device choice
    while choice not in devices:
        deviceChoice = input("Please choose a valid device: Plug or Speaker: ")
        choice = deviceChoice.lower().strip()
    
    if choice == devices[0]:
        consumptionRate = input("Consumption Rate: ")

        #validate consumption rate input
        while not validation(consumptionRate):
            print("Please enter a valid consumption rate between 0 and 150")
            consumptionRate = input("Consumption Rate: ")
            
        smartHome.addDevice(SmartPlug(int(consumptionRate)))
    elif choice == devices[1]:
        smartHome.addDevice(SmartSpeaker())
        
def setUpHome():
    mySmartHome = SmartHome()
    print("Enter five devices")

    for _ in range(5): 
        setUpDevice(mySmartHome)

    return mySmartHome

def main():
    smartHome = setUpHome()
    mySystem = SmartHomeSystem(smartHome)
    mySystem.run()

main()