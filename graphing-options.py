# Author: James Balden
# GitHub username: baldenosu
# Date: 5/8/2023
# Description: A microservice for creating graph from received data and setting the graph options for a matplotlib
# graph. Created as a microservice for CS 361.

import matplotlib.pyplot as plt
import numpy as np
import zmq

# Set up the socket for receiving requests
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client store x_data and y_data
    print('waiting for the next request')
    x_data, y_data, x_label, y_label, graph_title, set_axis, grid_visible = socket.recv_pyobj()
    print('request received starting system')

    # Set up the graph with the received data
    fig, graph = plt.subplots()
    graph.plot(x_data, y_data)

    # Set Axis Scale, and increments
    if set_axis is not None:
        x_low = set_axis[0]
        x_high = set_axis[1]
        x_increment = set_axis[2]
        y_low = set_axis[3]
        y_high = set_axis[4]
        y_increment = set_axis[5]
        graph.set_xlim(x_low, x_high)
        graph.set_ylim(y_low, y_high)
        graph.set_xticks(np.arange(x_low, x_high, x_increment))
        graph.set_yticks(np.arange(y_low, y_high, y_increment))
    else:
        print("Axis Scale auto set")

    # Apply all the settings to the graph
    graph.set(xlabel=x_label, ylabel=y_label, title=graph_title)

    # Set whether gridlines are visible or not
    if grid_visible == 'Y':
        graph.grid()
    elif grid_visible == 'N':
        graph.grid(visible=False)
    else:
        print("Incorrect input, gridlines set to default on.")
        graph.grid()

    #  Send reply to client containing graph object
    print("Applying settings and returning graph.")
    socket.send_pyobj(graph)

