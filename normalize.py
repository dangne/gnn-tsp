import numpy as np
import pickle


def read_coordinates(filepath):
    coordinates = []
    with open(filepath, "r") as f:
        coor = f.read()
        coor = list(map(int, coor.strip().split(" ")))
        for i in range(0, len(coor), 2):
            coordinates.append([coor[i], coor[i+1]])

    return coordinates


def normalize_coors(coordinates, x_min, x_max, y_min, y_max):
    for i in range(len(coordinates)):
        coordinates[i][0] = (coordinates[i][0] - x_min)/(x_max - x_min)
        coordinates[i][1] = (coordinates[i][1] - y_min)/(y_max - y_min)

    return coordinates



coordinates = np.array(read_coordinates("graph.pkl"), dtype=np.float32)

normalized_coors = normalize_coors(coordinates, 0, 605, 0, 480)

with open("graph.pkl", "wb") as f:
    pickle.dump(normalized_coors, f)
