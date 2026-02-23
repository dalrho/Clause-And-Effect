import json
from app.core.llm import call_llm

def analyze_multiple_clauses(chunks: list):
    # Prepare the batch text
    formatted_clauses = [
        {"id": i, "text": chunk["text"]} 
        for i, chunk in enumerate(chunks)
    ]
    
    prompt = f"""
    Analyze the following contract clauses. 
    Return a JSON object with a key "analyses" containing a list of objects.
    Each object must include: "id", "category", "risk_level", and "explanation".

    Clauses:
    {json.dumps(formatted_clauses)}
    """

    result_raw = call_llm(prompt)
    
    try:
        # Parse the batch response
        batch_data = json.loads(result_raw)
        analyses_list = batch_data.get("analyses", [])
        
        # Map the AI results back to the original chunks using the ID
        final_results = []
        for i, chunk in enumerate(chunks):
            # Find the matching analysis by ID
            analysis = next((a for a in analyses_list if a["id"] == i), None)
            
            final_results.append({
                "text": chunk["text"],
                "page_number": chunk["page_number"],
                "category": analysis["category"] if analysis else "unknown",
                "risk_level": analysis["risk_level"] if analysis else "low",
                "explanation": analysis["explanation"] if analysis else "Analysis missing"
            })
        return final_results

    except Exception as e:
        print(f"Batch Parsing Error: {e}")
        # Fallback for the whole batch if JSON fails
        return [{"text": c["text"], "page_number": c["page_number"], "category": "error"} for c in chunks]