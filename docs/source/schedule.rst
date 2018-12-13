Schedule Twitter Updates
========================

Schedule updates with `datetime` strings or integers and use custom `Templates`_ if needed.

.. code-block:: python

    Coo.schedule(updates, time_zone)

Full example:

.. code-block:: python

    from coo import Coo

    at = Coo(
        "consumer_key",
        "consumer_secret",
        "access_token",
        "access_token_secret"
    )

    tweets = [
        # datetime with and without templates
        ("2030-10-28 18:50", template, "My Twitter update with a template."),
        ("2030-10-29 18:15", template2, "Update with a different template."),
        ("2030-11-01 13:45", None, "Twitter update without a template."),

        # date with and without templates
        ("2030-12-25", template3, "Merry christmas!"),
        ("2031-01-01", None, "And a happy new year!"),

        # time with and without templates
        ("18:46", template2, "Will be post today at 18:46."),
        ("23:00", None, "A tweet for today at 23:00."),

        # integer (seconds) with and without templates
        (3600, template, "This tweet will be posted in an hour."),
        (86400, None, "This one, tomorrow at the same hour."),
    ]

    at.schedule(tweets, time_zone="America/Santiago")

Parsing DateTime strings
^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

    - If a time zone is not specified, it will set to `local`.
    - The time will be set to 00:00:00 if it's not specified.
    - When passing only time information the date will default to today.
    - A future date is needed, otherwise a `ScheduleError` is raised.

Here you can find all the `Time Zones <https://en.wikipedia.org/wiki/List_of_tz_database_time_zones>`_.

Media Files
^^^^^^^^^^^

There are two ways to add media files to your tweets. The first and easiest is to use one global file for all the updates:

.. code-block:: python

    at.schedule(tweets, time_zone="America/Santiago", media="path/to/file.png")

Also, an individual file can be set for each one of the updates:

.. code-block:: python

    tweets = [
        ("2030-10-28 18:50", template, "Update with an image.", "pics/owl.png"),
        ("2030-10-29 18:15", template, "Update with other media.", "videos/funny_video.mp4"),
        ("2030-11-01 13:45", template, "Tweet without media."),
    ]

Finally, it is possible to combine these to ways. For example, if most of the tweets are gonna use the same media and just a few will have a different or none:

.. code-block:: python

    tweets = [
        ("2030-11-01 13:45", template, "Tweet with global media."),
        ("2030-11-02 13:45", template, "Tweet with global media."),
        ("2030-11-03 13:45", template, "Tweet with global media."),
        ("2030-11-04 13:45", template, "Tweet with global media."),
        ("2030-11-05 13:45", template, "Tweet with global media."),
        ("2030-11-06 13:45", template, "Tweet with global media."),
        ("2030-11-07 13:45", template, "Tweet with global media."),
        ("2030-11-08 13:45", template, "Tweet without media.", None),
        ("2030-11-09 13:45", template, "Tweet without media.", None),
        ("2030-12-10 18:50", template, "Update with an image.", "pics/owl.png"),
        ("2030-12-11 18:15", template, "Update with other media.", "videos/funny_video.mp4"),
    ]

    at.schedule(tweets, time_zone="America/Santiago", media="path/to/global_media.png")

Templates
^^^^^^^^^

You can set different templates for each one of your updates, or none.

.. code-block:: python

    tweets = [
        # datetime with and without templates
        ("2030-10-28 18:50", template, "My Twitter update with a template."),
        ("2030-10-29 18:15", template2, "Update with a different template."),
        ("2030-11-01 13:45", None, "Twitter update without a template."),

    ]

    at.schedule(tweets, time_zone="America/Santiago")

Templates are very simple, just use a multiline string and add a `$message` where you want your message to appear.

.. code-block:: python

    template = """My aswesome header

    $message

    #python #coding #coo
    """