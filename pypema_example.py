# -*- coding: utf-8 -*-
"""
A. Folch-Fortuny, R. Marques, I. Isidro, R. Oliveira, A. Ferrer
Copyright (C) 2015 A. Folch-Fortuny
Copyright (C) 2018 R. Marques

This file is part of PyPEMA.

PyPEMA is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

PyPEMA is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with PyPEMA.  If not, see <https://www.gnu.org/licenses/>.
"""

import numpy as np

from pema import pypema
from pema import plotfuncs
from pema import dataio

"""
This script exemplifies how to run PyPEMA using an interactive environment such
as IPython. PyPEMA computes the Principal Elementary Modes, providing an
Elementary Mode matrix (EM) and a matrix of flux states (X). PyPEMA also
provides several vizualization tools to interpret the results. All these steps
will be exemplified in this script.

Please consult the documentation for further details about the PEMA algorithm.
"""

# Define the PyPEMA parameters
nrel = 3 # number of relaxations
nbranch = 1 # number of branch points
maxPEMs = 5 # number of PEMs to be extracted
# data_filename = 'ecoli.mat' # should be a .mat file present in the data folder containing both flux and the elementary mode matrix

# The input data should be a numpy 2D-array for the flux and elementary mode matrices. PyPEMA includes an example MAT file containing both matrices in ./data/ecoli.mat. The module dataio.py contains an utility that handles the conversion of X and EM to a numpy array.
datafile = './data/ecoli.mat'
X, EM = dataio.load_matfile(datafile)

# Run PyPEMA. The results are presented as a 2D-numpy array, with the first
# column corresponding to the percentage of explained variance for each
# set of extracted PEMs, represented on each row.
result = pypema.run(X, EM, nrel, nbranch, maxPEMs)

# -------------- Plot functions -------------------#
# Some plots require the flux (X) and elementary mode (EM) matrices a PEM solution.
PEM_list = np.int64(result[-1, 1:]) # the last row contains the solution with maximum number of PEMs extracted
X, EM = dataio.load_matfile(datafile)

# Print scree plot
plotfuncs.scree_plot(result)

# Print the weights_vars plot. This plot shows the explained variance for
# each individual PEM in the chosen solution.
plotfuncs.weights_vars(X, EM, PEM_list)

# Print the weights plot. The columns represent PEM solution in PEM_list and
# the rows the scenarios in the flux data.
plotfuncs.weighting_plot(X, EM, PEM_list)

# Print plot with observed fluxes vs predicted fluxes (recovered by the PEMs)
plotfuncs.obs_vs_pred(X, EM, PEM_list)

# Print PEM plots. The columns represent a solution of PEMs defined by PEM_list.
# The rows represent the fluxes of the metabolic network
plotfuncs.pem_plot(X, EM, PEM_list)

# Print explained variance per observations plot
plotfuncs.variance_obs(X, EM, PEM_list)
