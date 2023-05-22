from django.db import models

class Measurement(models.Model):
    value = models.DecimalField(max_digits=7, decimal_places=2)
    measured_date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField()


    def __str__(self):
        return f"({self.value} {self.measured_date} {self.notes})"