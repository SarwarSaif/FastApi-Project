
from pydantic.main import BaseModel

#BOTH WORKS (Pydantic model OR normal DTO)
class ExceptionDto(BaseModel):
    name: str
    message: str
    error_code: str
    http_error_code: str
    description: str
     
class ExceptionDto:
    def __init__(self, **kwargs):
        self.http_error_code = kwargs['http_error_code']
        self.name = kwargs['name']
        self.internal_error_code = kwargs['internal_error_code'] 
        self.message = kwargs.get('message') #get means its optional
        self.exception_args = kwargs.get('exception_args')
        #self.description = kwargs.get('description')
        self.stacktrace = kwargs.get('stacktrace')
        
# exception_dto2=ExceptionDto(name="aa", message="bb", error_code="cc", http_error_code="dd", description="ee")
# exception_dto2.description="ff"
# print(exception_dto2.description)


# class ExceptionDto:
#     def __init__(self, http_error_code, name, internal_error_code, message, exception_args, stacktrace): 
#         self.ttp_error_code = http_error_code
#         self.name = name
#         self.internal_error_code = internal_error_code
#         self.message = message
#         self.exception_args = exception_args
#         self.stacktrace = stacktrace