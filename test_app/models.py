from django.db import models


class SampleModel(models.Model):
    field1 = models.CharField(max_length=32, null=True, blank=True)
    field2 = models.CharField(max_length=32, null=True, blank=True)
    field3 = models.CharField(max_length=32, null=True, blank=True)
    field4 = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.field1
