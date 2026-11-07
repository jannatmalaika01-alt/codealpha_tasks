from fastapi import FastAPI

app = FastAPI(title="Language Translation Tool")

@app.get("/")
def home():
    return {"message": "Language Translation API is running"}