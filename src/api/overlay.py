from tkinter import *

import win32con
import win32gui
from PIL import Image, ImageTk


def setClickthrough(hwnd):
    print("setting window properties")
    try:
        styles = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
        styles |= win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, styles)
        win32gui.SetLayeredWindowAttributes(hwnd, 0, 255, win32con.LWA_ALPHA)
    except Exception as e:
        print(e)


# Dimensions
x_pos = 280
y_pos = 360
width = 760
height = 140

root = Tk()
root.geometry("%dx%d+%d+%d" % (width, height, x_pos, y_pos))
root.overrideredirect(1)  # Remove title bar, minimize, maximize, and close buttons
root.attributes("-transparentcolor", "white", "-topmost", 1)
root.config(bg="white")
root.attributes("-alpha", 1)
root.wm_attributes("-topmost", 1)

bg = Canvas(root, width=width, height=height, bg="black")
setClickthrough(bg.winfo_id())

frame = ImageTk.PhotoImage(
    file="C:\\Users\\abtii\\OneDrive\\Documents\\GitHub\\DBD_RPP\\DBD_RPP\\images\\test.png"
)
bg.create_image(0, 0, anchor=NW, image=frame)
bg.pack()

root.mainloop()
