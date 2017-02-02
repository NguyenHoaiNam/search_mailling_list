#!/usr/bin/env python2
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import searchs

requisites = []

setup(
    name='ml_search',
    version=searchs.__version__,
    description='Search all header of mailling-list on Openstack',
    scripts=['scripts/ml_search'],
    long_description=open('README.rst').read(),
    author='Nam Nguyen Hoai',
    author_email='namptit307@gmail.com',
    url='https://github.com/NguyenHoaiNam/search_mailling_list',
    packages=['ml_search'],
    license='MIT',
    classifiers=[
        'Environment :: Console',
        'Topic :: Terminals :: Terminal Emulators/X Terminals',
    ],
)
