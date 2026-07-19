from fastapi import FastAPI
from test_db import router as test_router

app = FastAPI()

app.include_router(test_router)

@app.get("/status")
def status():
    return {"ok": True}
