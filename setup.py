#!/usr/bin/python3
from distutils.core import setup

setup(
    name='Directory Searched',
    version='1.0',
    description='Changes directory based on a search',
    author='Jake Torrance',
    author_email='jaket1234@hotmail.com',
    packages=['dir_search'],
    package_dir={'dir_search': 'src/dir_search'},
    scripts=['bin/dir_search']
)
