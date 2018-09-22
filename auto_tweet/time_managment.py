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


def delay_tweet(time_delay, dictionary):
    """Delay a Twitter Update. """
    sleep_time = dictionary.get(time_delay)
    # At this point, the 'sleep_time' comes from the one of the
    # dictionaries. If the return value is 'None', means that the
    # value provided by the user is not valid, so a 'NoneError'
    # is raised.
    try:
        return sleep_time
    except TypeError:
        raise NoneError(NoneError.delayInfoMessage)


if __name__ == "__main__":

    class Test:
        def tweet(self, msg: str, delay=None):
            """Post a single tweet with or without time delay."""
            if delay:
                try:
                    time.sleep(delay)
                except TypeError:
                    sleep_time = delay_tweet(delay, DELAY_STR)
                    time.sleep(sleep_time)

            print(f"msg: {msg} - delay: {delay}")

    t = Test()
    t.tweet("My test Twitter update", "half_hour")

    # a = delay_tweet("half_hour")
    # print(type(a))
