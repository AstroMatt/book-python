import sys
from distutils.core import setup, Extension

if sys.version_info >= (3,):
    print('Building for Python 3')
    module = Extension('hello', sources = ['hello-python3.c'])
elif sys.version_info >= (2,):
    print('Building for Python 2')
    module = Extension('hello', sources=['hello-python2.c'])
else:
    print('Unsupported Python version')
    sys.exit(1)

setup(
    name = 'hello',
    version='1.0',
    description = 'Ehlo World!',
    ext_modules = [module])

