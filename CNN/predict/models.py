from django.db import models

# Create your models here.
class PredResults(models.Model):

    sentence = models.CharField(max_length=100)
    position1 = models.IntegerField()
    position2 = models.IntegerField()
    classification = models.CharField(max_length=30)
    def __str__(self):
        return self.classification