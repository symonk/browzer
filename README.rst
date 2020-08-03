.. image:: .github/banner.png
  :width: 800

========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs:
      - |docs|
    * - tests:
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

========
Browzer Overview
========

Selenium wrapper for automating web applications end to end. Browzer helps you get off the ground running and has a
core focus on improving stability of selenium when used for test writing.  With Selenium 4 upcoming, Browzer aims for
its first release in Q1 2021.  Browzer contains test runner framework plugin(s) and is test runner agnostic.

=============
Browzer Configuration
=============

Browzer offers a wide range of configuration options and a pain free way to provide and override such option(s) to fit
your needs.  The default configuration is outlined below:

    .. code-block:: yaml

        browzer:
          browser: "chrome"  # chrome|firefox
          headless: True
          remote: True
          selenium_grid_url: "http://127.0.0.1:4444/wd/hub"
          selenium_grid_port: 4444
          browser_resolution: "1280x1024"
          browser_version: "latest"
          driver_binary_path: "acquire"
          browser_capabilities: {}
          chrome_options: []
          base_url: ""
          explicit_waiting: 30.00
          polling_interval: 0.25
          page_source_capturing: False
          page_screenshot_capturing: False
          stack_trace_capturing: False
          javascript_clicks: False
          javascript_sendkeys: False
          default_selector: "css"
          page_loading_strategy: = "fast"  # slow|fast
          driver_listener_module_class_path: null



In order to override any of these options, the BROWZER_CONFIGURATION environment variable should store a path to your
own yaml file; any of the overridden keys will then be merged into the default and applied at runtime before the library
is imported.

=============
Documentation
=============

https://browzer.readthedocs.io/
