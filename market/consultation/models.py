from django.db import models
from django.contrib.auth.models import User

class ConsultationRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    consultant = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    message = models.TextField()

    def __str__(self):
        return f"Consultation with {self.consultant} on {self.date_time}"
