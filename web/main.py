from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .routes.print import router as print_router

app = FastAPI()

app.include_router(print_router)


@app.get("/health")
def health():
    return {"status": "ok"}


app.mount("/", StaticFiles(directory="static", html=True), name="static")
