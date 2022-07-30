from fastapi import FastAPI
from board import board

app = FastAPI()

# how to run
# gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8080 --reload

app.include_router(
    board.router,
    prefix='/board'
)
