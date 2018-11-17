The Twitter API
===============

Coo is written using the `Python Twitter <https://github.com/bear/python-twitter/>`_
wrapper, and through `Coo.api` you gain access to all of his models:

.. code-block:: python

    # get your followers
    followers = at.api.GetFollowers()

    # get your direct messages
    d_messages = at.api.GetDirectMessages()

    # favorited tweets
    favorites = at.api.GetFavorites()

    # mentions
    mentions = at.api.GetMentions()

    # retweets
    retweets = at.api.GetRetweets()

And a lot more. If you are interested, check their `documentation <https://python-twitter.readthedocs.io/en/latest/index.html>`_.
