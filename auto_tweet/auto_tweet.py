from typing import Union, List, Dict

import twitter

from .time_managment import zzz, DELAY_DICT, INTERVAL_DICT


class AutoTweet:
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
        if delay:
            # if 'delay' is not 'None', first, try to sleep, but if
            # there is a 'TypeError' use 'get_time()' to get the
            # int value from the DELAY_DICT. Raise a custom NoneError
            # if the key is wrong. If there is no 'delay', just post
            # the Update.
            zzz(delay, DELAY_DICT)

        if self.debug:
            return f"msg: {msg} - delay: {delay}"

        return self.connect.PostUpdate(msg)

    def tweets(
        self,
        msgs: Union[List, Dict],
        delay: Union[str, int] = None,
        interval: Union[str, int] = None,
    ):
        """Post multiple tweets with delay and interval options."""
        if delay:
            zzz(delay, DELAY_DICT)

        if isinstance(msgs, list):
            # Use a generator
            twitter_msgs = (i for i in msgs)
            for msg in twitter_msgs:
                if self.debug:
                    print(f"msg: {msg} - delay: {delay} - interval: {interval}")
                else:
                    self.connect.PostUpdate(msg)

                # !FIXME: Remove interval at the end of the loop.
                if interval:
                    zzz(interval, INTERVAL_DICT)

        if isinstance(msgs, dict):
            pass

    def __str__(self) -> str:
        return f"Twitter User: {self.verify.name}"

    def __repr__(self) -> str:
        return "AutoTweet('{}', '{}', '{}', '{}')".format(
            self.consumer, self.consumer_secret, self.token, self.token_secret
        )
