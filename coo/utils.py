from string import Template
from typing import Dict
import time

import pendulum
from pendulum.parsing.exceptions import ParserError

from .exceptions import TemplateError, ScheduleError


TIME_DICT: Dict[str, int] = {
    "now": 0,
    "half_hour": 1800,
    "one_hour": 3600,
    "two_hours": 7200,
    "four_hours": 14400,
    "six_hours": 21600,
    "eight_hours": 28800,
    "ten_hours": 36000,
    "twelve_hours": 43200,
    "fourteen_hours": 50400,
    "sixteen_hours": 57600,
    "eighteen_hours": 64800,
    "twenty_hours": 72000,
    "twenty_two_hours": 79200,
    "one_day": 86400,
    "two_days": 172800,
    "three_days": 259200,
    "four_days": 345600,
    "five_days": 432000,
    "six_days": 518400,
    "one_week": 604800,
}


def parse_time(date_time: str, time_zone: str) -> int:
    """Returns the seconds between now and the scheduled time."""
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
    """Returns seconds from dictionaries, integers or a DateTime."""
    if isinstance(schedule_time, int):
        return schedule_time

    elif schedule_time in TIME_DICT:
        return TIME_DICT.get(schedule_time)

    try:
        return parse_time(schedule_time, time_zone)
    except ParserError:
        raise TypeError("An integer, valid datetime or string is needed.")


def zzz(sleep_time, time_zone: str = None):
    """Delay sleep and interval time sleep. """
    try:
        time.sleep(sleep_time)
    except TypeError:
        sleep_time = parse_or_get(sleep_time, time_zone)
        time.sleep(sleep_time)


def tweet_template(update: str, template: str) -> str:
    """Returns the the update in the template."""
    try:
        return Template(template).substitute(message=update)
    except TypeError:
        raise TemplateError(TemplateError.templateInfoMsg)
