from fastapi import FastAPI
from app.routes import payments
from app.logging_config import setup_logging

setup_logging()

app = FastAPI(title="Cloud Native Payments API")

@app.get("/health")
def health_check():
    return {"status": "UP"}

app.include_router(payments.router)