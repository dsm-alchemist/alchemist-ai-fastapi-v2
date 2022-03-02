# Import Library
from fastapi import FastAPI, File, UploadFile, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from typing import List, Optional
import os, aiofiles

# Import Utils Setting
from alchemist.config import HOST, PORT
from alchemist.utils import files_check
from alchemist.utils.human_detection import human_detection
from alchemist.utils.posture_classification import posture_classity

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return "Hello, Kronos!"


@app.post("/ai", status_code=status.HTTP_200_OK)
async def upload_files(files: Optional[List[UploadFile]] = File([])):
    if files_check(files):
        if human_detection(files):
            if posture_classity(files) is False:
                HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User is Sleep.")
            else:
                raise HTTPException(status_code=status.HTTP_200_OK, detail="Timer Run")
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Human Not Found.")
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="file is none")


if __name__ == '__main__':
    uvicorn.run("alchemist.main:app", host=HOST, port=PORT, reload=True)