from typing import Dict
import time

try:
    from exceptions import NoneError
except ModuleNotFoundError:
    from .exceptions import NoneError

DELAY_STR: Dict[str, int] = {
    "half_hour": 2,  # 1800
    "one_hour": 4,  # 3600
    "tomorrow": 6,  # 86400
    "next_week": 8,  # 604800
}

INTERVAL_STR: Dict[str, int] = {
    "once_a_day": 2,  # 86400
    "twice_perday": 4,  # 43200
    "three_times_day": 6,  # 28800
}


# TODO: function or function decorator for intervals in tweets()


def delay_tweet(time_delay):
    """Delay a tweet update. """
    if type(time_delay) is int:
        return time.sleep(time_delay)

    sleep_time = DELAY_STR.get(time_delay)
    try:
        return time.sleep(sleep_time)
    except TypeError:
        raise NoneError(NoneError.delayInfoMessage)


if __name__ == "__main__":

    class Test:
        def tweet(self, msg: str, delay=None):
            """Post a single tweet with or without time delay."""
            if delay:
                delay_tweet(delay)

            print(f"msg: {msg} - delay: {delay}")

    t = Test()
    t.tweet("My test Twitter update", 3)
