#!/usr/bin/env python


from setuptools import find_packages, setup

LONG_DESCRIPTION = "CRATE"

INSTALL_REQUIRES = [
    "docutils==0.17",  # documentation, 0.18 not compatible with Sphinx
    "sphinx==4.4.0",  # documentation
]

setup(
    name="crate-anon",
    version="1.0",
    description="CRATE: clinical records anonymisation and text extraction",
    long_description=LONG_DESCRIPTION,
    url="https://crateanon.readthedocs.io",
    author="Rudolf Cardinal",
    author_email="rudolf@pobox.com",
    license="GNU General Public License v3 or later (GPLv3+)",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
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
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
)
