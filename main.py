import tkinter
from typing import Set
import cv2
import PIL.Image
import PIL.ImageTk

# Width and Height of Screen

SET_WIDTH = 650
SET_HEIGHT = 368

# Making tkinter GUI

window = tkinter.Tk()
window.title("DRS Review System")  # gives title to the GUI
# Canvas used to draw pictures and add graphics
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
# cv_img = cv2.cvtColor(cv2.imread("welcome.jpg"), cv2.COLOR_BGR2RGB)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
window.mainloop()
