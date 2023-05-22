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

#  Send request to graph settings microservice
x_data = np.arange(0.0, 2.0, 0.01)
y_data = 1 + np.sin(2 * np.pi * x_data)
socket.send_pyobj([x_data, y_data])
```


# Receiving Requests

Requests can then be received like so:

```Python
#  Get the reply containing the graph.
ax = socket.recv_pyobj()
time.sleep(2)
plt.show()
```

# UML Sequence Diagram

![image](https://user-images.githubusercontent.com/114102391/236970363-720c3096-ca74-4400-ac0e-0863580318bd.png)
