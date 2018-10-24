import asyncio
from typing import Union

import twitter

from .utils import zzz, tweet_template, get_time, DELAY_DICT, INTERVAL_DICT
from .exceptions import TweetTypeError


class AutoTweet:
    """The heart of the AutoTweet Library."""

    def __init__(
        self,
        consumer: str,
        consumer_secret: str,
        token: str,
        token_secret: str,
        preview: bool = False,
    ) -> None:
        self.consumer = consumer
        self.consumer_secret = consumer_secret
        self.token = token
        self.token_secret = token_secret

        # True to debug purposes
        self.preview = preview

        # interval and delay switches
        self.delay_time = True
        self.interval_time = False

        # The async loop for the custom updates
        self.loop = asyncio.get_event_loop()

        # Creates the connection through the Twitter API
        self.connect = twitter.Api(
            self.consumer, self.consumer_secret, self.token, self.token_secret
        )

    @property
    def verify(self):
        """Verify if the authentication is valid."""
        return self.connect.VerifyCredentials()

    def tweet(
        self,
        msg: list,
        delay: Union[int, str] = None,
        interval: Union[str, int, None] = None,
        template: str = None,
    ):
        """Post a Twitter Update from a list of strings or tuples."""
        self.delay(delay)

        if not isinstance(msg, list):
            raise TweetTypeError(TweetTypeError.tweetInfoMsg)

        elif isinstance(msg[0], str):
            self.list_update(msg, interval, template)

        elif isinstance(msg[0], tuple):
            self.loop.run_until_complete(self.async_tasks(msg))
            self.loop.close()

        else:
            raise TweetTypeError(TweetTypeError.wrongListMsg)

    def list_update(
        self, msg: list, interval: Union[int, str] = None, template: str = None
    ):
        """Process and prepare a list of Strings as Twitter Updates."""
        for update in msg:
            if interval:
                self.interval(interval)

            self.str_update(update, template)

    def str_update(self, msg: str, template: str = None):
        """Post the Twitter Update."""
        if template:
            msg = tweet_template(msg=msg, template=template)

        if self.preview:
            print(msg)
            return

        return self.connect.PostUpdate(msg)

    async def async_tasks(self, custom_msgs: list):
        """Perare the asyncio tasks for the custom tweets."""
        await asyncio.wait(
            [self.loop.create_task(self.custom_updates(post)) for post in custom_msgs]
        )

    async def custom_updates(self, msg: tuple):
        """
        Process custom updates: templates and updates times for every twitter update.
        """
        try:
            await asyncio.sleep(msg[0])
        except TypeError:
            t = get_time(msg[0], DELAY_DICT)
            await asyncio.sleep(t)

        return self.str_update(msg=msg[2], template=msg[1])

    def delay(self, delay: Union[str, int, None]):
        """Delay the Post of one or multiple tweets."""
        if delay and self.delay_time:
            zzz(delay, DELAY_DICT)

            # Set to False to avoid repetition
            self.delay_time = False

    def interval(self, interval: Union[int, str]):
        """Add an interval between Twitter Updates."""
        # Avoid the first iteration
        if self.interval_time:
            zzz(interval, INTERVAL_DICT)

        # Enabled for the second iteration
        self.interval_time = True

    def __str__(self) -> str:
        return f"Twitter User: {self.verify.name}"

    def __repr__(self) -> str:
        return "AutoTweet('{}', '{}', '{}', '{}')".format(
            self.consumer, self.consumer_secret, self.token, self.token_secret
        )
