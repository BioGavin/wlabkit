#!/usr/bin/env python

from setuptools import find_packages
from setuptools import setup
import codecs
import os.path

def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")
version=get_version("src/wlabkit/__init__.py")

with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='wlabkit',
    version=version,
    url='https://github.com/BioGavin/wlab',
    license='GPL',
    author='Zhen-Yi Zhou',
    author_email="gavinchou64@gmail.com",
    description="A toolkit to handle bio-data from WeiBin Lab.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=["Programming Language :: Python :: 3.8",
                 "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
                 "Operating System :: OS Independent"],
    scripts=['scripts/wlabkit'],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=[
        "biopython",
        "numpy",
        "pandas",
        "python-dateutil",
        "pytz",
        "six"
    ]
)
