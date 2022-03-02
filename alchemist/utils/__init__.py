# Import Library
from fastapi import HTTPException, status, File, UploadFile
from typing import List


def files_check(files: List[UploadFile] = File(...)):
    if files is None:
        return False
    else:
        return True