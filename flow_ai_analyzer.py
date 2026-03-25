def analyze_flow_intelligence(logs):

    issues = []

    for log in logs:

        if log.get("status") == "ERROR":
            issues.append(f"Error at step: {log['step']}")

        if "Validation Failed" in log.get("step", ""):
            issues.append("Validation issue detected")

    return {
        "total_issues": len(issues),
        "issues": issues
    }