from starlette.responses import JSONResponse
from error_code import ErrorCode
from exceptionModel import ExceptionDto
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exceptions import RequestValidationError
from starlette import status
from fastapi.encoders import jsonable_encoder
import traceback
from coreException import CoreException
from starlette.responses import JSONResponse
from starlette.requests import Request


#overriding the fast api http_exception_handler:
#https://github.com/tiangolo/fastapi/blob/master/fastapi/exception_handlers.py
# exc.status_code
# exc.detail
async def generic_http_exception_handler(request: Request, exc: StarletteHTTPException) -> JSONResponse:
    stack_trace=traceback.format_exc()
    exception_dto=ExceptionDto(http_error_code=exc.status_code, 
                                name=type(exc).__name__, 
                                internal_error_code=ErrorCode.S9991.name +": " + ErrorCode.S9991.value, #TODO: use format
                                message=exc.detail, #str(exc),
                                exception_args=str(exc.status_code) + " -> " + exc.detail,
                                stacktrace=stack_trace)
    dto_to_json=jsonable_encoder(exception_dto)
    return JSONResponse(status_code=exc.status_code, content=dto_to_json)
#405 : send POST where GET expected -> localhost:8000
#404: request for resource which dont exist -> localhost:8000/not-exist

#overriding the fast api validation_exception_handler:
#https://github.com/tiangolo/fastapi/blob/master/fastapi/exception_handlers.py
# exc.errors()
# exc.body  #Original request payload
async def request_validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    stack_trace=traceback.format_exc()
    msg_list=[obj['msg'] + "->" + obj['type']  for obj in exc.errors()]
    exception_dto=ExceptionDto(http_error_code=status.HTTP_422_UNPROCESSABLE_ENTITY, 
                               name=type(exc).__name__, 
                               internal_error_code=ErrorCode.S9992.name +": " + ErrorCode.S9992.value, #TODO: use format
                               message=str(exc),
                               exception_args=" | ".join(msg_list),
                               stacktrace=stack_trace)
    dto_to_json=jsonable_encoder(exception_dto)
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content=dto_to_json)
#422: validation error for emmpty payload --> localhost:8000/create/user   { }


#my custom fields (ErrorCode Enum)
# exc.error_code.name
# exc.error_code.value
async def core_exception_handler(request: Request, exc: CoreException) -> JSONResponse:
    #internal_server_error_handler
    stack_trace=traceback.format_exc()
    exception_dto=ExceptionDto(http_error_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                               name=type(exc).__name__, 
                               internal_error_code=exc.error_code.name,
                               message=exc.error_code.value,
                               exception_args=exc.args,
                               stacktrace=stack_trace)
    dto_to_json=jsonable_encoder(exception_dto)
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=dto_to_json)


async def generic_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    stack_trace=traceback.format_exc()
    exception_dto=ExceptionDto(http_error_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                               name=type(exc).__name__,
                               internal_error_code=ErrorCode.S9999.name +": " + ErrorCode.S9999.value, #TODO: use format, 
                               message=str(exc),
                               exception_args=exc.args,
                               stacktrace=stack_trace)
    dto_to_json=jsonable_encoder(exception_dto)
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=dto_to_json)