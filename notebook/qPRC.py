# coding: utf-8

# qPRC workflow
# =============
# qPRC main workflow in a single, hopefully simple, notebook.
# - mainly used for debugging
#
# Dependencies
# ------------

# In[1]:

# standard library modules
import os


# external modules
import pandas as pd
import numpy as np


# Global settings
# ----------------

# In[2]:

DATA_LOC = '../data/'


# Parsing the data
# -----------------

# In[3]:

filepath = os.path.join(DATA_LOC, 'raw_input.csv')


# In[4]:

dna = pd.read_csv(filepath, index_col=[0,1])
dna = dna.transpose()
dna.index = [int(s.split(' ')[1]) for s in dna.index]
dna.index.name = 'cycle'
#dna.columns
dna.head()


# Plotting
# ---------

# Some examples of selecting data. [loc](http://pandas.pydata.org/pandas-docs/stable/indexing.html#different-choices-for-indexing-loc-iloc-and-ix) is a label-based selection method.
#
# All rows, single column.

# In[5]:

#dna.loc[:, 15].plot()


# First 5 rows, 2 columns.

# In[6]:

#dna.loc[:5, 15:16].plot()


# Single dye only.

# In[7]:

#dna.loc[:,(15, 'SYBR')].plot()
#show()
# cross-section in columns: axis=1
# two levels: 0 (cycle) and 1 (dye)
#dna.xs('SYBR', level=1, axis=1).loc[:,15:17].plot()


# Modeling
# --------
# Automatically slice.

# In[8]:

#concentrations = dna.loc[:,(31, 'SYBR')][:40].values
concentrations_raw = dna.loc[:,(31, 'SYBR')]
#concentrations_raw.plot(style='r--')
conc_diff = concentrations_raw.diff()
decrease_start_index = conc_diff[conc_diff<0].index[0]
concentrations_series = concentrations_raw[: decrease_start_index - 1]
#concentrations_series.plot(style='r-')
concentrations = concentrations_series.values


# In[9]:

# concentrations_series.plot()
# show()


# ### Older model

# Fit the model.

# In[17]:

import numpy as np
import math
from scipy.optimize import curve_fit
import ipdb

k = 1
n = 5
nx = 1
nc = 5
mode = 0
maxit = 100000
iprt = 0

# input_file_name = 'inp.txt'

# concentrations = np.loadtxt(input_file_name)

# offset
offset = np.mean(concentrations[5:8])

# expression
last_reading = concentrations[-1]
index = np.where((concentrations - offset) > 0.1 * last_reading)[0][0]
expression = ((concentrations[index] - offset) /
              math.exp(math.log(2.0)*index*1.0))

# rate
rate = 1.0

# reactants
reactants = last_reading/2.0

# power
power = 1.0

sy = concentrations.copy()
for i, elm in enumerate(concentrations):
    if (elm > 1.5 * offset) and (elm < 0.5 * last_reading):
        sy[i] = 0.5
    elif (i < index - 10):
        sy[i] = 2.5
    elif (elm > last_reading/1.5):
        sy[i] = 1.2

# bounds
al = 0.0
variables = np.array([5*offset, last_reading, 1.01, last_reading + 10.0, 3.0])
print(variables)

def f(meas, offset, n0, gama, nn, alfa):
    meas_calc = np.zeros(len(meas))
    for i in meas:
        # ipdb.set_trace()
        broj = np.zeros(i)
        if n0 < 0 or nn < 0:
            return np.repeat(1e10, len(meas))
        broj[0] = n0
        suma = n0
        for idx in range(1, i):
            broj[idx] = broj[idx - 1] * (1.0 + gama /
                                         (1.0 +
                                          math.exp(alfa * math.log(suma / nn))))
            suma = suma + broj[idx]

        meas_calc[i - 1] = broj[-1] + offset
    return meas_calc

times = list(range(1, len(concentrations) + 1))
fitted_params = curve_fit(f, times, concentrations, p0=variables)
params = fitted_params[0]
print(params)


# In[18]:

concentrations


# In[19]:

f(times, *params) - concentrations


# Plot the model.

# In[21]:

fitted_vals = f(times, *params)

#plot(times, concentrations, 'k-', label='measurements')
#plot(times, fitted_vals, 'r--', label='model')
#legend(loc='upper left')
#show()


# ### Newer model

# In[22]:

import sys
qprc_path = os.path.abspath(os.path.join('..'))
if qprc_path not in sys.path:
    sys.path.append(qprc_path)


# In[26]:

#from qPRC.lib.fitter import f

def f(meas, offset, n0, gama, nn, alfa):
    # ipdb.set_trace()
    meas_calc = np.zeros(len(meas))
    for i in meas:
        num = np.zeros(i)
        prim = np.zeros(i)
        if n0 < 0 or nn < 0:
            return np.repeat(1e10, len(meas))
        num[0] = n0
        summ = n0
        prim[0] = nn
        for idx in range(1, i):
            num[idx] = num[idx - 1] * (
                1.0 + gama / (1.0 + alfa * (summ / prim[idx - 1]))
            )
            summ = summ + num[idx]
            prim[idx] = prim[idx - 1] - (num[idx] - num[idx - 1])

        meas_calc[i - 1] = num[-1] + offset
    return meas_calc

good_variables = [1.76050783e+05, 5.78e+02, +1.13766225e+00,
                  7.42308865e+05, 8.11068606e+00]
times = list(range(1, len(concentrations) + 1))
fitted_params = curve_fit(f, times, concentrations, p0=good_variables)
params = fitted_params[0]
print(params)

fitted_vals = f(times, *params)

#plot(times, concentrations, 'k-', label='measurements')
#plot(times, fitted_vals, 'r--', label='model')
#legend(loc='upper left')
#show()


# In[14]:
