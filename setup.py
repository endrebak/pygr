#!/usr/bin/env python
"""
Pygr
====

Pygr is an open source software project used to develop graph database
interfaces for the popular Python language, with a strong emphasis
on bioinformatics applications ranging from genome-wide analysis of
alternative splicing patterns, to comparative genomics queries of
multi-genome alignment data.
"""

from distutils.core import setup
# from distutils.extension import Extension
from setuptools import find_packages, Extension, Command
from Cython.Build import cythonize

import os
import sys

# try:
#     from setuptools import setup, Extension
# except ImportError:
#     # print 'Setuptools not imported, falling back to distutils'
#     from distutils.core import setup, Extension

import pygr


def error(msg):
    "Fatal errors"
    print('*** error %s' % msg)
    sys.exit()

PYGR_NAME = "pygr"
PYGR_VERSION = pygr.__version__

if sys.version_info < (2, 3):
    error('pygr requires python 2.3 or higher')

CLASSIFIERS = """
Development Status :: 5 - Production/Stable
Operating System :: MacOS :: MacOS X
Operating System :: Microsoft :: Windows :: Windows NT/2000
Operating System :: OS Independent
Operating System :: POSIX
Operating System :: POSIX :: Linux
Operating System :: Unix
Programming Language :: Python
Topic :: Scientific/Engineering
Topic :: Scientific/Engineering :: Bio-Informatics
"""

# split into lines and filter empty ones
CLASSIFIERS = filter(None, CLASSIFIERS.splitlines())

# extension sources

extensions = [Extension("pygr.cdict", ["pygr/cdict.pyx", "pygr/cgraph.c"]),
              Extension("pygr.seqfmt", ["pygr/seqfmt.pyx"]),
              Extension("pygr.cnestedlist", ["pygr/cnestedlist.pyx", "pygr/apps/maf2nclist.c", "pygr/intervaldb.c"])]


def main():
    setup(
        name = PYGR_NAME,
        version= PYGR_VERSION,
        packages=find_packages(),
        ext_modules = cythonize(extensions),
        description = \
'Pygr, a Python graph-database toolkit oriented primarily on bioinformatics',
        long_description = __doc__,
        author = "Christopher Lee",
        author_email='leec@chem.ucla.edu',
        url = 'http://code.google.com/p/pygr/',
        license = 'New BSD License',
        classifiers = CLASSIFIERS,

        package_data={'': ['*.pyx', '*.pxd', '*.h', '*.c']},
        include_dirs=["."],

        # packages = ['pygr', 'pygr.apps'],

        # ext_modules = [
        #     Extension('pygr.seqfmt', seqfmt_src),
        #     Extension('pygr.cdict', cdict_src),
        #     Extension('pygr.cnestedlist', nested_src),
        # ],

     )

if __name__ == '__main__':
    main()
