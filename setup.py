from setuptools import find_packages
from setuptools import setup

__version__ = "0.0.2"


with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='wlab',
    version=__version__,
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
    scripts=['scripts/wlab'],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=[
        "biopython",
        "numpy"
    ]
)
