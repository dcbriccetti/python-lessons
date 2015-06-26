from tkinter import *

class Application(Frame):
    def greet(self):
        self.greeting.set("What's up?")

    def createWidgets(self):
        self.greeting = StringVar()
        self.greetingLabel = Label(self, textvariable = self.greeting)
        self.greetingLabel.grid(row = 2, column = 1, columnspan = 2)
        
        self.quitButton = Button(self, text = 'Quit', command = self.quit)
        self.quitButton.grid(row = 3, column = 1, padx = 5, pady = 5)

        self.greetMeButton = Button(self, text = "Greet Me", command = self.greet)
        self.greetMeButton.grid(row = 3, column = 2, padx = 5)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

app = Application()
app.master.title("Greeting Program")
app.mainloop()
