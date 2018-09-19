from typing import Iterable, Dict
import time
import twitter

# from_seconds_to: Dict[str, int] = {"tomorrow": 86400, "hour": 3600, "half_hour": 1800}
# intervals: Dict[str, int] = {"once_a_day": 86400}


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

    def tweet(self, msg: str, count_down: int = None):
        """Posts a Twitter Update through the Twitter API

        Arguments:
            msg {str} -- Tweeter Message

        Keyword Arguments:
            count_down {int} -- (default: {None})
            If Provided, Delay the Execution of the
            Update for a Given Number of Seconds.
        """
        if count_down:
            time.sleep(count_down)

        # self.connect.PostUpdate(msg)
        print(msg)

    # def tweet_interval(
    #     self, messages: Iterable[str], interval: int, random: bool = False
    # ):
    #     if random:
    #         pass
    #     else:
    #         for msg in messages:
    #             self.connect.PostUpdate(msg)
    #             time.sleep(interval)

    @property
    def verify(self):
        try:
            return self.connect.VerifyCredentials()

        except twitter.error.TwitterError as e:
            raise e

    def __str__(self) -> str:
        return f"{self.verify.name} - {self.verify.created_at}"

    def __repr__(self) -> str:
        return "AutoTweet('{}', '{}', '{}', '{}')".format(
            self.consumer, self.consumer_secret, self.token, self.token_secret
        )


if __name__ == "__main__":
    pass
