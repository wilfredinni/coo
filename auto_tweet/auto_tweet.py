from typing import Union

import twitter

from .time_managment import delay_tweet


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

        # Verify if the twitter.User authentication is valid
        self.verify = self.connect.VerifyCredentials()

    def tweet(self, msg: str, delay: Union[str, int] = None):
        """Post a single tweet with or without time delay."""
        if delay:
            delay_tweet(delay)

        # self.connect.PostUpdate(msg)
        print(f"msg: {msg} - delay: {delay}")

    # TODO: Post several tweets with time delay and interval options

    def __str__(self) -> str:
        return f"Twitter User: {self.verify.name}"

    def __repr__(self) -> str:
        return "AutoTweet('{}', '{}', '{}', '{}')".format(
            self.consumer, self.consumer_secret, self.token, self.token_secret
        )
