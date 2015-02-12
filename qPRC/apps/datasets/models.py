from django.db import models

from qPRC.lib.parser import parse

class Dataset(models.Model):
    file = models.FileField(upload_to='files/%Y/%m/%d')

    def __str__(self):
        return str(self.file)

    def data(self):
        """return the parsed data from the Dataset file"""
        try:
            return self._data
        except AttributeError:
            self._data = parse(self.file.url)
            return self._data

