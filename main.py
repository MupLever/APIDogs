import uvicorn
from fastapi import FastAPI
from api.orders.views import router as orders_router


app = FastAPI(title="APIDogs", version="1.0.0")
app.include_router(orders_router)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
