def chunk_pages(pages):
    chunks = []

    for page in pages:
        lines = page["text"].split("\n")

        for line in lines:
            if line.strip():
                chunks.append({
                    "text": line.strip(),
                    "page_number": page["page_number"]
                })

    return chunks