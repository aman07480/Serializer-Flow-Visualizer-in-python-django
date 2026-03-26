def build_timeline(logs):

    timeline = []

    for log in logs:

        timeline.append({
            "time": log["timestamp"],
            "event": log["step"],
            "status": log.get("status")
        })

    return timeline