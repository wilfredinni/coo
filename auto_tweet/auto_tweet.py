from typing import Dict, Union, List
import functools
import twitter

delay: Dict[str, int] = {
    "half_hour": 2,  # 1800
    "one_hour": 4,  # 3600
    "tomorrow": 6,  # 86400
    "next_week": 8,  # 604800
}

intervals: Dict[str, int] = {
    "once_a_day": 2,  # 86400
    "twice_perday": 4,  # 43200
    "three_times_day": 6,  # 28800
}


def time_delay(func):
    import time

    @functools.wraps(func)
    def wrapper_delay(*args, **kwargs):
        sleep_time = parse_time(delay, kwargs, "delay")
        try:
            time.sleep(sleep_time)
        except TypeError:
            raise NoneArgumentError(NoneArgumentError.delayInfoMessage)

        return func(*args, **kwargs)

    return wrapper_delay


def parse_time(dictionary, time_delay, keyword):
    time_delay = time_delay.get(keyword)

    if type(time_delay) == int:
        return time_delay
    if type(time_delay) == str:
        return dictionary.get(time_delay)


# def check_and_sleep(time_interval):
# if interval:
#     if type(interval) == int:
#         time.sleep(interval)

#     if type(interval) == str:
#         try:
#             time_str = test_intervals.get(interval)
#             time.sleep(time_str)
#         except TypeError:
#             raise NoneArgumentError(NoneArgumentError.intervalInfoMessage)


class NoneArgumentError(TypeError):
    """Raised when the string argument provided to count_down is not valid."""

    delayInfoMessage = (
        "'delay' must be an int(secs) or a valid String: "
        "'half_hour', 'one_hour', 'tomorrow' or 'next_week'."
    )

    intervalInfoMessage = (
        "'interval' must be an int(secs) or a valid String: "
        "'once_a_day', 'twice_perday' or 'three_times_day'."
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

    @time_delay
    def tweet(self, msg: str, delay: Union[str, int] = None):
        """Post a single tweet with or without time delay."""

        # self.connect.PostUpdate(msg)
        print(f"msg: {msg} - delay: {delay}")

    # @time_delay
    # def tweets(self, msgs, delay=None, interval=None):
    #     """Post multiple tweets with time delay and interval options."""
    #     check_and_sleep(delay=delay)

    #     for post in msgs:
    #         # self.connect.PostUpdate(msg)
    #         print(f"msg: {post} - delay: {delay} - interval: {interval}")

    def __str__(self) -> str:
        return f"Twitter User: {self.verify.name}"

    def __repr__(self) -> str:
        return "AutoTweet('{}', '{}', '{}', '{}')".format(
            self.consumer, self.consumer_secret, self.token, self.token_secret
        )
