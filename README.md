# Simple Router Example
This code sample is a minimal, though fully functional, implementation to demonstrate building an application that routes messages to handlers in a pattern similar to Flask and later FastAPI. The route handlers are registered with the application through decorators. As messages arrive, the application dispatches them to the appropriate handler based on some selection criteria.

I used this pattern to implement routing for a lightweight WebSocket API as well as an AWS Lambda function invoked by AWS triggers.

- `routing.py` defines the `Router` ("app" in Flask terms). The `route` method implements the `@route` decorator. The nested `register_route` function takes a kay argument that is the key for selecting the route. The `dispatch` method takes an event with a `route_key` element, looks up the route registered to handle that key, and then invokes the route handler by passing the event's `data` element to the handler.
- `simple.py` creates an instance of the `Router` and registers two handlers; one for "run" events (`route_key` equals `"run"`) and one for "pass" events. The `execute` function invokes the router's `dispatch` method to route an incoming message to the appropriate handler function. By convention, this function might be named `lambda_handler` in an AWS Lambda.
- `examples.py` provides examples to demonatrate the simple router application. The application is passed several sample messages of various types (as indicated by their `route_key`). Each message is routed to the function registered to handle messages of that type.
