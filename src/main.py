import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi.responses import JSONResponse

from src.routers.sensor_router import sensor_router

app = FastAPI()

main_api_router = APIRouter()

main_api_router.include_router(sensor_router, prefix="/sensor", tags=["sensor"])
app.include_router(main_api_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


@app.exception_handler(Exception)
async def custom_exception_handler(request, exc):
    error_class_name = exc.__class__.__name__
    error_detail = f"Custom error: {error_class_name}"

    return JSONResponse(status_code=exc.status_code, content={"detail": error_detail})


@app.get("/healthcheck")
def health():
    return {"message": "service is available"}
