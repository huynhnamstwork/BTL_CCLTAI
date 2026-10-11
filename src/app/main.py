import os

from fastapi import FastAPI

app = FastAPI(title="Vehicle Counting API")
MODEL_VERSION = os.getenv("MODEL_VERSION", "v1")


@app.get("/health")
def health():
    return {"status": "ok", "model_version": MODEL_VERSION}
