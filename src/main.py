from fastapi import FastAPI

import uvicorn


from routes.model import history, predict, load
from routes.system.exception_handler import global_exception_handler
from routes.system import health

app = FastAPI()

app.include_router(history.router)
app.include_router(predict.router)
app.include_router(load.router)
app.include_router(health.router)
app.add_exception_handler(Exception, global_exception_handler)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="debug")
