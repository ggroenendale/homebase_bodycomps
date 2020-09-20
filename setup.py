import os
import re

from setuptools import setup, find_packages

# Define here as the location of this file
here = os.path.abspath(os.path.dirname(__file__))
os.chdir(here)

setup(
    name = "bodycomps",
    author = "Geoff Groenendale",
    author_email = "g.groenendale@gmail.com",
    setup_requires = ['setuptools_scm'],
    description = "A few scripts to pull data from the Withings API",
    license = "BSD",
    keywords = "withings api data body composition",
    packages = ["bodycomps", "tests"]
)