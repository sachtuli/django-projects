from django.http import HttpResponse


class MiddlewareLifeCycle:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response


class ExceptionHandlerMiddleware:
    def __init__(self, get_response):
        """
        This is the constructor method.

        Parameters:
        get_response (function): a callable that takes a request object and
        returns a response object
        """
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        print(exception.__class__.__name__)
        return HttpResponse("<b>Currently, System is down. Retry after some time.</b>")
