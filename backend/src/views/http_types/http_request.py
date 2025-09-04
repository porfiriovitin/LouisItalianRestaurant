class HttpRequest:
    def __init__(self, request, param: dict = None):
        if hasattr(request, "get_json"):
            self.body = request.get_json(silent=True) or {}
        else:
            self.body = request
        self.param = param or {}