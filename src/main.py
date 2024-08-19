from fastapi import FastAPI

import uvicorn


from routes.model import history, predict

app = FastAPI()

app.include_router(history.router)
app.include_router(predict.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="debug")
