from django.db import models

from qPRC.lib.parser import parse
from qPRC.lib.fitter import fit as _fit

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

    def fit(self, well, dye):
        """return the fitted model of the concentrations"""
        params = _fit(self.data(), well, dye)
        return params
        # TODO: just store the params

    # TODO: method to return the time series of fitted values
