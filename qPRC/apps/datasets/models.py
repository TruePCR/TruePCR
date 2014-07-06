from django.db import models

class Dataset(models.Model):
    file = models.FileField(upload_to='files/%Y/%m/%d')
