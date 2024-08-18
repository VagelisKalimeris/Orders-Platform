## Objective
- Simulate an orders platform asynchronous RestApi
- Notify all subscribed clients about the order execution status, using WebSocket
- Build automated test suite covering all endpoints and generating results report
- Implement performance testing with concurrent orders, validating api responses and  calculating average 
  execution time and standard deviation
- Dockerize the tests and server in separate containers


## Swagger
Run server and visit [this page][swagger].


## Execution
Running `docker-compose up` will:
- Create api server container
- Create test container
- Execute all tests in test container
- Produce test report [here][test report]


## Design
Tests are executed in parallel, split in 3 workers, according to file.

In essence, each worker handles a suite:
- positive cases
- negative cases
- load testing  

This affects load testing, since other concurrent tests slow down server, and can be avoided by setting 
`-n=3` to `-n=1` in test [dockerfile][test dockerfile].


## Todo
- [x] Add CI actions
- [ ] Move DELETE order logic to PATCH - Update DELETE logic
- [ ] Test Websocket clients order status receival
- [ ] Load test Websocket
- [ ] Replace current thread implementation, with process pool for order status updates
- [ ] Replace in memory DB with async **Postgres**


[swagger]: http://0.0.0.0:80/docs
[test report]: test/test_reports/report.htm
[test dockerfile]: test/Dockerfile
