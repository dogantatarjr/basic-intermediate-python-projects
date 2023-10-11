from tkinter import Label, Tk
import time

appWindow = Tk()
appWindow.title("Digital Clock")
appWindow.geometry("420x150")
appWindow.resizable(1,1)

textFont = ("Boulder", 68, 'bold')
background = "#000000"
foreground = "#ffffff"
borderWidth = 25

label = Label(appWindow, font=textFont, bg=background, fg=foreground, bd=borderWidth)
label.grid(row=0, column=1)

def digitalClock():
    timeLive = time.strftime("%H:%M:%S")
    label.config(text=timeLive)
    label.after(200, digitalClock)

digitalClock()
appWindow.mainloop()