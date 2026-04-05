def generate_explanation(decision: str, reasons: list[str], ai_score: int) -> str:
    parts = [f"Decision: {decision}"]

    if reasons:
        parts.append("Reasons:")
        for reason in reasons:
            parts.append(f"- {reason}")

    if ai_score > 0:
        parts.append("- AI anomaly detector found unusual behavior")

    if decision == "BLOCK":
        parts.append("Action blocked due to high risk.")
    elif decision == "VERIFY":
        parts.append("User verification is required for temporary restricted access.")
    elif decision == "WARN":
        parts.append("Action allowed with warning and monitoring.")
    elif decision == "ALLOW":
        if reasons or ai_score > 0:
            parts.append("Action allowed, but the event is logged for observation.")
        else:
            parts.append("Traffic appears normal.")

    return "\n".join(parts)