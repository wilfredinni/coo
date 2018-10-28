from string import Template
from typing import Dict
import time

import pendulum
from pendulum.parsing.exceptions import ParserError

from .exceptions import NoneError, TemplateError, ScheduleError

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


def parse_time(date_time: str, time_zone: str = None) -> int:
    if not time_zone:
        time_zone = "local"

    now = pendulum.now(time_zone)
    update = pendulum.parse(date_time, tz=time_zone)

    # If a time zone is not specified, it will be set to local.
    # When passing only time information the date will default to today.
    # The time will be set to 00:00:00 if it's not specified.
    # A future date is needed.

    secs = update - now

    if secs.seconds < 0:
        raise ScheduleError(ScheduleError.pastDateError)

    return secs.seconds


def get_time(time_delay: str, dictionary: Dict[str, int]) -> int:
    """Get the delay or interval time for a Twitter Update."""
    secs = dictionary.get(time_delay)

    if isinstance(secs, int):
        return secs

    # Get the correct error message.
    err_msg = NoneError.delayInfoMessage

    if dictionary is INTERVAL_DICT:
        err_msg = NoneError.intervalInfoMessage

    raise NoneError(err_msg)


def parse_or_get(schedule_time, time_zone):
    if isinstance(schedule_time, int):
        return schedule_time

    elif schedule_time in DELAY_DICT:
        return get_time(schedule_time, DELAY_DICT)

    try:
        return parse_time(schedule_time, time_zone)
    except ParserError:
        raise TypeError("An integer, valid datetime or string is needed.")


def zzz(sleep_time, dictionary: Dict[str, int]):
    try:
        time.sleep(sleep_time)
    except TypeError:
        sleep_time = get_time(sleep_time, dictionary)
        time.sleep(sleep_time)


def tweet_template(msg: str, template: str) -> str:
    try:
        return Template(template).substitute(message=msg)
    except TypeError:
        raise TemplateError(TemplateError.templateInfoMsg)
