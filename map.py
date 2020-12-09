from tkinter import *
from PIL import ImageTk, Image
root = Tk()  # create a window

frame = Frame(root)  # define upper frame
middleframe = Frame(root)  # define middle frame
exitFrame = Frame(root)  # define exit frame
frame.pack()  # pack the frame
middleframe.pack()  # pack the subframe
exitFrame.pack(side='bottom')  # pack the exit frame

x_list = [258, 445, 514, 390, 163, 51, 138, 220, 114, 88, 97, 219, 276, 350, 359, 384, 458, 342, 50, 541, 581, 556, 498, 393, 168, 192, 206, 179, 176, 202, 220, 233, 228, 280, 248, 267, 280]
y_list = [431, 384, 303, 37, 17, 93, 82, 90, 228, 291, 342, 305, 346, 332, 280, 205, 172, 121, 424, 429, 41, 165, 75, 441, 187, 138, 110, 238, 260, 221, 209, 187, 233, 229, 200, 157, 199]

img = ImageTk.PhotoImage(Image.open("Desktop/southvn.png"))  # PIL solution

canvas = Canvas(frame, width=img.width(), height=img.height(), borderwidth=0)
canvas.grid(row=0, column=0)
canvas.create_image(0, 0, image=img, anchor=NW)

vars = []
var  = IntVar()
var_1 = IntVar()
var_2 = IntVar()
var_3 = IntVar()
var_4 = IntVar()
var_5 = IntVar()
var_6 = IntVar()
var_7 = IntVar()
var_8 = IntVar()
var_9 = IntVar()
var_10 = IntVar()
var_11 = IntVar()
var_12 = IntVar()
var_13 = IntVar()
var_14 = IntVar()
var_15 = IntVar()
var_16 = IntVar()
var_17 = IntVar()
var_18 = IntVar()
var_19 = IntVar()
var_20 = IntVar()
var_21 = IntVar()
var_22 = IntVar()
var_23 = IntVar()
var_24 = IntVar()
var_25 = IntVar()
var_26 = IntVar()
var_27 = IntVar()
var_28 = IntVar()
var_29 = IntVar()
var_30 = IntVar()
var_31 = IntVar()
var_32 = IntVar()
var_33 = IntVar()
var_34 = IntVar()
var_35 = IntVar()
var_36 = IntVar()
var_37 = IntVar()

# init list to store coordinates
coordinates = []

# a coordination dictionary

coor_dict = {
    '1' : [258,431],
    '2' : [445,384],
    '3' : [514,303],
    '4' : [390,37],
    '5' : [163,17],
    '6' : [51,93],
    '7' : [138,82],
    '8' : [220,90],
    '9' : [114,228],
    '10' : [88,291],
    '11' : [97,342],
    '12' : [219,305],
    '13' : [276,346],
    '14' : [350,332],
    '15' : [359,280],
    '16' : [384,205],
    '17' : [458,172],
    '18' : [342,121],
    '19' : [50,424],
    '20' : [541,429],
    '21' : [581,41],
    '22' : [556,165],
    '23' : [498,75],
    '24' : [393,441],
    '25' : [168,187],
    '26' : [192,138],
    '27' : [206,110],
    '28' : [179,238],
    '29' : [176,260],
    '30' : [202,221],
    '31' : [220,209],
    '32' : [233,187],
    '33' : [228,233],
    '34' : [280,229],
    '35' : [248,200],
    '36' : [267,157],
    '37' : [280,199]
}

def route():
    selected_list = []
    for var in (var_1, var_2, var_3, var_4, var_5, var_6, var_7, var_8, var_9, var_10, var_11, var_12, var_13, var_14, var_15, var_16, var_17, var_18, var_19, var_20, var_21, var_22, var_23, var_24, var_25, var_26, var_27, var_28, var_29, var_30, var_31, var_32, var_33, var_34, var_35, var_36, var_37):
        #print(var.get())
        if var.get() > 0:
            selected_list.append(var.get())
    
    
    for i in range(len(selected_list)):
        if str(selected_list[i]) in coor_dict:
            coordinates.append(coor_dict[str(selected_list[i])][0])
            coordinates.append(coor_dict[str(selected_list[i])][1])

    print(selected_list)
    print("coordinates: ", coordinates)
    # print(len(coordinates))
    for a in range(len(coordinates)):
        if a % 2 == 0:
            coordinates[a] /= img.width()
        else:
            coordinates[a] /= img.height()
    print("standarized coordinates: ", coordinates)

"""
BUTTON, WHEN PRESSED RETURN NORMALIZED COORDINATES OF SELECTED POINTS
"""

button_print_coor = Button(middleframe, text="Add destination", command = route)
button_print_coor.grid(row=1, column=1, pady=5)


var = IntVar()

