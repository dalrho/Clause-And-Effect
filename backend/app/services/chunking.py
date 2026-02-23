import re
import pdfplumber

def chunk_pages(pdf_path: str):
    full_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        # Join all pages to ensure sentences crossing pages stay together
        for page in pdf.pages:
            full_text += page.extract_text() + "\n"

    # Split into Preamble and Body using the WITNESSETH marker 
    parts = re.split(r'WITNESSETH THAT:', full_text, flags=re.IGNORECASE)
    preamble = parts[0].strip()
    body = parts[1] if len(parts) > 1 else ""

    chunks = []
    
    # Chunk 0: Who, When, Where [cite: 2, 3, 5]
    if preamble:
        chunks.append({
            "header": "PREAMBLE & PARTIES",
            "text": preamble,
            "page_number": 1
        })

    # Split the body by Numbered Sections (1. SUBJECT, 4. DELIVERY, etc.) [cite: 11, 21]
    # This regex is the "hook" that grabs the whole paragraph until the next number
    sections = re.split(r'\n(?=\d+\.\s+[A-Z])', body)
    
    for section in sections:
        clean_section = section.strip()
        if clean_section:
            # We take the first line as the header, but keep the WHOLE text
            lines = clean_section.split('\n')
            # Extract just the title for the header, e.g., "4. DELIVERY OF THE DEVICE" 
            header = lines[0].strip() 
            
            chunks.append({
                "header": header,
                "text": clean_section, # This now contains the FULL paragraph
                "page_number": 1 
            })

    return chunks