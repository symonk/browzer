.. image:: .github/banner.png
  :class: with-border
  :width: 1280

========
Overview :flags:
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs:
      - |docs|
    * - tests:
      - | |travis| |requires| |codecov|
    * - package:
      - | |version|
    * - infra:
      - | |github-actions|

.. |docs| image:: https://readthedocs.org/projects/sylenium/badge/?style=flat
    :target: https://sylenium.readthedocs.io/en/latest/
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.org/symonk/sylenium.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/symonk/sylenium

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/symonk/sylenium?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/symonk/sylenium

.. |requires| image:: https://requires.io/github/symonk/sylenium/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/symonk/sylenium/requirements/?branch=master

.. |codecov| image:: https://codecov.io/gh/symonk/sylenium/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/symonk/sylenium

.. |version| image:: https://img.shields.io/pypi/v/sylenium.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/sylenium

.. |wheel| image:: https://img.shields.io/pypi/wheel/sylenium.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/sylenium

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/sylenium.svg
    :alt: Supported versions
    :target: https://pypi.org/project/sylenium

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/sylenium.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/sylenium

.. |github-actions| image:: https://github.com/symonk/sylenium/workflows/Release%20Sylenium/badge.svg
    :alt: Automated Releasing
    :target: https://github.com/symonk/sylenium/workflows/Release%20Sylenium/badge.svg


.. end-badges

========
What is Sylenium? :flags:
========

Selenium wrapper for automating web applications end to end. Sylenium helps you get off the ground running and has a
core focus on improving stability of selenium when used for test writing.  With Selenium 4 upcoming, Sylenium aims for
its first release in Q1 2021.  Sylenium contains test runner framework plugin(s) and is test runner agnostic.


=============
Official Documentation :flags:
=============

https://sylenium.readthedocs.io/

==============
Configuring Sylenium :flags:
==============

Everything in sylenium begins with a Session(config: Configuration), all spawned browsers are contained within these
sessions, this avoids globals everywhere and major headaches, especially unit testing for us!  At the moment, a single
browser is mapped to a single session and these are fully customisable at runtime, as well as usable as ctx managers.
Note: Syleniums defaults are pretty savvy and are ideal when you are writing basic scripts.

.. code-block:: python

    def my_session():
        from sylenium import Session
        session = Session()
        driver = session.get_webdriver()
        # Requires clean up

    def my_ctx_session():
        from sylenium import Session
        with Session() as session:
            driver = session.get_webdriver()
            # do whatever with the driver... (auto cleaned up)

    def customising_a_session():
        from sylenium import Session
        config = Configuration(headless=True, download_directory="/tmp/", remote=True)
        with Session(configuration=config) as session:
            driver = session.get_webdriver() # fully configured with your own options



==============
Quick Start :flags:
==============

.. code-block:: python

    def test_without_page_objects():
        # Without page objects, for simple scripts
        start("https://localhost:8080/login.html")
        find("login-username").set_text("admin")
        find("login-pwd").set_text("password")
        click("login-btn-submit")

    def test_with_page_objects():
        login_page = start(LoginPage)
        dashboard = login_page.login_as("admin", "password")
        find("my-widget").should_have(visible_text("Custom Widget")) # asserts under the hood
        element: SyleniumElement = find("another-widget")
        element.should_be(clickable())

==============
Sylenium-pytest :flags:
==============

Plugin (coming soon)
