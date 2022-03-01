# Import Library
from fastapi import FastAPI, File, UploadFile, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from typing import List

# Import Utils Setting
from alchemist.config import HOST, PORT
from alchemist.utils import files_check
# from alchemist.utils.human_detection import
# from alchemist.utils.posture_classification import

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


@app.post("/ai/", status_code=status.HTTP_200_OK)
async def upload_files(files: List[UploadFile] = File(...)):
    files_check(files)

if __name__ == '__main__':
    uvicorn.run("alchemist.main:app", host=HOST, port=PORT, reload=True)