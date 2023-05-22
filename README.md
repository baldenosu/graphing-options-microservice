# graphing-options-microservice
This microservice takes a request with data to be plotted on a graph, the data for the x-axis and y-axis then get used to plot a graph and the client can decide on settings for the graph,  the resulting graph is then returned in a reply to the request

# Sending Requests

Requests can be made using ZeroMQ like so:
```Python
import zmq

context = zmq.Context()

#  Socket to talk to server
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
```
Then gather the data needed for the graph settings. The data is send in a python object with ZeroMQ.
The order of data should be sent as [x data, y data, x label, y label, graph title, set axis, grid visible]
x data = data for the x axis
y data = data for the y axis
x label = axis label for the x axis
y label = axis label for the y axis
graph title = title for the graph as a whole
grid visibility = should be 'Y' if the grid should be visible or 'N' if the grid should be invisible, if neither is picked the graph will auto set to the default of a visible grid
set axis = this should be set to None for auto scale and increments, otherwise store the setting variables or values in a list as follows: [x low, x high, x increment, y low, y high, y increment]
    x low = lower limit value for the x axis
    x high = the upper limit value for the x axis
    x increment = the increment to use for ticks on the graph on the x axis
    y low = lower limit value for the y axis
    y high = the upper limit value for the y axis
    y increment = the increment to use for ticks on the graph on the y axis
  
An example request might look as follows
```Python
# data for graph
x_data = np.arange(0.0, 2.0, 0.01)
y_data = 1 + np.sin(2 * np.pi * x_data)

# labels for graph
x_label = 'label for X axis'
y_label = 'label for Y axis'
graph_title = 'Title for the Graph'

# Axis Scale and increments
print("Set the scale for the x axis: ")
x_low = float(input('Lower limit: '))
x_high = float(input('Upper Limit: '))
x_increment = float(input('Increment for x-axis: '))
print("Set the scale for the y axis: ")
y_low = float(input('Lower limit: '))
y_high = float(input('Upper Limit: '))
y_increment = float(input('Increment for y-axis: '))
set_axis = [x_low, x_high, x_increment, y_low, y_high, y_increment]

# Y for yes and N for no, will auto set if neither option is chosen
grid_visibility = 'N'

#  Send request to graph settings microservice
print('Sending a request to the graphing microservice')
time.sleep(2)
socket.send_pyobj([x_data, y_data, x_label, y_label, graph_title, set_axis, grid_visibility])
```


# Receiving Requests

The request will then return the created graph with the desired settings as a python object

Requests can then be received like so:

```Python
#  Get the reply containing the graph.
ax = socket.recv_pyobj()
time.sleep(2)
plt.show()
```

# UML Sequence Diagram

![image](https://user-images.githubusercontent.com/114102391/236970363-720c3096-ca74-4400-ac0e-0863580318bd.png)
