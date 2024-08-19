from fastapi.responses import JSONResponse
from fastapi import Request
import logging


async def global_exception_handler(request: Request, exc: Exception):
    logging.error(f"Unhandled exception: {exc}")
    
    return JSONResponse(
        status_code=500,
        content={"error": str(exc)},
    )