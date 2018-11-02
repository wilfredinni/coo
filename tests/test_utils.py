import pytest

from auto_tweet.utils import (
    parse_time,
    parse_or_get,
    zzz,
    tweet_template,
    DELAY_DICT,
    INTERVAL_DICT,
)
from auto_tweet.exceptions import ScheduleError, TemplateError


# DICTIONARIES
@pytest.mark.parametrize(
    "time_delay, int_value",
    [
        ("now", 0),
        ("half_hour", 1800),
        ("one_hour", 3600),
        ("tomorrow", 86400),
        ("next_week", 604800),
    ],
)
def test_DELAY_DICT(time_delay, int_value):
    assert DELAY_DICT.get(time_delay) == int_value


@pytest.mark.parametrize(
    "time_delay, int_value",
    [
        ("test", 0),
        ("once_a_day", 86400),
        ("twice_perday", 43200),
        ("three_times_day", 28800),
    ],
)
def test_INTERVAL_DICT(time_delay, int_value):
    assert INTERVAL_DICT.get(time_delay) == int_value


# PARSE TIME
@pytest.mark.parametrize(
    "date_time, time_zone",
    [("2040-10-28 18:46", "America/Santiago"), ("2040-10-28", "America/Santiago")],
)
def test_parse_time(date_time, time_zone):
    secs = parse_time(date_time, time_zone)
    assert isinstance(secs, int)


@pytest.mark.parametrize(
    "schedule_time, time_zone",
    [("2015-10-28 18:46", "America/Santiago"), ("2002-10-28", "America/Santiago")],
)
def test_parse_time_ScheduleError(schedule_time, time_zone):
    with pytest.raises(ScheduleError):
        parse_time(schedule_time, time_zone)


# PARSE OR GET
@pytest.mark.parametrize(
    "schedule_time, time_zone",
    [
        (20, None),
        ("now", None),
        ("test", None),
        ("2040-10-28", "America/Santiago"),
        ("2040-10-28 18:46", "America/Santiago"),
    ],
)
def test_parse_or_get(schedule_time, time_zone):
    seconds = parse_or_get(schedule_time, time_zone)
    assert isinstance(seconds, int)


@pytest.mark.parametrize(
    "schedule_time, time_zone",
    [
        ("wrong_delay_time", "America/Santiago"),
        ("wrong_delay_time", "America/Santiago"),
    ],
)
def test_parse_or_get_TypeError(schedule_time, time_zone):
    with pytest.raises(TypeError):
        parse_or_get(schedule_time, time_zone)


# ZZZ
@pytest.mark.parametrize(
    "sleep_time, time_zone", [(0, None), ("now", None), ("test", None)]
)
def test_zzz_INT(sleep_time, time_zone):
    # TODO: test datetime strings
    zzz(sleep_time, time_zone)


# TWEET TEMPLATE
def test_tweet_template():
    assert isinstance(tweet_template("msg", "str"), str)


@pytest.mark.parametrize(
    "update, template",
    [
        ("msg", None),
        ("msg", (1, 2, 3)),
        ("msg", [1, 2, 3]),
        ("msg", {1, 2, 3}),
        ("msg", {1: 2}),
        ("msg", 1),
    ],
)
def test_tweet_template_TemplateError(update, template):
    with pytest.raises(TemplateError):
        tweet_template(update, template)
