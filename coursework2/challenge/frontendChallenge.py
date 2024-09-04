from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import filedialog
from backendChallenge import *
from datetime import datetime, timedelta
import os


class SmartHomeSystem:

    def __init__(self, smartHome) -> None:
        self.win = Tk()
        self.win.title("Smart Home System")
        self.mainFrame = Frame(self.win)
        self.mainFrame.pack(padx=10, pady=10)

        self.bgColour = "white"
        self.accentColour = "light blue"
        self.fgColour = "black"
        self.font = "Helvetica bold", 10

        directory = os.path.dirname(os.path.abspath(__file__))
        self.speakerIcon = PhotoImage(file=os.path.join(directory, "images", "speaker.png"))
        self.plugIcon = PhotoImage(file=os.path.join(directory, "images", "plug.png"))

        menuBar = Menu(self.mainFrame)
        self.win.config(menu=menuBar)
        
        file = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="File", menu=file)

        file.add_command(label = "Accessibility", command= self.changeAccessibility)
        file.add_command(label="Save", command=self.saveFile)
        file.add_command(label="Open", command=self.loadSave)

        self.hour = 0

        self.smartHome = smartHome
    
    def run(self):
        self.createWidgets()
        self.updateClock()
        self.win.mainloop()

    def createTopLvl(self):
        win = Toplevel()
        frame = Frame(win)
        frame.pack(padx=10, pady=10)
        return frame

    def updateClock(self):
        self.hour = (self.hour + 1) % 24
        time = f"{self.hour:02d}:00"
        self.clock.config(text=time)

        for i, device in enumerate(self.smartHome.getDevices()):
            schedule = device.getSchedule() 
            if schedule is not None:
                hour, action = schedule
                if int(hour) == self.hour:
                    if action == "On" and device.getSwitchedOn() == "Off":
                        device.toggleSwitch()
                        self.updateSwitchedOn()
                    elif action == "Off" and device.getSwitchedOn() == "On":
                        device.toggleSwitch()
                        self.updateSwitchedOn()

        self.win.after(3000, self.updateClock)
                
    
    def addSpeaker(self, addFrame):
        lbl = Label(addFrame, font=self.font, text = "Choose a platform:", width=30)
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
            "Apple",
            )
        streamingOptions.config(font=self.font)
        streamingOptions.grid(row=1, column=1, pady=10, padx=10)
        
        btnConfirm = Button(
            addFrame,
            bg=self.accentColour,
            font=self.font,
            text="Confirm",
            command= lambda: makeSpeaker(selectedOption.get())
        )
        btnConfirm.grid(row=2, column=0, sticky=W, pady=10)

    def addPlug(self, addFrame):
        lbl = Label(addFrame, font=self.font, text = "Enter a consumption rate: ")
        lbl.grid(row=1, column=0, sticky=W, pady=10)

        consumptionRate = StringVar()
        entry = Entry(
            addFrame,
            font=self.font,
            width=30,
            bg=self.bgColour, fg=self.fgColour,
            textvariable=consumptionRate
            )
        consumptionRate.set("")  
        entry.grid(row=1, column=1, pady=10, padx=10)

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
        deviceOptions.config(font=self.font)
        deviceOptions.grid(row=0, column=0, sticky=W, pady=10, padx=10)

    def changeColour(self, fgColour, bgColour, accentColour):
        self.bgColour = bgColour
        self.fgColour = fgColour
        self.accentColour = accentColour
        self.win.configure(bg=self.bgColour)
        self.mainFrame.configure(bg=self.bgColour)
        for widget in self.mainFrame.winfo_children():
            if isinstance(widget, Frame):
                widget.configure(bg=self.bgColour)
                for w in widget.winfo_children():
                    if isinstance(w, Button):
                        w.configure(bg=self.accentColour)
                        w.configure(fg=self.fgColour)
                    else:
                        w.configure(bg=self.bgColour)
                        w.configure(fg=self.fgColour)
            elif isinstance(widget, Button):
                widget.configure(bg=self.accentColour)
                widget.configure(fg=self.fgColour)
            elif isinstance(widget, Label):
                widget.configure(bg=self.bgColour)
                widget.configure(fg=self.fgColour)
    
    def changeFontSize(self, size):
        self.font = 'Helvetica bold', size
        for widget in self.mainFrame.winfo_children():
            if isinstance(widget, Frame):
                for w in widget.winfo_children():
                    w.config(font=self.font)
            else:
                widget.config(font=self.font)

    def changeAccessibility(self):
        settingsFrame = self.createTopLvl()
        settingsFrame.master.title("Accessibility")

        color = Label(settingsFrame, font=self.font, text = "Colour Scheme")
        color.grid(row=0, column=0, stick=W, pady=10, padx=10)

        checkLight = IntVar()
        checkDark = IntVar()
        checkContrast = IntVar()
        checkCustom = IntVar()

        lightMode = Checkbutton(
            settingsFrame,
            font=self.font,
            text = "Light Mode (Default)",
            command= lambda: [
                self.changeColour("black", "white", "blue"),
                darkMode.deselect(),
                contrastMode.deselect(),
                customMode.deselect()]
        )
        lightMode.grid(row=1, column=0, sticky=W, pady=10, padx=10)
        lightMode.select()

        darkMode = Checkbutton(
            settingsFrame,
            font=self.font,
            text="Dark Mode",
            variable=checkDark,
            command= lambda: [
                self.changeColour("white", "gray7", "purple"),
                lightMode.deselect(),
                contrastMode.deselect(),
                customMode.deselect()]
        )
        darkMode.grid(row=2, column=0, sticky=W, pady=10, padx=10)

        contrastMode = Checkbutton(
            settingsFrame,
            font=self.font,
            text="High Contrast Dark",
            variable = checkContrast,
            command= lambda:[
                self.changeColour("red", "gray7", "yellow"),
                darkMode.deselect(),
                lightMode.deselect(),
                customMode.deselect()]
        )
        contrastMode.grid(row=3, column=0, sticky=W, pady=10, padx=10)

        def customChooser():
            colour1 = colorchooser.askcolor(self.fgColour, title="Text Colour")[1]
            colour2 = colorchooser.askcolor(self.bgColour, title="Background Colour")[1]
            colour3 = colorchooser.askcolor(self.accentColour, title="Accent Colour")[1]
            self.changeColour(colour1, colour2, colour3)

        customMode = Checkbutton(
            settingsFrame,
            font=self.font,
            text="Custom",
            variable=checkCustom,
            command= lambda:[
                customChooser(),
                darkMode.deselect(),
                lightMode.deselect(),
                contrastMode.deselect()
            ]
        )
        customMode.grid(row=4, column=0, sticky=W, pady=10, padx=10)

        textLabel = Label(
            settingsFrame,
            font=self.font,
            text="Text size: "
        )
        textLabel.grid(row=5, column=0, sticky=W, pady=10, padx=10)

        sizeChanger = Spinbox(
            settingsFrame,
            font=self.font,
            from_=1, to=20,
            command= lambda: self.changeFontSize(sizeChanger.get())
        )
        sizeChanger.delete(0, "end")
        sizeChanger.insert(0, self.font[1])
        sizeChanger.config(state="readonly")
        sizeChanger.grid(row=5, column=1, pady=10, padx=10)

    def deviceWidgets(self, device): # toggle, edit and delete buttons specific to a device
        miniFrame = Frame(self.mainFrame)
        rowIndex = self.mainFrame.grid_size()[1]
        miniFrame.grid(row=rowIndex, sticky=W)

        if isinstance(device, SmartPlug):
            photo  = self.plugIcon
        else:
            photo = self.speakerIcon

        devicePhoto = Label(miniFrame, image=photo)
        devicePhoto.grid(row=0, column=0, pady=10, padx=10, sticky=W)
        deviceInfo = Label(miniFrame, font=self.font, text = device, width=25) 
        deviceInfo.grid(row=0, column=1, pady=10, padx=10)

        btnToggle = Button(
            miniFrame, 
            width=10,
            bg=self.accentColour,
            font=self.font,
            text="Toggle",
            command = lambda: [device.toggleSwitch(), deviceInfo.config(text = device)]
            )
        btnToggle.grid(row=0, column=2, pady=10, padx=10)

        if isinstance(device, SmartPlug):
            consumptionRate = IntVar()
            crScale = Scale(
                miniFrame,
                font=self.font,
                activebackground = "red",
                variable = consumptionRate,
                from_=0, to=150,
                sliderlength = 15,
                length = 305,
                tickinterval = 50,
                orient = HORIZONTAL,
                command = lambda event:[
                    device.setConsumptionRate(consumptionRate.get()),
                    deviceInfo.config(text = device)]
            )
            consumptionRate.set(device.getConsumptionRate())
            crScale.grid(row=0, column=3, sticky=N, pady=10, padx=10)
        else:
            for platform in device.platforms:
                btnStreaming = Button(
                    miniFrame,
                    width=10,
                    bg=self.accentColour,
                    font=self.font,
                    text = platform.capitalize(),
                    command = lambda p = platform: [
                    device.setStreaming(p),
                    deviceInfo.config(text = device)]
                )
                btnStreaming.grid(row=0, column=miniFrame.grid_size()[0], pady=10, padx=10)

        btnSchedule = Button(
            miniFrame,
            width=10,
            bg=self.accentColour,
            font=self.font,
            text="Schedule",
            command = lambda: self.setSchedule(device, miniFrame)
        )
        btnSchedule.grid(row=0, column=miniFrame.grid_size()[0], pady=10, padx=10)

        scheduleLbl = Label(
            miniFrame,
            width=20,
            font=self.font,
            text="No schedule set"
        )
        scheduleLbl.grid(row=0, column=miniFrame.grid_size()[0], pady=10, padx=10)

        if device.getSchedule() != None:
            scheduleLbl.config(text=f"Device will turn {device.getSchedule()[1]} at {device.getSchedule()[0]}:00")

        btnDelete = Button(
            miniFrame, 
            width=10,
            bg=self.accentColour,
            font=self.font,
            text="Delete",
            command = lambda: [
                self.smartHome.removeDevice(device),
                miniFrame.destroy()]
            )
        btnDelete.grid(row=0, column=miniFrame.grid_size()[0], pady=10, padx=10)

        return miniFrame
    
    def setSchedule(self, device, miniFrame):
        scheduleFrame = self.createTopLvl()
        scheduleFrame.master.title("Set Schedule")

        l = Label(scheduleFrame, text="Turn device ", font=self.font)
        l.grid(row=0, column=0)

        selectedOption = StringVar()
        selectedOption.set("On")
        onOff = OptionMenu(
            scheduleFrame,
            selectedOption,
            "On",
            "Off"
        )
        onOff.config(font=self.font)
        onOff.grid(row=0, column=1)

        l2 = Label(scheduleFrame, text=" at")
        l2.grid(row=0, column=2)

        time = Spinbox(
            scheduleFrame,
            font=self.font,
            from_=0, to=23
        )
        time.config(state="readonly")
        time.grid(row=0, column=3, pady=10, padx=10)

        def makeSchedule():
            device.setSchedule(time.get(), selectedOption.get())
            miniFrame.winfo_children()[-2].config(text=f"Device will turn {selectedOption.get()} at {time.get()}:00", font=self.font)

        btnConfirm = Button(
            scheduleFrame,
            width=20,
            bg=self.accentColour,
            font=self.font,
            text="Confirm",
            command=lambda: makeSchedule() 
        )
        btnConfirm.grid(row=1, sticky=W)

    def updateSwitchedOn(self):
        i = 0
        for widget in self.mainFrame.winfo_children():
            if isinstance(widget, Frame):
                widget.winfo_children()[1].config(text = self.smartHome.getDeviceAt(i))
                i+=1
        
    def createWidgets(self):

        btnTurnOnAll = Button(
            self.mainFrame, 
            width=20,
            bg=self.accentColour,
            font=self.font,
            text="Turn on all",
            command = lambda: [self.smartHome.turnOnAll(), self.updateSwitchedOn()]
            )
        btnTurnOnAll.grid(row=0, column=0, sticky=W, pady=10, padx=10)

        self.clock = Label(self.mainFrame, width=20, font=self.font, bg=self.bgColour, fg=self.fgColour)
        self.clock.grid(row=0, column=0, pady=10, padx=10)

        btnTurnOffAll = Button(
            self.mainFrame, 
            width=20,
            bg=self.accentColour,
            font=self.font,
            text="Turn off all",
            command = lambda: [self.smartHome.turnOffAll(), self.updateSwitchedOn()]
            )
        btnTurnOffAll.grid(row=0, column=0, sticky=E, pady=10, padx=10)

        for device in self.smartHome.getDevices(): 
            self.deviceWidgets(device)
        
        self.btnAdd = Button(
            self.mainFrame, 
            width=20,
            bg=self.accentColour,
            font=self.font,
            text="Add",
            command = self.addNewDevice
            )
        self.btnAdd.grid(row=self.mainFrame.grid_size()[1], column=0, sticky=W, pady=10, padx=10)

    def saveFile(self):
        filePath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if filePath:
            try:
                with open(filePath, 'w') as file:  
                    for device in self.smartHome.getDevices():
                        if isinstance(device, SmartPlug):
                            file.write(f"SmartPlug: {device.getConsumptionRate()}: {device.getSwitchedOn()}")
                        elif isinstance(device, SmartSpeaker):
                            file.write(f"SmartSpeaker: {device.getStreaming()}: {device.getSwitchedOn()}")

                        schedule = device.getSchedule()
                        if schedule is not None:
                            file.write(f": {schedule[0]}: {schedule[1]}")
                        
                        file.write("\n")

                    file.write(f"Background: {self.bgColour}\nForeground: {self.fgColour}\nAccent: {self.accentColour}\nText: {self.font[1]}")
            except Exception as e:
                messagebox.showerror("Error", "An error occurred while trying to save")

    def loadSave(self):
        save = messagebox.askyesno("Save?", "Would you like to save the current smart home?")
        if save == True:
            self.saveFile()

        filePath = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if filePath:
            try:
                savedSmartHome = SmartHome()
                with open(filePath, 'r') as file:
                    lines = file.readlines()
                    for line in lines:
                        if line.startswith("SmartPlug:") or line.startswith("SmartSpeaker:"):
                            parts = line.split(":")
                            if line.startswith("SmartPlug:"):
                                consumptionRate = int(parts[1].strip())
                                device = SmartPlug(consumptionRate)
                                savedSmartHome.addDevices(device)
                            elif line.startswith("SmartSpeaker:"):
                                streaming = parts[1].strip()
                                device = SmartSpeaker()
                                device.setStreaming(streaming)
                                savedSmartHome.addDevices(device)

                            if parts[2].strip() == "On":
                                device.toggleSwitch()

                            if len(parts) >= 5:
                                hour = parts[3].strip()
                                action = parts[4].strip()
                                device.setSchedule(hour, action)
                
                        elif line.startswith("Background:"):
                            bgColour = line.split(":")[1].strip()
                        elif line.startswith("Foreground:"):
                            fgColour = line.split(":")[1].strip()
                        elif line.startswith("Accent:"):
                            accentColour = line.split(":")[1].strip()
                        elif line.startswith("Text:"):
                            fontSize = line.split(":")[1].strip()

                for widget in self.mainFrame.winfo_children():
                    if isinstance(widget, Button) or isinstance(widget, Frame):
                        widget.destroy()
                self.smartHome = savedSmartHome
                self.createWidgets()
                self.changeColour(fgColour, bgColour, accentColour)
                self.changeFontSize(fontSize)
            except Exception as e:
                messagebox.showerror("Error", "An error occurred while trying to load the save")

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