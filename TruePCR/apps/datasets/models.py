from django.db import models
import pandas as pd

from TruePCR.lib.parser import parse
from TruePCR.lib.fitter import fit as _fit
from TruePCR.lib.fitter import slice as _slice

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

    # TODO: method to return the time series of fitted values
    def fitted_values(self, well, dye):
        params = self.fit(well, dye)
        concentrations = _slice(data.loc[:,(well, dye)])
        times = list(range(1, len(concentrations) + 1))
        fitted_vals = f(times, *params)
        s = pd.Series(fitted_vals, times)
        return fitted_vals
