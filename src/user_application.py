from src.routers.deployments_router import router
from fastapi import FastAPI
import uvicorn


app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)