from src.exception.exception_handler import DeploymentNotFound, NameInvalid
from src.routers.deployments_router import router
from fastapi.responses import JSONResponse
from fastapi import FastAPI
import uvicorn


app = FastAPI()
app.include_router(router)


@app.exception_handler(DeploymentNotFound)
async def unicorn_exception_handler(exc: DeploymentNotFound):
    return JSONResponse(
        status_code=404,
        content={"error": f"{exc.message}"},
    )


@app.exception_handler(NameInvalid)
async def unicorn_exception_handler(exc: NameInvalid):
    return JSONResponse(
        status_code=400,
        content={"error": f"{exc.message}"},
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)