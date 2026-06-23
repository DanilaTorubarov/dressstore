from fastapi import FastAPI

app = FastAPI(title="dressstore", version="0.1.0")


@app.get("/")
async def root():
    return {"message": "Welcome to dressstore API"}


@app.get("/health")
async def health():
    return {"status": "ok"}
