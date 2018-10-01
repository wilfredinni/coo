from typing import Union

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

    def tweet(
        self,
        msg: Union[str, list],
        delay: Union[int, str] = None,
        interval: Union[str, int, None] = None,
    ):
        """Post a Twitter Update from a sting or a list."""

        if delay and self.delay_time:
            zzz(delay, DELAY_DICT)

            # Set to False to avoid repetition
            self.delay_time = False

        if isinstance(msg, str):
            # This if for a single tweet, just post or print.
            if self.debug:
                debug_msg = f"msg: {msg} - delay: {delay}"
                print(debug_msg)
                return debug_msg

            return self.connect.PostUpdate(msg)

        elif isinstance(msg, list):
            # For one or multiple tweets Updates
            for update in msg:

                if interval:
                    self.interval(interval)

                if self.debug:
                    debug_msg = f"msg: {update} - delay: {delay}"
                    print(debug_msg)
                else:
                    self.connect.PostUpdate(update)

        else:
            raise TweetTypeError(TweetTypeError.tweetInfoMsg)

    def interval(self, interval: Union[int, str]):

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
