from django.db import models

class Lista(models.Model):
    data = models.DateField()
    hora = models.TimeField()
    total = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.data} - {self.hora} - {self.total}"
