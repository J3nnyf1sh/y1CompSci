from tkinter import *

class LoginApp:
    
    def __init__(self, loginDetails):
        self.loginDetails = loginDetails
        self.win = Tk()
        self.win.title("Employee Login")
        self.win.geometry("250x100")

        self.mainFrame = Frame(self.win)
        self.mainFrame.grid(column=0, row=0)

        self.userName = StringVar()
        self.password = StringVar()
        self.message = StringVar()
        self.message.set("Enter username and password.")

    def run(self):
        self.createWidgets()
        self.win.mainloop()

    def createWidgets(self):
        lblMessage = Label(
            self.mainFrame,
            textvariable=self.message,
            width=30
        )
        lblMessage.grid(column=0, row=0, columnspan=2)

        lblUserName = Label(
            self.mainFrame,
            text="Username:"
        )
        lblUserName.grid(column=0, row=1)

        entryUserName = Entry(
            self.mainFrame,
            width=25,
            textvariable=self.userName
        )
        entryUserName.grid(column=1, row=1)

        lblPassword = Label(
            self.mainFrame,
            text="Password:"
        )
        lblPassword.grid(column=0, row=2)

        entryPassword = Entry(
            self.mainFrame,
            width=25,
            textvariable=self.password
        )
        entryPassword.grid(column=1, row=2)

        btnSignIn = Button(
            self.mainFrame,
            text="Sign In",
            command=self.authenticate
        )
        btnSignIn.grid(column=0, row=3)

        btnCancel = Button(
            self.mainFrame,
            text="Cancel",
            command=self.win.destroy
        )
        btnCancel.grid(column=1, row=3)

    def authenticate(self):
        username = self.userName.get()
        password = self.password.get()

        if username not in self.loginDetails:
            self.message.set("Username not found.")
        elif self.loginDetails[username] != password:
            self.message.set("Incorrect password.")
        else:
            self.message.set("Login successful!")


def main():
    companyLoginDetails = {
        "YousefD": "VenterboSS",
        "SergeiT": "25Operyu",
        "Yemi": "Idec704",
        "WernerS": "IAmMel12"
    }
    app = LoginApp(companyLoginDetails)
    app.run()