# Import Library
from fastapi import APIRouter, status

# Import Utils
# from alchemist.utils


router = APIRouter()


@router.post("/detection", status_code=status.HTTP_200_OK, tags=["detection"])
async def human_detection(img_list: list):
