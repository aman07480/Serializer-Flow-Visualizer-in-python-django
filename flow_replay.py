import time

def replay_flow(logs, delay=0.5):
    """
    Replay flow step by step
    """

    replay_data = []

    for log in logs:
        replay_data.append({
            "step": log["step"],
            "status": log.get("status"),
        })
        time.sleep(delay)

    return replay_data

    import time

def replay_flow(logs, delay=0.5):
    """
    Replay flow step by step
    """

    replay_data = []

    for log in logs:
        replay_data.append({
            "step": log["step"],
            "status": log.get("status"),
        })
        time.sleep(delay)

    return replay_data