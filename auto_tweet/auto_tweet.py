from typing import Iterable, Dict, Union
import time
import twitter

# delay: Dict[str, int] = {
#     "half_hour": 1800,
#     "one_hour": 3600,
#     "tomorrow": 86400,
#     "next_week": 604800,
# }

# intervals: Dict[str, int] = {
#     "once_a_day": 86400,
#     "twice_perday": 43200,
#     "three_times_day": 28800,
# }

test_delay: Dict[str, int] = {
    "half_hour": 2,
    "one_hour": 4,
    "tomorrow": 6,
    "next_week": 8,
}

test_intervals: Dict[str, int] = {
    "once_a_day": 2,
    "twice_perday": 4,
    "three_times_day": 6,
}


class NoneArgumentError(TypeError):
    """Raised when the string argument provided to count_down is not valid."""

    infoMessage = (
        "count_down must be an int(secs) or a valid String: "
        "half_hour, one_hour, tomorrow or next_week"
    )


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

    def tweet(self, msg: str, count_down: Union[str, int] = None):
        """Post a single tweet with a time delay option."""
        if type(count_down) == int:
            time.sleep(count_down)  # type: ignore

        if type(count_down) == str:
            time_str = test_delay.get(count_down)  # type: ignore
            try:
                time.sleep(time_str)  # type: ignore
            except TypeError:
                raise NoneArgumentError(NoneArgumentError.infoMessage)

        # self.connect.PostUpdate(msg)
        print(f"msg: {msg} - run with count_down argument: {count_down}")

    def tweets(self, msgs, count_down=None, interval=None):
        """Post multiple tweets with time delay and interval options."""
        pass

    def __str__(self) -> str:
        return f"Twitter User: {self.verify.name}"

    def __repr__(self) -> str:
        return "AutoTweet('{}', '{}', '{}', '{}')".format(
            self.consumer, self.consumer_secret, self.token, self.token_secret
        )
