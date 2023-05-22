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
        print("Set the scale for the x axis: ")
        x_low = float(input('Lower limit: '))
        x_high = float(input('Upper Limit: '))
        x_increment = float(input('Increment for x-axis: '))
        print("Set the scale for the y axis: ")
        y_low = float(input('Lower limit: '))
        y_high = float(input('Upper Limit: '))
        y_increment = float(input('Increment for y-axis: '))
        graph.set_xlim(x_low, x_high)
        graph.set_ylim(y_low, y_high)
        graph.set_xticks(np.arange(x_low, x_high, x_increment))
        graph.set_yticks(np.arange(y_low, y_high, y_increment))
    else:
        print("Axis Scale auto set")

    # Set labels for the graph
    # x_label = input("What should the label for the x axis be? ")
    # y_label = input("What should the label for the y axis be? ")
    # graph_title = input("What should the label for the title be? ")

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

