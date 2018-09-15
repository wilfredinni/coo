#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

requirements = []

test_requirements = ["pytest"]

setup(
    author="Carlos Montecinos Geisse",
    author_email="carlos.w.montecinos@gmail.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    description="",
    entry_points={"console_scripts": ["auto_tweet=auto_tweet.cli:main"]},
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme,
    include_package_data=True,
    keywords="auto_tweet",
    name="auto_tweet",
    packages=find_packages(include=["auto_tweet"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/wilfredinni/auto_tweet",
    version="0.1.0",
    zip_safe=False,
)
