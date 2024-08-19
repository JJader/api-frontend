from fastapi import FastAPI

import uvicorn


from routes.model import history

app = FastAPI()

app.include_router(history.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="debug")
