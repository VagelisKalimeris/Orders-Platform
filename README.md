# Task
Build an automated test suite for a RESTful API that simulates a trading platform with WebSocket support. 
Dockerize the test suite and server.

# Description
Create a sample RESTful API server that exposes a set of endpoints to simulate a trading platform and supports managing
and executing orders. The platform should use WebSocket connections also, for receiving real-time order status messages. 
Build an automated test suite for the API using Python and pytest, and Dockerize both the test suite and the server.

# Server requirements:
1. Implement the following API endpoints:
    GET /orders
    POST /orders
    GET /orders/{orderId} 
    DELETE /orders/{orderId}
2. After client sends POST/orders request, server sends confirmation and orderId. Then a client can request an order 
   info by using GET /orders/{orderId} and receive status.
3. Each endpoint must have a random short delay between 0.1 and 1 second.
4. The Database can be kept in memory.

# Advanced server requirements:
1. Make server asynchronous.
2. Implement WebSocket functionality into your server.
3. After orders are received from the client, the server sends back orderId and orderStatus as a response. Assume that 
   Order has three statuses: PENDING, EXECUTED, CANCELLED. They should be assigned after a random short delay.
4. Notify all subscribed clients about the order execution through WebSocket connection.

# Test cases requirements:
1. Cover all endpoints and methods of the API.
2. Organized into test suites and test functions using pytest.
3. Cover both positive and negative scenarios, including input validation errors.
4. Assert the correctness of the API responses and the expected behavior of the API.
5. Test suite and API server should be dockerized and should be able to run in separate containers
6. Generate report as a standalone file (e.g. html).

# Advanced testing requirements:
1. Verify WebSocket connections:
  A. Ensuring that real-time order status events are properly received by connected WebSocket clients.
  B. Ensuring that the order of receiving messages are correct (orderStatus=CREATED, received before 
     orderStatus=FILLED or no messages are received after receiving orderStatus=CANCELLED).

2. Implement performance testing according to the following scenario:
  A. Place 100 orders at the same time, validate the responses from REST API,
  B. Receive WS messages from the server,
  C. Calculate average order execution delay and standard deviation based on the a. and b. timestamps, d. print all the 
     metrics to the console.
