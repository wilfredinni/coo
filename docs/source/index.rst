=============================
coo: Schedule Twitter updates
=============================

.. raw:: html

    <embed>
        <p align="center"><img src="https://raw.githubusercontent.com/wilfredinni/coo/master/coo.png" alt="Logo"></p>
    </embed>

.. raw:: html

    <embed>
        <p align="center">
            <a href="https://badge.fury.io/py/coo">
                <img src="https://badge.fury.io/py/coo.svg" alt="PyPI version" height="18">
            </a>
            <a href="https://travis-ci.org/wilfredinni/coo">
                <img src="https://travis-ci.org/wilfredinni/coo.svg?branch=master" alt="Build Status">
            </a>
            <a href="https://codecov.io/gh/wilfredinni/coo">
                <img src="https://codecov.io/gh/wilfredinni/coo/branch/master/graph/badge.svg" alt="codecov">
            </a>
            <a href="https://opensource.org/licenses/Apache-2.0">
                <img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="License">
            </a>
        </p>
    </embed>

Coo is an easy to use Python library for scheduling Twitter updates. To use it, you need
to first apply for a developer account in the
`Twitter Developers Platform <https://developer.twitter.com/>`_ and generate the Keys and
Access Tokens.

.. code-block:: python

    from coo import Coo

    at = Coo(
        "consumer_key",
        "consumer_secret",
        "access_token",
        "access_token_secret"
    )

    tweets = [
        ("2030-12-05 16:30", template, "Awesome Twitter update."),
        ("2030-10-28 18:50", template, "Another awesome Twitter update."),
        ("2030-10-29 18:15", template2, "One more update."),
        ("2030-11-01 13:45", None, "Twitter update without a template."),

    at.schedule(tweets, time_zone="America/Santiago")

Or you can use a list of strings and add a ``delay``, ``interval`` and ``template``:

.. code-block:: python

    tweets = [
        "My first awesome Twitter Update",
        "My second awesome Twitter Update",
        "My third awesome Twitter Update",
        "My fourth awesome Twitter Update",
        "My fifth awesome Twitter Update",
        "My sixth awesome Twitter Update",
    ]

    at.tweet(tweets, delay="13:45", interval="four_hours", template=my_template)

User Guide
^^^^^^^^^^

.. toctree::
   :maxdepth: 2

   schedule
   list_schedule
   twitter_api
   changelog

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
