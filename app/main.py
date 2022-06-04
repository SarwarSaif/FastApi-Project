from interceptors import HTTPWebInterceptor
from models.validate import ValidationModel
from fastapi.exceptions import RequestValidationError
from coreException import CoreException
from fastapi import FastAPI
import uvicorn

### Bring my Logger
from lib.mylogger import MyLogger
custom_logger = MyLogger(logger_name="MAIN")

#class FastAPI(Starlette):
#https://github.com/tiangolo/fastapi/blob/master/fastapi/applications.py
app = FastAPI(   #app = FastAPI()
    title='Yandex.Cloud Netinfra API',
    description='A bundled API for Yandex.Cloud Netinfra team tools',
    debug=True
)
# server = FastAPI(title=app_settings.project_name, 
#                  openapi_url=api_settings.openapi_route, 
#                  debug=api_settings.debug)
# server.include_router(get_api_router(), prefix=api_settings.api_v1_route)

    # @server.get("/", include_in_schema=False)
    # def redirect_to_docs() -> RedirectResponse:
    #     return RedirectResponse("/docs")

    # @server.on_event("startup")
    # async def connect_to_database() -> None:
    #     database = get_database()
    #     if not database.is_connected:
    #         await database.connect()

    # @server.on_event("shutdown")
    # async def shutdown() -> None:
    #     database = get_database()
    #     if database.is_connected:
    #         await database.disconnect()
            
#________________________________________________________
#manually ENV Variables
# from config2 import get_settings2

#using pydantic
from core.config3 import get_settings
api_logger = MyLogger(logger_name="API")

@app.get("/")
async def root():
    #return {"message": "Hello World"}
    custom_logger.info("Accessing Root endpoint ")
    return {"message": get_settings().SQLALCHEMY_DATABASE_URI, "by_pydantic": get_settings()} #"Hello World"}



@app.post("/validation")
async def validate(input_dto: ValidationModel):
    print(input_dto)
    api_logger.info("Input DTO: {}".format(input_dto))
    return input_dto

# {
# 	"id": "55",
# 	"name": "greater",
# 	"apple_based_food": "apple pie",
# 	"is_active": true,
# 	"url":"http://www.localhost:8000/validation",
# 	"count":"55"
# }

# "id": "not integer", (string instead on int)
    #msg: value is not a valid integer
# "id": 10
#  #msg: ensure this value is greater than 50
#"id": 51
    #msg: ensure this value is a multiple of 5
#"url":"localhost:8000/validation" (missing http part "http://www")
    # msg: invalid or missing URL scheme (type=value_error.url.scheme)
#"name": "test",
    # mgg: ensure this value has at least 5 characters
#"apple_based_food": "mango pie"
    #msg: apple_based_food": "mango pie",
#"email_address":"mamadu.bah@rakuten.com333"
    #value is not a valid email address
#"password1":""
    #msg:passwords must be provided
# ________________________________________________________
#static_files_app = StaticFiles(directory=str(app_settings.static_dir))
#app.mount(path=app_settings.static_mount_path, app=static_files_app, name="static")

#from fastapi.staticfiles import StaticFiles
from starlette.staticfiles import StaticFiles
app.mount("/static", StaticFiles(directory="app/static"), name="static") #http://localhost:8000/static/index.html

#________________________________________________________

#API services
from routers.user_service import user_router
from routers.parent_child_service import parent_router
from routers.custom_service import custom_service_router

#app.include_router(UserService().router)
app.include_router(user_router)
app.include_router(parent_router)
app.include_router(custom_service_router)
#@app.get("/")
#@app.post("/validation")


#Exception Handlers
from starlette.exceptions import HTTPException as StarletteHTTPException
from generic_http_handler import core_exception_handler, generic_exception_handler, generic_http_exception_handler, request_validation_exception_handler
app.add_exception_handler(StarletteHTTPException, generic_http_exception_handler)
app.add_exception_handler(RequestValidationError, request_validation_exception_handler)
app.add_exception_handler(CoreException, core_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

#adding a middleware as HTTP Interceptor
#@app.middleware("http")
app.add_middleware(HTTPWebInterceptor)

# middleware state.connectionにdatabaseオブジェクトをセットする。
# @app.middleware("http")
# async def db_session_middleware(request: Request, call_next):
#     request.state.connection = database
#     response = await call_next(request)
#     return response

#todo
#app.include_router(rutas.router)


    # async def vnot_found_error_handler(request: requests, exc: RequestValidationError):
    # BadRequestError
    # ForbiddenError(error_code: int = 403,
    # UnauthorizedError(error_code: int = 401
#starlette HTTPResponse codes
#https://github.com/encode/starlette/blob/master/starlette/status.py


#TODO PAGINATION BY FASTAPI
#@app.get("/")
# async def list(pagination: Pagination = Depends()):
#     filter_kwargs = {}
#     return await pagination.paginate(
#         serializer_class=SomeSerializer, **filter_kwargs
#     )


#their uses has been discouraged, find updared alternatives
#@app.on_event("startup")
# async def startup_event():
#     items["foo"] = {"name": "Fighters"}
#     items["bar"] = {"name": "Tenders"}

# @app.on_event("shutdown")
# def shutdown_event():
#     with open("log.txt", mode="a") as log:
#         log.write("Application shutdown")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

    #TODO: use yugabyte DB
    
#================================================================

