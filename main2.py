
from fastapi.exceptions import RequestValidationError
from app.coreException import CoreException
from fastapi import FastAPI
import uvicorn

from fastapi_utils.api_settings import get_api_settings

#
# It is generally a good idea to initialize your FastAPI instance inside a function. 
# This ensures that you never have access to a partially-configured instance of your app,
# and you can easily change settings and generate a new instance
def get_app() -> FastAPI:
    get_api_settings.cache_clear()
    settings = get_api_settings()
    app = FastAPI(**settings.fastapi_kwargs)
    # <Typically, you would include endpoint routers here>
    return app


if __name__ == "__main__":
    app = get_app()
    uvicorn.run(app, host="0.0.0.0", port=8000)

    #TODO: use yugabyte DB