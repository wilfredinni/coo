from typing import Union, List, Dict

import twitter

from .utils import zzz, DELAY_DICT, INTERVAL_DICT


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
        # Verify if the twitter.User authentication is valid
        return self.connect.VerifyCredentials()

    def tweet(self, msg: str, delay: Union[str, int] = None):
        """Post a single tweet with or without a time delay."""

        # If there is a 'TypeError' raises NoneError.
        if delay and self.delay_time:
            zzz(delay, DELAY_DICT)

            # Set to False to avoid repetition
            self.delay_time = False

        if self.debug:
            # print(f"msg: {msg} - delay: {delay}")
            return f"msg: {msg} - delay: {delay}"

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
                if self.interval_time:
                    zzz(interval, INTERVAL_DICT)
                # True to interval after first iteration.
                self.interval_time = True

            self.tweet(msg, delay)

    def __str__(self) -> str:
        return f"Twitter User: {self.verify.name}"

    def __repr__(self) -> str:
        return "AutoTweet('{}', '{}', '{}', '{}')".format(
            self.consumer, self.consumer_secret, self.token, self.token_secret
        )
