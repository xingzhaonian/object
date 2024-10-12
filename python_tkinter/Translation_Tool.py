import tkinter
import requests


class Translation(object):

    def __init__(self, window) -> None:
        self.window = window
        tkinter.Frame(self.window)



def RunTranslationTool() -> None:
    window = tkinter.Tk()
    run = Translation(window)
    window.mainloop()

RunTranslationTool()