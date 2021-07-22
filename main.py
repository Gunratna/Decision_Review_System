import tkinter
import cv2
import PIL.Image
import PIL.ImageTk
from functools import partial
import threading
import imutils
import time

# reading images

path1 = r'C:\Users\Gunratna\Desktop\Python\DRS_review_system\welcome.jpg'
welcome_img = cv2.imread(path1)
path2 = r'C:\Users\Gunratna\Desktop\Python\DRS_review_system\pending.jpg'
pending_img = cv2.imread(path2)
path3 = r'C:\Users\Gunratna\Desktop\Python\DRS_review_system\out.jpg'
out_img = cv2.imread(path3)
path4 = r'C:\Users\Gunratna\Desktop\Python\DRS_review_system\not_out.jpg'
not_out_img = cv2.imread(path4)

# reading the video clip

path5 = r'C:\Users\Gunratna\Desktop\Python\DRS_review_system\clip.mp4'
clip = cv2.VideoCapture(path5)

# creating functions to add functionality when buttons are clicked


def play(speed):
    print(f"You clicked on play. speed is {speed}")

    # play in reverse/forward mode
    # if we are on f(th) frame and speed(specified by user) is n(+ve or -ve) then our current frame will become (f + n)th frame
    frame1 = clip.get(cv2.CAP_PROP_POS_FRAMES)
    clip.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed, frame = clip.read()
    if not grabbed:
        exit()

    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    # framearray gives tkinter compatible image
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    # display a text when video is being played
    canvas.create_text(200, 26, fill="black",
                       font="Times 40 bold", text="Decision Pending")


def pending(decision):

    # 1. Display decision pending image

    frame = cv2.cvtColor(pending_img, cv2.COLOR_BGR2RGB)
    # resize the image that is stored in frame
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    # 2. Wait for 3 second

    time.sleep(3)

    # 3. Display out/notout image

    if decision == 'out':
        frame = cv2.cvtColor(out_img, cv2.COLOR_BGR2RGB)
    elif decision == 'not out':
        frame = cv2.cvtColor(not_out_img, cv2.COLOR_BGR2RGB)

    # resize the image that is stored in frame
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    # 4. Wait for 3 second

    time.sleep(3)


def out():
    # thread allows us to run multiple parts of program concurruntly and this runs the pending function
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1  # The Daemon Thread does not block the main thread from exiting and continues to run in the background
    thread.start()
    print("Player is out")


def not_out():
    # thread allows us to run multiple parts of program concurruntly and this runs the pending function
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1  # The Daemon Thread does not block the main thread from exiting and continues to run in the background
    thread.start()
    print("Player is not out")


# Width and Height of Screen
SET_WIDTH = 971
SET_HEIGHT = 600

# Tkinter GUI

window = tkinter.Tk()
window.title("Decision Review System")  # gives title to the GUI
# Canvas used to draw pictures and add graphics
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)

# converts image into RGB
cv_img = cv2.cvtColor(welcome_img, cv2.COLOR_BGR2RGB)

# converts the input image into array which is tkinter compatible
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))

canvas_image = canvas.create_image(0, 0, ancho=tkinter.NW, image=photo)
canvas.pack()

# Buttons to control the run-out clip

btn = tkinter.Button(window, text="<< Previous (fast)",
                     width=50, command=partial(play, -25))
btn.pack()

btn = tkinter.Button(window, text="<< Previous (slow)",
                     width=50, command=partial(play, -2))
btn.pack()

btn = tkinter.Button(window, text="Forward (fast) >>",
                     width=50, command=partial(play, 25))
btn.pack()

btn = tkinter.Button(window, text="Forward (slow) >>",
                     width=50, command=partial(play, 2))
btn.pack()

# Buttons to control out and not out

btn = tkinter.Button(window, text="Give out", width=50,
                     command=out)
btn.pack()

btn = tkinter.Button(window, text="Give not out",
                     width=50, command=not_out)
btn.pack()

window.mainloop()
