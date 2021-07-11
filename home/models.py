from django.db import models
from unixtimestampfield.fields import UnixTimeStampField

class AlembicVersion(models.Model):
    version_num = models.CharField(primary_key=True, max_length=32)

    class Meta:
        managed = False
        db_table = 'alembic_version'


class Food(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    timestamp_unix = UnixTimeStampField(auto_now_add=True)
    timestamp_obj = models.DateTimeField(blank=True, null=True)
    calorie = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'food'

    def __str__(self):
        return '{} at {}'.format(self.name, self.timestamp_obj)

class HomeMisc(models.Model):
    total_calories = models.IntegerField(blank=True, null=True)
    bulk_items = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'home_misc'


class HomeValue(models.Model):
    total_calories = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'home_value'


class Misc(models.Model):
    timestamp_unix = models.FloatField(blank=True, null=True)
    timestamp_obj = models.DateTimeField(blank=True, null=True)
    amount_weight = models.FloatField(blank=True, null=True)
    amount_steps = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'misc'

    def __str__(self):
        return f'Weight: {self.amount_weight}| Steps:{self.amount_steps}  at {self.timestamp_obj}'