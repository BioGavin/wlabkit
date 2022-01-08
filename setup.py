import io
import re
import os
from setuptools import find_packages
from setuptools import setup

__version__ = "0.0.1"

here = os.path.abspath(os.path.dirname(__file__))

with io.open("README.rst", "rt", encoding="utf8") as f:
    readme = f.read()


setup(
    name='WLab',
    version=__version__,
    url='https://github.com/BioGavin/wlab',
    license='GPL',
    author='Zhen-Yi Zhou',
    author_email="gavinchou64@gmail.com",
    description="A toolkit to handle bio-data from WeiBin Lab.",
    long_description=readme,
    classifiers=["Programming Language :: Python :: 3.8"],
    scripts=['scripts/wlab.py'],
    packages=['src'],
    package_dir={"": "src"},
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=[
        "biopython=1.79"
    ]
)