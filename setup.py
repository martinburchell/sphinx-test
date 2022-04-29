#!/usr/bin/env python

"""
setup.py

===============================================================================

    Copyright (C) 2015-2021 Rudolf Cardinal (rudolf@pobox.com).

    This file is part of CRATE.

    CRATE is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    CRATE is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with CRATE. If not, see <https://www.gnu.org/licenses/>.

===============================================================================

CRATE setup file

To use:

    python setup.py sdist

    twine upload dist/*

To install in development mode:

    pip install -e .

More reasoning is in the setup.py file for CamCOPS.
"""

from setuptools import find_packages, setup
from codecs import open
import os
import platform

# =============================================================================
# Constants
# =============================================================================

# Directories
THIS_DIR = os.path.abspath(os.path.dirname(__file__))  # .../crate

# OS; setup.py is executed on the destination system at install time, so:
RUNNING_WINDOWS = platform.system() == "Windows"

LONG_DESCRIPTION = "CRATE"

# Package dependencies
INSTALL_REQUIRES = [
    "docutils==0.17",  # documentation, 0.18 not compatible with Sphinx
    "sphinx==4.4.0",  # documentation
]

# =============================================================================
# setup args
# =============================================================================

setup(
    name="crate-anon",  # "crate" is taken
    version="1.0",
    description="CRATE: clinical records anonymisation and text extraction",
    long_description=LONG_DESCRIPTION,
    # The project"s main homepage.
    url="https://crateanon.readthedocs.io",
    # Author details
    author="Rudolf Cardinal",
    author_email="rudolf@pobox.com",
    # Choose your license
    license="GNU General Public License v3 or later (GPLv3+)",
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 4 - Beta",
        # Indicate who your project is intended for
        "Intended Audience :: Science/Research",
        # Pick your license as you wish (should match "license" above)
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",  # noqa: E501
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: System :: Hardware",
        "Topic :: System :: Networking",
    ],
    keywords="anonymisation",
    packages=find_packages(),
    # finds all the .py files in subdirectories, as long as there are
    # __init__.py files
    include_package_data=True,  # use MANIFEST.in during install?
    # https://stackoverflow.com/questions/7522250/how-to-include-package-data-with-setuptools-distribute  # noqa: E501
    install_requires=INSTALL_REQUIRES,
)
