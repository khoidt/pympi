#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
from distutils.core import setup

licence = '"THE BEER-WARE LICENSE" (Revision 42)'
version = '1.6'

with open('README.md', 'r', encoding='utf8') as readme:
   long_description = readme.read()

setup(name='pympi-ling',
      version=version,
      description=
        'A python module for processing ELAN and Praat annotation files',
      author='Mart Lubbers',
      long_description=long_description,
      author_email='mart@martlubbers.net',
      url='https://github.com/dopefishh/pympi',
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Environment :: Console',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.4',
                   'Topic :: Text Processing :: Linguistic'],
      packages=['pympi'])
