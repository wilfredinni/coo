from string import Template
from typing import Dict
import time

import pendulum
from pendulum.parsing.exceptions import ParserError

from .exceptions import TemplateError, ScheduleError

DELAY_DICT: Dict[str, int] = {
    "now": 0,
    "half_hour": 1800,  # 1800
    "one_hour": 3600,  # 3600
    "tomorrow": 86400,  # 86400
    "next_week": 604800,  # 604800
}

INTERVAL_DICT: Dict[str, int] = {
    "test": 0,
    "once_a_day": 86400,  # 86400
    "twice_perday": 43200,  # 43200
    "three_times_day": 28800,  # 28800
}


def parse_time(date_time: str, time_zone: str) -> int:
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


def parse_or_get(schedule_time, time_zone):
    if isinstance(schedule_time, int):
        return schedule_time

    elif schedule_time in DELAY_DICT:
        return DELAY_DICT.get(schedule_time)

    elif schedule_time in INTERVAL_DICT:
        return INTERVAL_DICT.get(schedule_time)

    try:
        return parse_time(schedule_time, time_zone)
    except ParserError:
        raise TypeError("An integer, valid datetime or string is needed.")


def zzz(sleep_time, time_zone: str = None):
    try:
        time.sleep(sleep_time)
    except TypeError:
        sleep_time = parse_or_get(sleep_time, time_zone)
        time.sleep(sleep_time)


def tweet_template(update: str, template: str) -> str:
    try:
        return Template(template).substitute(message=update)
    except TypeError:
        raise TemplateError(TemplateError.templateInfoMsg)
