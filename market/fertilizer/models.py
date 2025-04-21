from django.db import models

class FertilizerRecommendation(models.Model):
    crop = models.CharField(max_length=50)
    fertilizer_type = models.CharField(max_length=50)
    amount_per_acre = models.FloatField(help_text="Amount in kg per acre")

    def __str__(self):
        return f"{self.crop} - {self.fertilizer_type}"
