from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Welcome to the Annotation Lifecycle Management Service API"}

