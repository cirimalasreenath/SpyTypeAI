from tkinter import Tk
from app.gui import KeyLoggerGUI

if __name__ == "__main__":
    root = Tk()
    root.geometry("400x400")
    app = KeyLoggerGUI(root)
    root.mainloop()
