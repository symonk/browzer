#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
import re
from distutils.core import setup
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages


def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names), encoding=kwargs.get("encoding", "utf8")
    ) as fh:
        return fh.read()


VERSION_FILE = "src/sylenium/_version.py"
version_str_line = open(VERSION_FILE, "rt").read()
version_regex = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(version_regex, version_str_line, re.M)
if mo:
    version_string = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSION_FILE,))


setup(
    name="sylenium",
    version=version_string,
    license="MIT",
    description="Selenium wrapper placeholder",
    long_description="This is an example placeholder for sylenium",
    author="Simon Kerr",
    author_email="jackofspaces@gmail.com",
    url="https://github.com/symonk/sylenium",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Utilities",
    ],
    project_urls={
        "Documentation": "https://sylenium.readthedocs.io/",
        "Changelog": "https://sylenium.readthedocs.io/en/latest/changelog.html",
        "Issue Tracker": "https://github.com/symonk/sylenium/issues",
    },
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
    python_requires=">=3.7",
    install_requires=[
        "appdirs==1.4.4",
        "assertpy==1.0",
        "atomicwrites==1.4.0",
        "attrs==20.1.0",
        "certifi==2020.6.20",
        "chardet==3.0.4",
        "colorama==0.4.3",
        "configparser==5.0.0",
        "coverage==5.2.1",
        "crayons==0.4.0",
        "distlib==0.3.1",
        "filelock==3.0.12",
        "idna==2.10",
        "iniconfig==1.0.1",
        "more-itertools==8.5.0",
        "packaging==20.4",
        "pluggy==0.13.1",
        "py==1.9.0",
        "pyparsing==2.4.7",
        "pytest==6.0.1",
        "pytest-cov==2.10.1",
        "pytest-travis-fold==1.3.0",
        "PyYAML==5.3.1",
        "requests==2.24.0",
        "selenium==3.141.0",
        "six==1.15.0",
        "toml==0.10.1",
        "tox==3.19.0",
        "urllib3==1.25.10",
        "virtualenv==20.0.31",
        "webdriver-manager==3.2.2",
    ],
    extras_require={
        # eg:
        #   'rst': ['docutils>=0.11'],
        #   ':python_version=="2.6"': ['argparse'],
    },
)