Checkbutton(root, variable = var_1, onvalue = 1, offvalue = 0, padx = 0, pady = 0).place(x=coor_dict['1'][0], y=coor_dict['1'][1])
Checkbutton(root, variable = var_2, onvalue = 2, offvalue = 0, padx = 0, pady = 0).place(x=coor_dict['2'][0], y=coor_dict['2'][1])
Checkbutton(root, variable = var_3, onvalue = 3, offvalue = 0, padx = 0, pady = 0).place(x=coor_dict['3'][0], y=coor_dict['3'][1])
Checkbutton(root, variable = var_4, onvalue = 4, offvalue = 0, padx = 0, pady = 0).place(x=coor_dict['4'][0], y=coor_dict['4'][1])
Checkbutton(root, variable = var_5, onvalue = 5, offvalue = 0, padx = 0, pady = 0).place(x=coor_dict['5'][0], y=coor_dict['5'][1])
Checkbutton(root, variable = var_6, onvalue = 6, offvalue = 0, padx = 0, pady = 0).place(x=coor_dict['6'][0], y=coor_dict['6'][1])
Checkbutton(root, variable = var_7, onvalue = 7, offvalue = 0, padx = 0, pady = 0).place(x=coor_dict['7'][0], y=coor_dict['7'][1])
Checkbutton(root, variable = var_8, onvalue = 8, offvalue = 0, padx = 0, pady = 0).place(x=coor_dict['8'][0], y=coor_dict['8'][1])
Checkbutton(root, variable = var_9, onvalue = 9, offvalue = 0, padx = 0, pady = 0).place(x=coor_dict['9'][0], y=coor_dict['9'][1])
Checkbutton(root, variable = var_10, onvalue = 10, offvalue = 0, padx = 0, pady = 0).place(x=coor_dict['10'][0], y=coor_dict['10'][1])
Checkbutton(root, variable = var_11, onvalue = 11, offvalue = 0, padx = 0, pady = 0).place(x=coor_dict['11'][0], y=coor_dict['11'][1])
Checkbutton(root, variable = var_12, onvalue = 12, offvalue = 0, padx = 0, pady = 0).place(x=coor_dict['12'][0], y=coor_dict['12'][1])
Checkbutton(root, variable = var_13, onvalue = 13, offvalue = 0, padx = 0, pady = 0).place(x=coor_dict['13'][0], y=coor_dict['13'][1])
Checkbutton(root, variable = var_14, onvalue = 14, offvalue = 0, padx = 0, pady = 0).place(x=coor_dict['14'][0], y=coor_dict['14'][1])
Checkbutton(root, variable = var_15, onvalue = 15, offvalue = 0, padx = 0, pady = 0).place(x=coor_dict['15'][0], y=coor_dict['15'][1])
Checkbutton(root, variable = var_16, onvalue = 16, offvalue = 0, padx = 0, pady = 0).place(x=coor_dict['16'][0], y=coor_dict['16'][1])
Checkbutton(root, variable = var_17, onvalue = 17, offvalue = 0, padx = 0, pady = 0).place(x=coor_dict['17'][0], y=coor_dict['17'][1])
Checkbutton(root, variable = var_18, onvalue = 18, offvalue = 0, padx = 0, pady = 0).place(x=coor_dict['18'][0], y=coor_dict['18'][1])
Checkbutton(root, variable = var_19, onvalue = 19, offvalue = 0, padx = 0, pady = 0).place(x=coor_dict['19'][0], y=coor_dict['19'][1])
Checkbutton(root, variable = var_20, onvalue = 20, offvalue = 0, padx = 0, pady = 0).place(x=coor_dict['20'][0], y=coor_dict['20'][1])
Checkbutton(root, variable = var_21, onvalue = 21, offvalue = 0, padx = 0, pady = 0).place(x=coor_dict['21'][0], y=coor_dict['21'][1])
Checkbutton(root, variable = var_22, onvalue = 22, offvalue = 0, padx = 0, pady = 0).place(x=coor_dict['22'][0], y=coor_dict['22'][1])
Checkbutton(root, variable = var_23, onvalue = 23, offvalue = 0, padx = 0, pady = 0).place(x=coor_dict['23'][0], y=coor_dict['23'][1])
Checkbutton(root, variable = var_24, onvalue = 24, offvalue = 0, padx = 0, pady = 0).place(x=coor_dict['24'][0], y=coor_dict['24'][1])
Checkbutton(root, variable = var_25, onvalue = 25, offvalue = 0, padx = 0, pady = 0).place(x=coor_dict['25'][0], y=coor_dict['25'][1])
Checkbutton(root, variable = var_26, onvalue = 26, offvalue = 0, padx = 0, pady = 0).place(x=coor_dict['26'][0], y=coor_dict['26'][1])
Checkbutton(root, variable = var_27, onvalue = 27, offvalue = 0, padx = 0, pady = 0).place(x=coor_dict['27'][0], y=coor_dict['27'][1])
Checkbutton(root, variable = var_28, onvalue = 28, offvalue = 0, padx = 0, pady = 0).place(x=coor_dict['28'][0], y=coor_dict['28'][1])
Checkbutton(root, variable = var_29, onvalue = 29, offvalue = 0, padx = 0, pady = 0).place(x=coor_dict['29'][0], y=coor_dict['29'][1])
Checkbutton(root, variable = var_30, onvalue = 30, offvalue = 0, padx = 0, pady = 0).place(x=coor_dict['30'][0], y=coor_dict['30'][1])timer = Timer(path)
Checkbutton(root, variable = var_31, onvalue = 31, offvalue = 0, padx = 0, pady = 0).place(x=coor_dict['31'][0], y=coor_dict['31'][1])
Checkbutton(root, variable = var_32, onvalue = 32, offvalue = 0, padx = 0, pady = 0).place(x=coor_dict['32'][0], y=coor_dict['32'][1])
Checkbutton(root, variable = var_33, onvalue = 33, offvalue = 0, padx = 0, pady = 0).place(x=coor_dict['33'][0], y=coor_dict['33'][1])
Checkbutton(root, variable = var_34, onvalue = 34, offvalue = 0, padx = 0, pady = 0).place(x=coor_dict['34'][0], y=coor_dict['34'][1])
Checkbutton(root, variable = var_35, onvalue = 35, offvalue = 0, padx = 0, pady = 0).place(x=coor_dict['35'][0], y=coor_dict['35'][1])
Checkbutton(root, variable = var_36, onvalue = 36, offvalue = 0, padx = 0, pady = 0).place(x=coor_dict['36'][0], y=coor_dict['36'][1])
Checkbutton(root, variable = var_37, onvalue = 37, offvalue = 0, padx = 0, pady = 0).place(x=coor_dict['37'][0], y=coor_dict['37'][1])


