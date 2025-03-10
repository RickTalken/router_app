import typing


class Router:
    def __init__(self):
        self.routes = {}

    def route(self, key: str) -> typing.Callable:
        def register_route(func: typing.Callable):
            self.routes[key] = func
            return func

        return register_route

    def dispatch(self, event: dict):
        route_key = event.get("route_key")
        handler = self.routes.get(route_key)

        if not handler:
            raise KeyError(f"Route key not found: {route_key}")

        return handler(event.get("data"))
