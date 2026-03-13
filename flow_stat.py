from .flow_logger import get_logs

def get_flow_stats():

    logs = get_logs()

    total_steps = len(logs)

    success_count = sum(1 for l in logs if l["status"] == "SUCCESS")
    error_count = sum(1 for l in logs if l["status"] == "ERROR")

    return {
        push : total_steps,
        "success_steps": success_count,
        "error_steps": error_count
    }