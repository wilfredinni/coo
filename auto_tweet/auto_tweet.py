import twitter

from .time_managment import sleep


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

    def tweet(self, msg: str, delay=None):
        """Post a single tweet with or without a time delay."""
        if delay:
            # if 'delay' is not 'None', first, try to sleep, but if
            # there is a 'TypeError' use 'delay_time_int()' to get the
            # int value from the DELAY_STR dict. If there is nothing
            # in 'delay', just post the Update.
            sleep(delay)

        # return self.connect.PostUpdate(msg)
        print(f"msg: {msg} - delay: {delay}")

    def __str__(self) -> str:
        return f"Twitter User: {self.verify.name}"

    def __repr__(self) -> str:
        return "AutoTweet('{}', '{}', '{}', '{}')".format(
            self.consumer, self.consumer_secret, self.token, self.token_secret
        )
