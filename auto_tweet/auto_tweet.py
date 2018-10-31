from typing import Union
import asyncio

import twitter

from .utils import zzz, tweet_template, parse_or_get
from .exceptions import TweetTypeError, ScheduleError

# TODO: write the test to raise a ScheduleError for the wrong len(tuple).
# TODO: change the print for logging in str_update().
# TODO: revisit comments and docstrings.
# TODO: rewrite the README.


class AutoTweet:
    """
    Easily schedule Twitter updates.

    Note: to use this library you need to create an account on
    https://developer.twitter.com/ and generate Keys and Access
    Tokens.

    Attributes
    ----------
    consumer : str
        Twitter consumer key.
    consumer_secret : str
        Twitter consumer secret.
    token : str
        Twitter token.
    token_secret : str
        Twitter token secret.
    preview : bool, optional
        True to print the update(s) on the console
        and not publish on Twitter (default is False).

    Methods
    -------
    verify()
        Verify if the authentication is valid.
    tweet(updates, delay=None, interval=None, template=None, time_zone="local")
        Post Twitter Updates from a list of strings.
    schedule(updates, time_zone='local')
        Post multiple Twitter Updates from a list of tuples.
    str_update()
        Post a Twitter Update from a string.
    """

    time_zone: str = "local"

    def __init__(
        self,
        consumer: str,
        consumer_secret: str,
        token: str,
        token_secret: str,
        preview: bool = False,
    ) -> None:
        """
        Parameters
        ----------
        consumer : str
            Twitter consumer key.
        consumer_secret : str
            Twitter consumer secret.
        token : str
            Twitter token.
        token_secret : str
            Twitter token secret.
        preview : bool, optional
            True to print the update(s) on the console
            and not publish on Twitter (default is False).
        """
        # Creates the connection through the Twitter API.
        self.connect = twitter.Api(consumer, consumer_secret, token, token_secret)

        # True to preview the update in the console.
        self.preview = preview

        # interval and delay switches.
        self.delay_time = True
        self.interval_time = False

        # The async loop for the custom updates.
        self.loop = asyncio.get_event_loop()

    @property
    def verify(self):
        """Verify if the authentication is valid."""

        return self.connect.VerifyCredentials()

    def tweet(
        self,
        updates: list,
        delay: Union[int, str] = None,
        interval: Union[str, int, None] = None,
        template: str = None,
        time_zone: str = time_zone,
    ):
        """
        Post Twitter Updates from a list of strings with
        delay, interval and template options.

        Parameters
        ----------
        updates : list
            A list of strings, each one is a Twitter Update.
        delay : int, str, optional
            The time before the first Update.
        interval : str, int, optional
            The time between Updates.
        template : str, optional
            Multiline string containing a '$message' that will
            be replaced with the Twitter update.
        time_zone : str, optional
            Sets a time zone for parsing date, time or
            datetime strings (default is 'local').

            e.g. "America/Santiago"

            https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

        Raises
        ------
        TweetTypeError
            Raised when 'updates' is not an instance of list, or
            the elements in the list are not strings.
        """
        self.delay(delay, time_zone)

        if not isinstance(updates, list):
            raise TweetTypeError(TweetTypeError.tweetInfoMsg)

        elif isinstance(updates[0], str):
            for update in updates:
                if interval:
                    self.interval(interval)

                self.str_update(update, template)

        else:
            raise TweetTypeError(TweetTypeError.wrongListMsg)

    def schedule(self, updates: list, time_zone=time_zone):
        """
        Post multiple Twitter Updates from a list of tuples.

        Parameters
        ----------
        updates : list
            A list of tuples that contains the datetime, the template and the
            update message:

            [("datetime", "template", "update msg")]

            e.g.

            [("2040-10-30 00:05", template, "Update msg")]

            Notes for parsing date and time strings:
            - If a time zone is not specified, it will be set to local.
            - When passing only time information the date will default to today.
            - The time will be set to 00:00:00 if it's not specified.
            - A future date is needed, otherwisem a ScheduleError is raised.

        time_zone : str, optional
            Sets a time zone for parsing date, time or datetime strings
            (default is 'local').

            e.g. "America/Santiago"

            https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

        Raises
        ------
        ScheduleError
            Raised when the lenght of the tuple on a list is
            greater or less than 3.
        """
        if not isinstance(updates[0], tuple):
            raise ScheduleError(ScheduleError.wrongListMsg)

        self.loop.run_until_complete(self.async_tasks(updates, time_zone))
        self.loop.close()

    def str_update(self, update: str, template: Union[str, None]):
        """
        Post a Twitter Update from a string.

        Parameters
        ----------
        update : str
            A string representing a Twitter Update.
        template : str, optional
            Multiline string containing a '$message' that will
            be replaced with the Twitter update.

        Returns
        -------
        twitter.Api.PostUpdate
            Post the update to Twitter.
        """
        if template:
            update = tweet_template(update=update, template=template)

        if self.preview:
            print(update)
            return

        return self.connect.PostUpdate(update)

    async def async_tasks(self, custom_msgs: list, time_zone: str):
        """Perare the asyncio tasks for the custom tweets."""
        for msg in set(custom_msgs):
            if len(msg) != 3:
                # Raises a ScheduleError if the len of the typle is less tan 3.
                raise ScheduleError(ScheduleError.tupleLenError)

        await asyncio.wait(
            [
                self.loop.create_task(self.custom_updates(post, time_zone))
                for post in custom_msgs
            ]
        )

    async def custom_updates(self, msg: tuple, time_zone: str):
        """
        Process custom updates: templates and updates times for every
        Twitter update.
        """
        seconds = parse_or_get(msg[0], time_zone)
        await asyncio.sleep(seconds)

        return self.str_update(update=msg[2], template=msg[1])

    def delay(self, delay: Union[str, int, None], time_zone):
        """Delay the Post of one or multiple tweets."""
        if delay and self.delay_time:
            zzz(delay, time_zone)

            # Set to False to avoid repetition
            self.delay_time = False

    def interval(self, interval: Union[int, str]):
        """Add an interval between Twitter Updates."""
        # Avoid the first iteration
        if self.interval_time:
            zzz(interval)

        self.interval_time = True

    def __str__(self):
        return f"Twitter User: {self.verify.name}."
