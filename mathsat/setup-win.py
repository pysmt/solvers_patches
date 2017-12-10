#!/usr/bin/env python
import os
from setuptools import setup, Extension

MATHSAT_DIR = '..'

libraries = ['mathsat', 'psapi', 'mpir']

setup(name='mathsat', version='0.1',
      description='MathSAT API',
      ext_modules=[Extension('_mathsat', ['mathsat_python_wrap.c'],
                             define_macros=[('SWIG','1')],
                             include_dirs=[os.path.join(MATHSAT_DIR,
                                                        'include')],
                             library_dirs=[os.path.join(MATHSAT_DIR, 'lib')],
                             extra_compile_args=[],
                             extra_link_args=[],
                             libraries=libraries,
                             language='c++',
                             )]
      )
