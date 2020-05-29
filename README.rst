========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - documentation
      - |docs|
    * - testing
      - | |travis| |appveyor| |requires| |codecov|

.. |docs| image:: https://readthedocs.org/projects/browzer/badge/?style=flat
    :target: https://readthedocs.org/projects/browzer
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.org/symonk/browzer.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/symonk/browzer

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/symonk/browzer?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/symonk/browzer

.. |requires| image:: https://requires.io/github/symonk/browzer/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/symonk/browzer/requirements/?branch=master

.. |codecov| image:: https://codecov.io/gh/symonk/browzer/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/symonk/browzer

.. |version| image:: https://img.shields.io/pypi/v/browzer.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/browzer

.. |wheel| image:: https://img.shields.io/pypi/wheel/browzer.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/browzer

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/browzer.svg
    :alt: Supported versions
    :target: https://pypi.org/project/browzer

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/browzer.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/browzer

.. |commits-since| image:: https://img.shields.io/github/commits-since/symonk/browzer/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/symonk/browzer/compare/v0.0.0...master



.. end-badges

Selenium wrapper placeholder

* Free software: MIT license

Installation
============

::

    pip install browzer

You can also install the in-development version with::

    pip install https://github.com/symonk/browzer/archive/master.zip


Documentation
=============


https://browzer.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
