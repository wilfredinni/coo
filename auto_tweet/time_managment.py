from typing import Dict

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


def delay_time_int(time_delay, dictionary):
    """Delay a Twitter Update. """
    sleep_time = dictionary.get(time_delay)
    # At this point, the 'sleep_time' comes from the one of the
    # dictionaries. If the return value is 'None', means that the
    # value provided by the user is not valid, so an 'NoneError'
    # is raised.
    try:
        return sleep_time
    except TypeError:
        raise NoneError(NoneError.delayInfoMessage)
