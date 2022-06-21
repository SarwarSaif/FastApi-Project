from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, Response
import time

class HTTPWebInterceptor(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
            #you can modify the request here <--
        response = await call_next(request) #passing the request to the router/path and wait the response
        process_time = time.time() - start_time
            #request/response additional processing functions
        self.add_process_time_header(process_time, response)
        self.logging(process_time, request, response)
        return response
    

    """ [summary] 
    """
    def add_process_time_header(self, process_time, response: Response):
        response.headers["X-Process-Time"] = str(process_time)
        
        
        """[summary]
        """
    def logging(self, process_time, request: Request, response: Response):
        print(">>>>>>>>" + self.__class__.__name__)
        print(f'{request.method} {request.url}') #http://localhost:8000/custom
        # print(request.client.host)  #27.0.0.1
        # print(request.url.path)     #/custom
        # print(request.url.scheme)   #http
        # print(request.url.hostname) #localhost
        # print(request.url.port)     #8000
        print(f'Status code: {response.status_code} [HTTP Response time: {process_time}]')
        #TODO: log apiName, userID, response time, etc
        




