from fastapi import FastAPI, HTTPException
from schemas import TranslationRequest, TranslationResponse
from translator import translate_text

app = FastAPI(title="Language Translation Tool")

@app.get("/")
def home():
    return {"message": "Language Translation API is running"}

@app.post("/translate", response_model=TranslationResponse)
def translate(request: TranslationRequest):
    try:
        result = translate_text(
            request.text,
            request.source_language,
            request.target_language
        )
        return TranslationResponse(
            original_text=request.text,
            translated_text=result,
            source_language=request.source_language,
            target_language=request.target_language
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))