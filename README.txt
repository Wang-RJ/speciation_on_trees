Implementation of algorithm for testing models of hybrid incompatibility accumulation on phylogenetic trees.
Applicable if you want to test models on a three species complex and you have branch lengths and counts of the
number of shared/unique incompatibilities (in at least two species pairs).

This implementation was originally written in Python 2.7
Requires NumPy (http://www.numpy.org/) for scientific computing and SciPy (http://www.scipy.org/) for its
implementation of Broyden-Fletcher-Goldfarb-Shanno (BFGS) algorithm.

<evcEqsEPL.py> contains definitions for expectations, variances, covariances as well as likelihood functions
for different models and wrapper functions for missing data.

<maxlikeEPL.py> contains functions for maximizing the likelihood functions of different models given
observations of incompatibilities between species and relative divergence times.

<help.txt> contains details on usage of functions in maxlikeEPL.py