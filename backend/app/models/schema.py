from pydantic import BaseModel
from typing import List

class Clause(BaseModel):
    text: str
    category: str
    risk_level: str
    explanation: str
    page_number: int

class ContractAnalysis(BaseModel):
    clauses: List[Clause]
    summary: str