#!/usr/bin/env python2
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

requisites = []

setup(
    name='ml_search',
    version='1.0',
    description='Search all header of mailing-list on OpenStack',
    keywords='openstack, mailing-list',
    install_requires=[
        'requests'
    ],
    scripts=['scripts/ml_search'],
    long_description=open('README.rst').read(),
    author='Nguyen Hoai Nam',
    author_email='namptit307@gmail.com',
    url='https://github.com/NguyenHoaiNam/search_mailling_list',
    packages=['ml_search'],
    license='MIT',
    classifiers=[
        'Environment :: Console',
        'Topic :: Terminals :: Terminal Emulators/X Terminals',
    ],
)
