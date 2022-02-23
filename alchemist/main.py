# Import Library
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from alchemist.apps import
from alchemist.config import HOST, PORT
import uvicorn


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router()

@app.get("/")
async def root():
    return "Hello, Kronos!"

if __name__ == '__main__':
    uvicorn.run("kronos.main:app", host=HOST, port=PORT, reload=True)