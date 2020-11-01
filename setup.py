# Import statements
import os
import io
import re

from setuptools import setup, find_packages

# Package meta-data
NAME = 'bodycomps'
DESCRIPTION = 'A few scripts to pull data from the Withings API'
URL = 'https://github.com/ggroenendale/bodycomps'
EMAIL = 'g.groenendale@gmail.com'
AUTHOR = 'Geoff Groenendale'
REQUIRES_PYTHON = '>=3.6.0'


def read(*names, **kwargs):
    with io.open(
            os.path.join(os.path.dirname(__file__), *names),
            encoding=kwargs.get('encoding', 'utf8')
    ) as fp:
        return fp.read()


# Define cwd as the current working directory of this file
cwd = os.path.abspath(os.path.dirname(__file__))
os.chdir(cwd)

setup(
    name=NAME,
    version='',
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    setup_requires=['setuptools_scm'],
    license='MIT',
    keywords='withings api data body composition',
    packages=['bodycomps', 'tests'],
    long_description=read("README.md"),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Natural Language :: English',
        'Topic :: Home Automation'
    ]
)
