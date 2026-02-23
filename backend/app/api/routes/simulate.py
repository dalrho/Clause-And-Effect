from fastapi import APIRouter
from app.services.simulator import simulate_scenario
from app.core.db import fake_db
router = APIRouter()


@router.post("/{contract_id}")
def simulate(contract_id: str, scenario: str):
    data = fake_db.get(contract_id)

    if not data or "analysis" not in data:
        return {"error": "Analyze first"}
    
    result = simulate_scenario(data["analysis"], scenario)

    return result