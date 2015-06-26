from tkinter import *

class Application(Frame):
    def createWidgets(self):
        self.quitButton = Button(self, text = 'Quit', command = self.quit)
        self.quitButton.pack()
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

app = Application()
app.mainloop()
