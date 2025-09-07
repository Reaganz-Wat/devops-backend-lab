import time
class SampleTestMiddleware():
    def __init__(self, get_response):
        print("Starting the middleware...")
        self.get_response = get_response
        
    def __call__(self, request):
        print("Executing the middleware...")
        
        return self.get_response(request)