# --------------------- DRAW PATH -------------------

# RESULT FROM DANG
path = ['1', '6', '10', '2', '30', '1']

class Timer:
    def __init__(self, path):
        self.iteration = 0
        canvas.after(10, self.draw_line)
        self.pointList = pathPoints(path)
        print(len(self.pointList))

    def draw_line(self):
        #print(self.iteration)
        A = self.pointList[self.iteration]
        B = self.pointList[self.iteration + 1]
        canvas.create_line(A[0], A[1], B[0], B[1], width=4)
        if (self.iteration < len(self.pointList) - 2):
            self.iteration += 1
        else:
            self.do_nothing()
        canvas.after(10, self.draw_line)
    
    def do_nothing(self):
        pass

    
def __plotLineLow(x0,y0, x1,y1):
    points = []
    dx = x1 - x0
    dy = y1 - y0
    yi = 1
    if dy < 0:
        yi = -1
        dy = -dy
    D = 2*dy - dx
    y = y0

    for x in range( x0, x1 ):
        points.append( (x,y) )
        if D > 0:
           y = y + yi
           D = D - 2*dx
        D = D + 2*dy
    return points

def __plotLineHigh(x0,y0, x1, y1):
    points = []
    dx = x1 - x0
    dy = y1 - y0
    xi = 1
    if dx < 0:
        xi = -1
        dx = -dx
    D = 2*dx - dy
    x = x0

    for y in range(y0, y1):
        points.append( (x,y) )
        if D > 0:
            x = x + xi
            D = D - 2*dy
        D = D + 2*dx
    return points

def linePoints(pointA, pointB):
    """ Generate a list of integer points on the line pointA -> pointB """
    x0, y0 = pointA
    x1, y1 = pointB
    points = []
    if ( abs(y1 - y0) < abs(x1 - x0) ):
        if ( x0 > x1 ):
            points += __plotLineLow( x1, y1, x0, y0 )
        else:
            points += __plotLineLow( x0, y0, x1, y1 )
    else:
        if ( y0 > y1 ):
            points += __plotLineHigh( x1, y1, x0, y0 )
        else:
            points += __plotLineHigh( x0, y0, x1, y1 )
    
    font_x = points[0][0]
    if (abs(font_x - x0) <= 2):
        return points
    else:
        return points[::-1]

def pathPoints(path):
    points = []
    for i in range(len(path) - 1):
        x0 = coor_dict[str(path[i])][0]
        y0 = coor_dict[str(path[i])][1]
        x1 = coor_dict[str(path[i+1])][0]
        y1 = coor_dict[str(path[i+1])][1]
        print('from ' + str((x0,y0)) + ' to ' + str((x1,y1)))
        print(len(linePoints((x0,y0), (x1,y1))))
        points = points + (linePoints((x0,y0), (x1,y1)))
    print(points)
    return points

def find_path():
    timer = Timer(path)
button_print_coor = Button(middleframe, text="Find path", command = find_path)
button_print_coor.grid(row=1, column=2, pady=5)

root.mainloop()
