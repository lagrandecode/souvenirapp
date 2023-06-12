from django.db import models

# Create your models here.


class Feedback(models.Model):
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name