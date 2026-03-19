def analyze_performance(logs):

    if len(logs) < 2:
        return {"execution_time": 0}

    start = logs[0]["timestamp"]
    end = logs[-1]["timestamp"]

    execution_time = end - start

    return {
        "execution_time": execution_time,
        "steps_count": len(logs)
    }