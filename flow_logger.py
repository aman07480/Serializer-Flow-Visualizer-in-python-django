FLOW_LOGS = []


def log_step(step, data=None):
    """
    Store serializer execution steps
    """

    FLOW_LOGS.append({
        "step": step,
        "data": str(data)
    })


def get_logs():

    return FLOW_LOGS


def clear_logs():

    FLOW_LOGS.clear()

import time

FLOW_LOGS = []


def log_step(step, data=None):
    FLOW_LOGS.append({
        "step": step,
        "data": str(data),
        "timestamp": time.time()
    })