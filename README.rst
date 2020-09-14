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

The goal of sylenium is to create a test framework agnostic browser (selenium wrapper) automation library to help
development teams write end to end tests for their web applications without all the necessary boilerplate that is
required to achieve stability with selenium.


=============
Official Documentation :flags:
=============

https://sylenium.readthedocs.io/

==============
Configuring Sylenium :flags:
==============

.. code-block:: python

    # Coming soon

==============
Quick Start :flags:
==============

Here is a simple way to get going for a standalone simple library script that requires some browser interaction:

.. code-block:: python

    import sylenium import *

    def main():
        # google search => No setup at all, just install sylenium with pip
        with get_driver():
            go("https://www.bing.com")
            find(ById("sb_form_q")).set_text("Hello World").clear().set_text("My Search").press_enter()
            find(ById("b_results")).should_be(Visible).should_contain(Text("My Search"))


For those building more robust automation frameworks around their applications, here is an example harnessing Page Objects:

.. code-block:: python

    # Complex Page Objects Approach:
    from __future__ import annotations
    from sylenium import *

    class BingPage:
        search_box = find(ById("sb_form_q") # Lazy
        results_box = find(ById("b_results") # Lazy

        def __init__(self) -> None:
            ... # No driver necessary, sylenium is very smart with driver management

        def perform_search(search_term: str) -> BingPage:
          search_box.clear().set_text(search_term)).press_enter(0)
          return self

        def check_results_contains(search_term: str) -> BingPage:
            # conditions are inbuilt assertions, failing tests accordingly
            results_box.should_be(Visible).should_contain(Text(search_term)))
            return self


    # Note: This is a pytest explicit example and bing_page is a 'fixture'
    def test_bing_searching(bing_page) -> None:
        term = "sylenium"
        bing_page.perform_search(term)
        bing_page.check_results_contains(term)


==============
Sylenium-pytest :flags:
==============

Plugin (coming soon)
