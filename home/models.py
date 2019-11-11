from django.db import models

# Maybe worth change so imports relevant info from api into db
class SignificantLaunch(models.Model):
    flight_number = models.IntegerField()

    class Meta:
        verbose_name = 'Significant Launch'
        verbose_name_plural = 'Significant Launches'
