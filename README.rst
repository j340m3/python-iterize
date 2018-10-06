========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |coveralls| |codecov|
        | |landscape| |scrutinizer| |codacy| |codeclimate|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/python-iterize/badge/?style=flat
    :target: https://readthedocs.org/projects/python-iterize
    :alt: Documentation Status


.. |travis| image:: https://travis-ci.org/j340m3/python-iterize.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/j340m3/python-iterize

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/j340m3/python-iterize?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/j340m3/python-iterize

.. |requires| image:: https://requires.io/github/j340m3/python-iterize/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/j340m3/python-iterize/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/j340m3/python-iterize/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/j340m3/python-iterize

.. |codecov| image:: https://codecov.io/github/j340m3/python-iterize/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/j340m3/python-iterize

.. |landscape| image:: https://landscape.io/github/j340m3/python-iterize/master/landscape.svg?style=flat
    :target: https://landscape.io/github/j340m3/python-iterize/master
    :alt: Code Quality Status

.. |codacy| image:: https://img.shields.io/codacy/REPLACE_WITH_PROJECT_ID.svg
    :target: https://www.codacy.com/app/j340m3/python-iterize
    :alt: Codacy Code Quality Status

.. |codeclimate| image:: https://codeclimate.com/github/j340m3/python-iterize/badges/gpa.svg
   :target: https://codeclimate.com/github/j340m3/python-iterize
   :alt: CodeClimate Quality Status

.. |version| image:: https://img.shields.io/pypi/v/iterize.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/iterize

.. |commits-since| image:: https://img.shields.io/github/commits-since/j340m3/python-iterize/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/j340m3/python-iterize/compare/v0.1.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/iterize.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/iterize

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/iterize.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/iterize

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/iterize.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/iterize

.. |scrutinizer| image:: https://img.shields.io/scrutinizer/g/j340m3/python-iterize/master.svg
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/j340m3/python-iterize/


.. end-badges

Python optimisation Framework using iterative repair.

* Free software: MIT license

Installation
============

::

    pip install iterize

Documentation
=============


https://python-iterize.readthedocs.io/


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
