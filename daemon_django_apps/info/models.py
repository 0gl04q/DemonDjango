from django.db import models


class CPUInfo(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    cpu = models.FloatField()

    class Meta:
        ordering = ('-time',)
        indexes = [models.Index(fields=['time'], name='time_idx')]

    def __str__(self):
        return f'Time: {self.time}, CPU %: {self.cpu}'
