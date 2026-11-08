import requests

def translate_text(text, source_language, target_language):
    url = "https://api.mymemory.translated.net/get"

    params = {
        "q": text,
        "langpair": f"{source_language}|{target_language}"
    }

    response = requests.get(url, params=params, timeout=15)
    response.raise_for_status()

    data = response.json()

    if data.get("responseStatus") != 200:
        raise Exception(data.get("responseDetails", "Translation failed"))

    return data["responseData"]["translatedText"]