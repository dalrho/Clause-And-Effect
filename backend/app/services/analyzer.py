import json
from app.core.llm import call_llm

def analyze_multiple_clauses(chunks: list):
    # Now each "chunk" is a full Section (e.g., "3. PAYMENT TERMS")
    formatted_clauses = [
        {"id": i, "header": chunk["header"], "text": chunk["text"]} 
        for i, chunk in enumerate(chunks)
    ]
    
    prompt = f"""
    Analyze the following contract sections. 
    Return a JSON object with a key "analyses" containing a list of objects.
    Each object must include: "id", "category", "risk_level", and "explanation".

    Sections:
    {json.dumps(formatted_clauses)}
    """

    result_raw = call_llm(prompt)
    
    try:
        batch_data = json.loads(result_raw)
        analyses_list = batch_data.get("analyses", [])
        
        final_results = []
        for i, chunk in enumerate(chunks):
            analysis = next((a for a in analyses_list if a["id"] == i), None)
            
            final_results.append({
                "header": chunk["header"],
                "text": chunk["text"],
                "page_number": chunk.get("page_number", 1),
                "category": analysis["category"] if analysis else "unknown",
                "risk_level": analysis["risk_level"] if analysis else "low",
                "explanation": analysis["explanation"] if analysis else "Analysis missing"
            })
        return final_results
    except Exception as e:
        print(f"Batch Parsing Error: {e}")
        return [{"header": c["header"], "text": c["text"], "category": "error"} for c in chunks]