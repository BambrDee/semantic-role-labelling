#!/usr/bin/env python
from distutils.core import setup

setup(name='semantic_tagger',
      version='0.1.0',
      description='semantic tagger',
      author='',
      author_email='',
      url='',
      packages=['semantic_tagger', 'semantic_tagger.data', 'classifier.evaluation'],
   	  package_data={'semantic_tagger.data': ['./*']})
