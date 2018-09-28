from typing import Union, List, Dict

import twitter

from .utils import zzz, DELAY_DICT, INTERVAL_DICT
from .exceptions import TweetTypeError


class AutoTweet:
    """The heart of the AutoTweet Library."""

    def __init__(
        self,
        consumer: str,
        consumer_secret: str,
        token: str,
        token_secret: str,
        debug: bool = False,
    ) -> None:

        self.consumer = consumer
        self.consumer_secret = consumer_secret
        self.token = token
        self.token_secret = token_secret

        # True to debug purposes
        self.debug = debug

        # interval and delay switches
        self.delay_time = True
        self.interval_time = False

        # Creates the connection through the Twitter API
        self.connect = twitter.Api(
            self.consumer, self.consumer_secret, self.token, self.token_secret
        )

    @property
    def verify(self):
        """ Verify if the authentication is valid """

        return self.connect.VerifyCredentials()

    def tweet(self, msg: str, delay: Union[str, int] = None):
        """Post a single tweet with or without a time delay."""

        if not isinstance(msg, str):
            raise TweetTypeError(TweetTypeError.tweetInfoMsg)

        if delay and self.delay_time:
            zzz(delay, DELAY_DICT)

            # Set to False to avoid repetition
            self.delay_time = False

        if self.debug:
            debug_msg = f"msg: {msg} - delay: {delay}"
            print(debug_msg)
            return debug_msg

        return self.connect.PostUpdate(msg)

    def tweets(
        self,
        msgs: Union[List, Dict],
        delay: Union[str, int] = None,
        interval: Union[str, int] = None,
    ):
        """Post multiple tweets with delay and interval options."""

        for msg in msgs:

            if interval:
                self.interval(interval)

            if isinstance(msgs, list):
                self.tweet(msg, delay)

            elif isinstance(msgs, dict):
                pass

            else:
                raise TweetTypeError(TweetTypeError.tweetsInfoMsg)

    def interval(self, interval):

        # Avoid the first iteration:
        if self.interval_time:
            zzz(interval, INTERVAL_DICT)

        # Enabled for the second iteration:
        self.interval_time = True

    def __str__(self) -> str:
        return f"Twitter User: {self.verify.name}"

    def __repr__(self) -> str:
        return "AutoTweet('{}', '{}', '{}', '{}')".format(
            self.consumer, self.consumer_secret, self.token, self.token_secret
        )
