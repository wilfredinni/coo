from typing import Union

import twitter

from .utils import zzz, tweet_template, DELAY_DICT, INTERVAL_DICT
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
        """Verify if the authentication is valid."""

        return self.connect.VerifyCredentials()

    def tweet(
        self,
        msg: Union[str, list],
        delay: Union[int, str] = None,
        interval: Union[str, int, None] = None,
        template: str = None,
    ):
        """Post a Twitter Update from a sting or a list."""

        if self.debug:
            print(f"delay: {delay} - interval: {interval}")

        # Delay the post if needed.
        self.delay(delay)

        if isinstance(msg, str):
            # This is for a single tweet, just post or print.

            # if template:
            #     msg = templates(template=template, msg=msg)

            self.str_update(msg, template)

        elif isinstance(msg, list):
            # For one or multiple tweet Updates
            self.list_update(msg, interval, template)

        else:
            raise TweetTypeError(TweetTypeError.tweetInfoMsg)

    def str_update(self, msg: str, template=None):
        """Process one Twitter Update."""

        if template:
            msg = tweet_template(msg=msg, template=template)

        if self.debug:
            print(msg)
        else:
            self.connect.PostUpdate(msg)

    def list_update(self, msg: list, interval: Union[int, str] = None, template=None):
        """Process and prepare a list of tweet Updates."""

        for update in msg:

            if interval:
                self.interval(interval)

            self.str_update(update, template)

    def delay(self, delay: Union[str, int, None]):
        """Delay the Post of one or multiple tweets."""

        if delay and self.delay_time:
            zzz(delay, DELAY_DICT)

            # Set to False to avoid repetition
            self.delay_time = False

    def interval(self, interval: Union[int, str]):
        """Add an interval between Tweeter Updates."""

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
