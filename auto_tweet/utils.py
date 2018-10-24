from typing import Dict
from string import Template
import time

from .exceptions import NoneError, TemplateError

DELAY_DICT: Dict[str, int] = {
    "now": 0,
    "test": 1,
    "half_hour": 2,  # 1800
    "one_hour": 4,  # 3600
    "tomorrow": 6,  # 86400
    "next_week": 10,  # 604800
}

INTERVAL_DICT: Dict[str, int] = {
    "test": 1,
    "once_a_day": 2,  # 86400
    "twice_perday": 4,  # 43200
    "three_times_day": 6,  # 28800
}


def get_time(time_delay: str, dictionary: Dict[str, int]) -> int:
    """Get the time delay for a Twitter Update."""
    sleep_time = dictionary.get(time_delay)

    if isinstance(sleep_time, int):
        return sleep_time

    # If 'sleep_time' == None, get the correct error message.
    err_msg = NoneError.delayInfoMessage
    if dictionary is INTERVAL_DICT:
        err_msg = NoneError.intervalInfoMessage

    # And raise the custom NoneError.
    raise NoneError(err_msg)


def zzz(sleep_time, dictionary: Dict[str, int]):
    """The actual sleep."""
    try:
        time.sleep(sleep_time)
    except TypeError:
        sleep_time = get_time(sleep_time, dictionary)
        time.sleep(sleep_time)


def tweet_template(msg: str, template: str) -> str:
    """Process the Template if provided."""
    try:
        return Template(template).substitute(message=msg)
    except TypeError:
        raise TemplateError(TemplateError.templateInfoMsg)
