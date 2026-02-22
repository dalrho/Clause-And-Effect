def chunk_text(text: str):
    return [chunk.strip() for chunk in text.split("\n") if chunk.strip()]