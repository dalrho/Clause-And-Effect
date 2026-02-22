import json

from app.core.llm import call_llm

def analyze_clause(text: str):
    prompt = f"""
    Analyze this contract clause:
    "{text}

    Return JSON:
    {{
        "category": "payment | termination | liability | confidentiality| other",
        "risk_level": "low | medium | high",
        "explanation": "one sentence explanation"
    }}
    """

    response = call_llm(prompt)

    try:
        return json.loads(response)
    except:
        return {
            "category": "other",
            "risk_level": "low",
            "explanation": "Parsing failed"
        }