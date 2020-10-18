*****
SciPy
*****


Rationale
=========
SciPy (pronounced "Sigh Pie") is open-source software for mathematics, science, and engineering. It includes modules for statistics, optimization, integration, linear algebra, Fourier transforms, signal and image processing, ODE solvers, and more. It is also the name of a very popular conference on scientific programming with Python.

The SciPy library depends on NumPy, which provides convenient and fast N-dimensional array manipulation. The SciPy library is built to work with NumPy arrays, and provides many user-friendly and efficient numerical routines such as routines for numerical integration and optimization. Together, they run on all popular operating systems, are quick to install, and are free of charge. NumPy and SciPy are easy to use, but powerful enough to be depended upon by some of the world's leading scientists and engineers. If you need to manipulate numbers on a computer and display or publish the results.

SciPy builds on the NumPy array object and is part of the NumPy stack which includes tools like Matplotlib, pandas and SymPy, and an expanding set of scientific computing libraries. This NumPy stack has similar users to other applications such as MATLAB, GNU Octave, and Scilab. The NumPy stack is also sometimes referred to as the SciPy stack.

* https://www.scipy.org/
* https://github.com/scipy/scipy

.. code-block:: python

    import scipy

    help(scipy)
    # Help on package scipy:
    # NAME
    #  scipy
    # FILE
    #  c:\python25\lib\site-packages\scipy\__init__.py
    # DESCRIPTION
    #  SciPy --- A scientific computing package for Python
    #  ===================================================
    #  Documentation is available in the docstrings and
    #  online at http://docs.scipy.org.
    #  Contents
    #  --------
    #  SciPy imports all the functions from the NumPy namespace, and in
    #  addition provides:
    #  Available subpackages
    #  ---------------------
    #  odr --- Orthogonal Distance Regression [*]
    #  misc --- Various utilities that don't have another home.
    #  sparse.linalg.eigen.arpack --- Eigenvalue solver using iterative methods. [*]
    #  fftpack --- Discrete Fourier Transform algorithms [*]
    #  io --- Data input and output [*]
    #  sparse.linalg.eigen.lobpcg --- Locally Optimal Block Preconditioned Conjugate Gradient Method (LOBPCG) [*]
    #  special --- Airy Functions [*]
    #  lib.blas --- Wrappers to BLAS library [*]
    #  sparse.linalg.eigen --- Sparse Eigenvalue Solvers [*]
    #  stats --- Statistical Functions [*]
    #  lib --- Python wrappers to external libraries [*]
    #  lib.lapack --- Wrappers to LAPACK library [*]
    #  maxentropy --- Routines for fitting maximum entropy models [*]
    #  integrate --- Integration routines [*]
    #  ndimage --- n-dimensional image package [*]
    #  linalg --- Linear algebra routines [*]
    #  spatial --- Spatial data structures and algorithms [*]
    #  interpolate --- Interpolation Tools [*]
    #  sparse.linalg --- Sparse Linear Algebra [*]
    #  sparse.linalg.dsolve.umfpack --- :Interface to the UMFPACK library: [*]
    #  sparse.linalg.dsolve --- Linear Solvers [*]
    #  optimize --- Optimization Tools [*]
    #  cluster --- Vector Quantization / Kmeans [*]
    #  signal --- Signal Processing Tools [*]
    #  sparse --- Sparse Matrices [*]

    # [*] - using a package requires explicit import (see pkgload)

.. code-block:: python

    import scipy
    import scipy.interpolate

.. csv-table:: Scipy
    :header: "module", "Description"
    :widths: 10, 90

    "scipy.constants", "Many mathematical and physical constants."
    "scipy.special", "Special functions for mathematical physics, such as iry, elliptic, bessel, gamma, beta, hypergeometric, parabolic cylinder, mathieu, spheroidal wave, struve, and kelvin functions."
    "scipy.integrate", "Functions for performing numerical integration using trapezoidal, Simpson's, Romberg, and other methods. Also provides methods for integration of ordinary differential equations."
    "scipy.optimize", "Standard minimization / maximization routines that operate on generic user-defined objective functions. Algorithms include: Nelder-Mead Simplex, Powell's, conjugate gradient, BFGS, least-squares, constrained optimizers, simulated annealing, brute force, Brent's method, Newton's method, bisection method, Broyden, Anderson, and line search."
    "scipy.linalg", "Much broader base of linear algebra routines than NumPy. Offers more control for using special, faster routines for specific cases (e.g., tridiagonal matrices). Methods include: inverse, determinant, solving a linear system of equations, computing norms and pseudo/generalized inverses, eigenvalue/eigenvector decomposition, singular value decomposition, LU decomposition, Cholesky decomposition, QR decomposition, Schur decomposition, and various other mathematical operations on matrices."
    "scipy.sparse", "Routines for working with large, sparse matrices."
    "scipy.interpolate", "Routines and classes for interpolation objects that can be used with discrete numeric data. Linear and spline interpolation available for one- and two-dimensional data sets."
    "scipy.fftpack", "Fast Fourier transform routines and processing."
    "scipy.signal", "Signal processing routines, such as convolution, correlation, finite fourier transforms, B-spline smoothing, filtering, etc."
    "scipy.stats", "Huge library of various statistical distributions and statistical functions for operating on sets of data."
