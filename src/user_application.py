from src.exception.exception_handler import (DeploymentNotFound, NameInvalid, MongoError, AuthorizationError,
                                             InvalidUsername)
from src.rdbms.establish_connection import create_tables, add_status
from src.configuration.open_config import HOST, PORT
from src.routers.deployments_router import router
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request
import uvicorn


app = FastAPI()
app.include_router(router)


@app.on_event("startup")
def on_startup():
    create_tables()
    add_status()


@app.exception_handler(DeploymentNotFound)
def unicorn_exception_handler(request: Request, exc: DeploymentNotFound):
    return JSONResponse(
        status_code=404,
        content={"error": f"{exc.message}"},
    )


@app.exception_handler(MongoError)
def unicorn_exception_handler(request: Request, exc: MongoError):
    return JSONResponse(
        status_code= 503,
        content={"error": f"{exc.message}"},
    )


@app.exception_handler(NameInvalid)
def unicorn_exception_handler(request: Request, exc: NameInvalid):
    return JSONResponse(
        status_code=400,
        content={"error": f"{exc.message}"},
    )


@app.exception_handler(InvalidUsername)
def unicorn_exception_handler(request: Request, exc: InvalidUsername):
    return JSONResponse(
        status_code=400,
        content={"error": f"{exc.message}"},
    )


@app.exception_handler(AuthorizationError)
def unicorn_exception_handler(request: Request, exc: AuthorizationError):
    return JSONResponse(
        status_code=401,
        content={"error": f"{exc.message}"},
    )


if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)
