from django.db import models


class FlowLog(models.Model):

    step = models.CharField(max_length=200)

    status = models.CharField(max_length=20)

    data = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.step