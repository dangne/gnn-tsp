from tkinter import *
from PIL import ImageTk, Image

root = Tk()  # create a window

frame = Frame(root)  # define upper frame
middleframe = Frame(root)  # define middle frame
exitFrame = Frame(root)  # define exit frame
frame.pack()  # pack the frame
middleframe.pack()  # pack the subframe
exitFrame.pack(side='bottom')  # pack the exit frame
# function that closes the GUI
def close_window():
    
    root.destroy()


img = ImageTk.PhotoImage(Image.open("southvn.png"))  # load the image
"""959 x 593"""

canvas = Canvas(frame, width=img.width(), height=img.height(), borderwidth=0)
canvas.grid(row=0, column=0)
canvas.create_image(0, 0, image=img, anchor=NW)

# Normalized coordinates list
coor_normalized = []

x_Coordinates = []  # list for storing x-axis coordinates
y_Coordinates = []  # list for storing y-axis coordinates
clicks = 0

x_list = [258, 445, 514, 390, 163, 51, 138, 220, 114, 88, 97, 219, 276, 350, 359, 384, 458, 342, 50, 541, 581, 556, 498, 393, 168, 192, 206, 179, 176, 202, 220, 233, 228, 280, 248, 267, 280]
y_list = [431, 384, 303, 37, 17, 93, 82, 90, 228, 291, 342, 305, 346, 332, 280, 205, 172, 121, 424, 429, 41, 165, 75, 441, 187, 138, 110, 238, 260, 221, 209, 187, 233, 229, 200, 157, 199]
def create_circle(canvas, x, y, radius, **kwargs):
    return canvas.create_oval(x-radius, y-radius, x+radius, y+radius, **kwargs)

def countClicks():
    global clicks

    clicks += 1
    # if the user has selected 2 points, add a button that closes the window
    if clicks == 2:
        # link the closing function to the button
        exit_button = Button(exitFrame, state="normal", text="Done!",
                             command=close_window)
        exit_button.grid(row=2, column=0, pady=5)  # set button position with "grid"

def selectPoints():  # function called when user clicks the button "select two points"
    # link the function to the left-mouse-click event
    canvas.bind("<Button 1>", saveCoordinates)
    # link closing function to the button
    exit_button = Button (exitFrame, state="disabled", text="Done!",
                          command=close_window)
    exit_button.grid(row=2, column=0, pady=5)  # set button position with "grid"
    button_select_points.config(state="disabled") # switch button state to "disabled"

def saveCoordinates(event): # function called when left-mouse-button is clicked
    x_coordinate = event.x  # save x and y coordinates selected by the user
    y_coordinate = event.y

    x_Coordinates.append(x_coordinate)
    y_Coordinates.append(y_coordinate)

    coor_normalized.append(x_coordinate / img.width())
    coor_normalized.append(y_coordinate / img.height())
    # Display a small dot showing position of point.
    create_circle(canvas, x_coordinate, y_coordinate, radius=3, fill='red')
    print(x_Coordinates)
    print(y_Coordinates)
    countClicks()

# insert button and link it to "selectPoints"
button_select_points = Button(middleframe, text="select two points",
                              command=selectPoints)
button_select_points.grid(row=1, column=0, pady=5)

for a, b in zip(x_list,y_list):
    create_circle(canvas, a, b, radius = 5, fill='red')
    

root.mainloop()