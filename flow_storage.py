# from django.db import models


# class FlowLog(models.Model):

#     step = models.CharField(max_length=200)

#     status = models.CharField(max_length=20)

#     data = models.TextField(null=True, blank=True)

#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.step

from .flow_storage import save_flow_log

def log_step(step, data=None, status="INFO"):

    save_flow_log(step, status, data)

    FLOW_LOGS.append({
        "step": step,
        "status": status,
        "data": str(data)
    })