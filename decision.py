def make_decision(total_score: int) -> str:
    if total_score >= 100:
        return "BLOCK"
    elif total_score >= 60:
        return "VERIFY"
    elif total_score >= 30:
        return "WARN"
    return "ALLOW"