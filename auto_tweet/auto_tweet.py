from typing import Union, List, Dict
import twitter

from .time_managment import zzz, DELAY_STR, INTERVAL_STR


class AutoTweet:
    def __init__(
        self, consumer: str, consumer_secret: str, token: str, token_secret: str
    ) -> None:
        self.consumer = consumer
        self.consumer_secret = consumer_secret
        self.token = token
        self.token_secret = token_secret

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
            # there is a 'TypeError' use 'delay_time_int()' to get the
            # int value from the DELAY_STR dict. Raise a custom NoneError
            # if the key is wrong. If there is nothing in 'delay', just post
            # the Update.
            zzz(delay, DELAY_STR)

        # return self.connect.PostUpdate(msg)
        return f"msg: {msg} - delay: {delay}"

    def tweets(
        self,
        msgs: Union[List, Dict],
        delay: Union[str, int] = None,
        interval: Union[str, int] = None,
    ):
        """Post multiple tweets with delay and interval options."""
        if delay:
            zzz(delay, DELAY_STR)

        # !FIXME: Remove interval at the end of the loop.
        if isinstance(msgs, list):
            for post in msgs:
                # return self.connect.PostUpdate(post)
                print(f"msg: {post} - delay: {delay} - interval: {interval}")
                if interval:
                    zzz(interval, INTERVAL_STR)

    def __str__(self) -> str:
        return f"Twitter User: {self.verify.name}"

    def __repr__(self) -> str:
        return "AutoTweet('{}', '{}', '{}', '{}')".format(
            self.consumer, self.consumer_secret, self.token, self.token_secret
        )
