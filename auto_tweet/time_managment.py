from typing import Dict
import time

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


def delay_time_int(time_delay, dictionary: Dict) -> int:
    """Get the time delay for a Twitter Update."""

    # Get the 'int' value from the 'str' provided and return it.
    sleep_time = dictionary.get(time_delay)
    if isinstance(sleep_time, int):
        return sleep_time

    # If 'sleep_time' == None:
    # First: Choose the correct error message.
    err_msg = NoneError.delayInfoMessage
    if dictionary is INTERVAL_STR:
        err_msg = NoneError.intervalInfoMessage

    # Second, raise the custom NoneError msg.
    raise NoneError(err_msg)


def zzz(sleep_time, dictionary: Dict):
    """The actual sleep."""
    try:
        time.sleep(sleep_time)
    except TypeError:
        sleep_time = delay_time_int(sleep_time, dictionary)
        time.sleep(sleep_time)
