from .flow_logger import get_logs
from .flow_performance import analyze_performance


def get_dashboard_data():

    logs = get_logs()

    performance = analyze_performance(logs)

    return {
        "total_steps": len(logs),
        "performance": performance,
        "last_step": logs[-1] if logs else None,
        "all_logs": logs
    }