#!/usr/bin/env python

from setuptools import setup


setup(name='rmodel',
      description='simple redis model',
      author='dsociative',
      author_email='admin@geektech.ru',
      packages=['rmodel', 'rmodel.fields', 'rmodel.models', 'rmodel.sessions'],
      package_dir={'rmodel': 'rmodel'},
      dependency_links=[
          
      ],
      install_requires=[
          'redis',
          
      ]
)
