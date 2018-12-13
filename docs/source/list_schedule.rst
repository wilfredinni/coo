Schedule a list of strings
==========================

Post ordered updates with `Delay`_, `Interval`_, and a `Template`_ if needed.

.. code-block:: python

    Coo.tweet(updates, delay, interval, template, time_zone)

.. code-block:: python

    from coo import Coo

    at = Coo(
        "consumer_key",
        "consumer_secret",
        "access_token",
        "access_token_secret"
    )

    tweets = [
        "My first awesome Twitter Update",
        "My second awesome Twitter Update",
        "My third awesome Twitter Update",
        "My fourth awesome Twitter Update",
        "My fifth awesome Twitter Update",
        "My sixth awesome Twitter Update",
    ]

    # post the twitter updates
    at.tweet(tweets)

Delay
^^^^^

You can use ``datetime``, ``date`` and ``time`` strings, integers as seconds and some
`Keywords`_: ``half_hour``, ``one_hour``, ``one_day`` and ``one_week`` between others to
delay the post of your first update.

.. code-block:: python

    # datetime, date and time strings
    at.tweet(tweets, delay="2030-11-24 13:45", time_zone="America/Santiago")
    at.tweet(tweets, delay="2030-11-24", time_zone="Australia/Sydney")
    at.tweet(tweets, delay="13:45", time_zone="America/New_York")

    # "keywords"
    at.tweet(tweets, delay="one_week")

    # integer
    at.tweet(tweets, delay=604800)

.. note::

    When parsing DateTime strings:

    - If a time zone is not specified, it will set to `local`.
    - The time will be set to 00:00:00 if it's not specified.
    - When passing only time information the date will default to today.
    - A future date is needed, otherwise a `ScheduleError` is raised.

Here you can find all the `Time Zones <https://en.wikipedia.org/wiki/List_of_tz_database_time_zones>`_.

Interval
^^^^^^^^

Use integers as seconds or some strings as `Keywords`_: ``half_hour``, ``one_hour``,
``one_day`` and ``one_week`` between others.

.. code-block:: python

    # "keywords"
    at.tweet(tweets, interval="four_hours")

    # integers
    at.tweet(tweets, interval=14400)

Media files
^^^^^^^^^^^

Use one media file for all of your updates:

.. code-block:: python

    at.tweet(tweets, media="path/to/media.jpeg")

Random updates
^^^^^^^^^^^^^^

To tweet your updates randomly:

.. code-block:: python

    at.tweet(tweets, aleatory=True)

Keywords
^^^^^^^^

================ =======
Keyword          Seconds
================ =======
now              0
half_hour        1800
one_hour         3600
two_hours        7200
four_hours       14400
six_hours        21600
eight_hours      28800
ten_hours        36000
twelve_hours     43200
fourteen_hours   50400
sixteen_hours    57600
eighteen_hours   64800
twenty_hours     72000
twenty_two_hours 79200
one_day          86400
two_days         172800
three_days       259200
four_days        345600
five_days        432000
six_days         518400
one_week         604800
================ =======

Template
^^^^^^^^
You can also set one template for each one of the updates.

.. code-block:: python

    at.tweet(tweets, template=template)

Templates are very simple, just use a multiline string and add a `$message` where you want your message to appear.

.. code-block:: python

    template = """My aswesome header

    $message

    #python #coding #coo
    """