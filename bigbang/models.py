from django.db import models

# Create your models here.
class BigBangTheory(models.Model):
    name = models.CharField(max_length=256)
    desgination = models.CharField(max_length=256)
    performance = models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return self.name
