from tkinter import *
from PIL import ImageTk, Image
import argparse
import pickle
import numpy as np
from graph import Graph
from solver import GNNSolver


class Timer:
    def __init__(self, path, canvas, coordinates):
        self.canvas = canvas
        self.path = path
        self.coordinates = coordinates

    def run(self):
        self.iteration = 0
        self.canvas.after(5, self.draw_line)
        self.pointList = pathPoints(self.path, self.coordinates)

    def draw_line(self):
        A = self.pointList[self.iteration]
        B = self.pointList[self.iteration + 1]
        self.canvas.create_line(A[0], A[1], B[0], B[1], width=4)
        if (self.iteration < len(self.pointList) - 2):
            self.iteration += 1
        else:
            self.do_nothing()
        self.canvas.after(5, self.draw_line)

    def do_nothing(self):
        pass


def read_coordinates(filepath):
    with open(filepath, "rb") as f:
        coordinates = pickle.load(f)

    return coordinates


def route(nodes, coordinates):
    selected_node_ids = [id for id, node in enumerate(nodes) if node.get() == 1]

    print("-" * 30)
    for node_idx in selected_node_ids:
        print(f"Node {node_idx}: ({coordinates[node_idx][0]}, {coordinates[node_idx][1]})")


def __plotLineLow(x0, y0, x1, y1):
    points = []
    dx = x1 - x0
    dy = y1 - y0
    yi = 1
    if dy < 0:
        yi = -1
        dy = -dy
    D = 2 * dy - dx
    y = y0

    for x in range(x0, x1):
        points.append((x, y))
        if D > 0:
            y = y + yi
            D = D - 2 * dx
        D = D + 2 * dy
    return points


def __plotLineHigh(x0, y0, x1, y1):
    points = []
    dx = x1 - x0
    dy = y1 - y0
    xi = 1
    if dx < 0:
        xi = -1
        dx = -dx
    D = 2 * dx - dy
    x = x0

    for y in range(y0, y1):
        points.append((x, y))
        if D > 0:
            x = x + xi
            D = D - 2 * dy
        D = D + 2 * dx
    return points


def linePoints(pointA, pointB):
    """ Generate a list of integer points on the line pointA -> pointB """
    x0, y0 = pointA
    x1, y1 = pointB
    points = []
    if (abs(y1 - y0) < abs(x1 - x0)):
        if (x0 > x1):
            points += __plotLineLow(x1, y1, x0, y0)
        else:
            points += __plotLineLow(x0, y0, x1, y1)
    else:
        if (y0 > y1):
            points += __plotLineHigh(x1, y1, x0, y0)
        else:
            points += __plotLineHigh(x0, y0, x1, y1)

    font_x = points[0][0]
    if (abs(font_x - x0) <= 2):
        return points
    else:
        return points[::-1]


def pathPoints(path, coordinates):
    points = []
    for i in range(len(path) - 1):
        x0 = coordinates[path[i]][0]
        y0 = coordinates[path[i]][1]
        x1 = coordinates[path[i+1]][0]
        y1 = coordinates[path[i+1]][1]
        points = points + (linePoints((x0, y0), (x1, y1)))
    return points


def solve(solver: GNNSolver, checkbox_vars, canvas, coordinates, plot_heatmap=False):
    selected_node_ids = [id for id, node in enumerate(checkbox_vars) if node.get() == 1]

    if len(selected_node_ids) <= 1:
        print("Please select more than 1 node")
        return

    optimal_route, heatmap = solver.solve(selected_node_ids)
    heatmap = heatmap[0]
    print(f"optimal_route={optimal_route}")

    if plot_heatmap:
        for r in range(len(heatmap)):
            for c in range(len(heatmap)):
                x0 = coordinates[optimal_route[r]][0]
                y0 = coordinates[optimal_route[r]][1]
                x1 = coordinates[optimal_route[c]][0]
                y1 = coordinates[optimal_route[c]][1]
                width = round(10*float(heatmap[r][c]))
                #canvas.create_line(x0, y0, x1, y1, width=width, fill=color, tags="heatmap")
                canvas.create_line(x0, y0, x1, y1, width=width, tags="heatmap")
                
    else:
        coords = []
        for i in range(len(optimal_route)-1):
            x0 = coordinates[optimal_route[i]][0]
            y0 = coordinates[optimal_route[i]][1]
            x1 = coordinates[optimal_route[i+1]][0]
            y1 = coordinates[optimal_route[i+1]][1]
            coords.extend([x0, y0, x1, y1])
     
        canvas.create_line(coords, width=5, fill="red", tags="line")


