
# feb 22, 2026
# this is hard-coded for now
def simulate_scenario(clauses, scenario: str):
    timeline=[]
    cost = 0

    for clause in clauses:
        text = clause["text"].lower()

        if scenario == "missed_payment" and "late fee" in text:
            timeline.append("Late fee applied")
            cost += 50
        
        if scenario == "early_termination" and "penalty" in text:
            timeline.append("Termination penalty triggered")
            cost += 200
    
    return {
        "scenario": scenario,
        "timeline": timeline,
        "estimated_cost": cost
    }