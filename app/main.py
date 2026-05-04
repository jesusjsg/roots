from fastapi import FastAPI

from app.core.settings import settings

app = FastAPI(title=settings.TITLE)


@app.get("/")
def read_root() -> bool:
    return True
