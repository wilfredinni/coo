from setuptools import setup, find_packages
import re

with open("coo/__init__.py", "r") as file:
    regex_version = r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]'
    version = re.search(regex_version, file.read(), re.MULTILINE).group(1)

with open("README_P.rst") as readme_file:
    readme = readme_file.read()


requirements = ["python-twitter", "pendulum"]

test_requirements = ["pytest", "flake8", "flake8-mypy", "black"]

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
    description="Schedule Twitter Updates with Easy",
    install_requires=requirements,
    license="MIT License",
    long_description=readme,
    include_package_data=True,
    keywords="coo",
    name="coo",
    packages=find_packages(include=["coo"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/wilfredinni/coo",
    version=version,
    zip_safe=False,
)
