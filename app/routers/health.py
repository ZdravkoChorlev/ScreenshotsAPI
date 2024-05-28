from fastapi import APIRouter
from fastapi.responses import JSONResponse
import orjson

router = APIRouter()

@router.get("")
def is_alive():
    content = {"status": "alive"}
    return JSONResponse(status_code=200, content=content)
