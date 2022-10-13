# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Area(models.Model):
    """Модель областей Республики"""
    name = models.CharField(max_length=128)

    class Meta:
        def __str__(self):
            return self.name


class Years(models.Model):
    """Модель с записанными годами"""
    year = models.DateField()


class Fertility(models.Model):
    """Модель смертности"""
    number = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    area = models.ForeignKey(Area, on_delete=models.CASCADE)  # Field name made lowercase.
    year = models.ForeignKey(Years, on_delete=models.CASCADE)  # Field name made lowercase.


class Lifeextantion(models.Model):
    """Модель средней продолжительности жизни"""
    year = models.ForeignKey(Years, on_delete=models.CASCADE)
    age = models.FloatField(blank=True, null=True)


class Mortality(models.Model):
    """Модель рождаемости"""
    mortal = models.IntegerField()
    id_years = models.ForeignKey(Years, on_delete=models.CASCADE)
    id_area = models.ForeignKey(Area, on_delete=models.CASCADE)
