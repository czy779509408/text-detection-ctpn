from distutils.core import setup
from Cython.Build import cythonize
import numpy as np

try:
    numpy_include = np.get_include()
except AttributeError:
    numpy_include = np.get_numpy_include()

setup(
    ext_modules=cythonize(["bbox.pyx","cython_nms.pyx"],include_path=[numpy_include]),
)

# export CFLAGS=-I/usr/local/anaconda3/lib/python3.6/site-packages/numpy/core/include
# python setup.py build
