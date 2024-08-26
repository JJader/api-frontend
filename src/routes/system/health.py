from fastapi import APIRouter

router = APIRouter()


@router.get("/model/health")
async def get_health():
    return "ok"
