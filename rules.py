def rule_based_score(event: dict) -> tuple[int, list[str]]:
    score = 0
    reasons = []

    if int(event["is_known_bad_ip"]) == 1:
        score += 80
        reasons.append("Source IP is in known malicious list")

    if int(event["failed_logins"]) >= 5:
        score += 30
        reasons.append("Too many failed login attempts")

    if int(event["request_count"]) > 100:
        score += 25
        reasons.append("Abnormally high request count")

    if int(event["untrusted_file"]) == 1:
        score += 20
        reasons.append("Activity involves untrusted file")

    if int(event["privilege_request"]) == 1:
        score += 30
        reasons.append("Privilege escalation attempt detected")

    return score, reasons