def blend(color, alpha, base=[255,255,255]):
    '''
    color should be a 3-element iterable,  elements in [0,255]
    alpha should be a float in [0,1]
    base should be a 3-element iterable, elements in [0,255] (defaults to white)
    '''
    out = [int(round((alpha * color[i]) + ((1 - alpha) * base[i]))) for i in range(3)]

    return out


def to_hex(color):
    return "#" + ''.join(["%02x" % e for e in color])


def reset(checkboxes, canvas):
    for idx in canvas.find_withtag("line"):
        canvas.delete(idx)

    for idx in canvas.find_withtag("heatmap"):
        canvas.delete(idx)

    for i in range(len(checkboxes)):
        checkboxes[i].deselect()


def print_selected_nodes(checkbox_vars, coordinates):
    selected_node_ids = [id for id, node in enumerate(checkbox_vars) if node.get() == 1]

    for idx in selected_node_ids:
        print(f"Node {idx}: x={coordinates[idx][0]}, y={coordinates[idx][1]}")


def select_all(checkboxes):
    for checkbox in checkboxes:
        checkbox.select()


def toggle_all(checkboxes):
    for checkbox in checkboxes:
        checkbox.toggle()


def main():
    # Create a window
    root = Tk()
    root.resizable(False, False)
    topframe = Frame(root)
    bottomframe = Frame(root)
    topframe.pack()
    bottomframe.pack()

    # Load background image
    img = ImageTk.PhotoImage(Image.open("img/map.jpg"))

    # Create canvas
    canvas = Canvas(topframe, width=img.width(), height=img.height(), borderwidth=0)
    canvas.grid(row=0, column=0)
    canvas.create_image(0, 0, image=img, anchor=NW)

    # Load graph
    graph = Graph(img.width(), img.height(), "graph.pkl")
    solver = GNNSolver(graph)

    # Draw checkboxes
    checkbox_vars = []
    checkboxes = []
    for i, (x, y) in enumerate(graph.unf_coordinates):
        checkbox_vars.append(IntVar())
        checkboxes.append(Checkbutton(root, variable=checkbox_vars[-1], text=str(i)))
        checkboxes[-1].place(x=x, y=y)

    # Define buttons
    button_reset = Button(bottomframe, text="Clear all", command=lambda: reset(checkboxes, canvas))
    button_reset.grid(row=1, column=1, pady=5)
    button_reset = Button(bottomframe, text="Select all", command=lambda: select_all(checkboxes))
    button_reset.grid(row=1, column=2, pady=5)
    button_reset = Button(bottomframe, text="Toggle all", command=lambda: toggle_all(checkboxes))
    button_reset.grid(row=1, column=3, pady=5)
    button_reset = Button(bottomframe, text="View heat-map", command=lambda: solve(solver, checkbox_vars, canvas, graph.unf_coordinates, True))
    button_reset.grid(row=1, column=4, pady=5)
    button_solve = Button(bottomframe, text="View optimal tour", command=lambda: solve(solver, checkbox_vars, canvas, graph.unf_coordinates, False))
    button_solve.grid(row=1, column=5, pady=5)

    # Execute program
    root.mainloop()


if __name__ == "__main__":
    main()
