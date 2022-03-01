# Import Library
from fastapi import HTTPException, status
from typing import List


def files_check(files: List[str]):
    if files is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="file is none")